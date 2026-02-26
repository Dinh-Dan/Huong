import os
from datetime import datetime, date
from flask import request, jsonify, g
from database.db import query, query_one, execute, get_connection

def submit_work(task_id):
    try:
        student_id = g.user['id']

        # Check task exists and active
        task = query_one('SELECT * FROM tasks WHERE id = %s AND status = %s', (task_id, 'active'))
        if not task:
            return jsonify({'message': 'Task not found or closed'}), 404

        # Check deadline
        deadline = task['deadline']
        if isinstance(deadline, date):
            deadline = datetime.combine(deadline, datetime.max.time())
        if deadline and deadline < datetime.now():
            return jsonify({'message': 'Task deadline has passed'}), 400

        # Check max submissions
        if task['max_submissions'] is not None and task['current_submissions'] >= task['max_submissions']:
            return jsonify({'message': 'Maximum submissions reached for this task'}), 400

        # Check duplicate
        existing = query_one('SELECT id FROM submissions WHERE task_id = %s AND student_id = %s', (task_id, student_id))
        if existing:
            return jsonify({'message': 'You have already submitted for this task'}), 400

        text_answer = request.form.get('text_answer') or None
        portfolio_link = request.form.get('portfolio_link') or None

        file_path = None
        if 'file' in request.files:
            f = request.files['file']
            if f.filename:
                upload_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads', 'submissions')
                os.makedirs(upload_dir, exist_ok=True)
                filename = f"{int(datetime.now().timestamp() * 1000)}-{f.filename}"
                f.save(os.path.join(upload_dir, filename))
                file_path = filename

        # Use a single connection for all write operations (atomic transaction)
        conn = get_connection()
        try:
            conn.autocommit(False)
            with conn.cursor() as cursor:
                cursor.execute(
                    '''INSERT INTO submissions (task_id, student_id, file_path, text_answer, portfolio_link)
                       VALUES (%s, %s, %s, %s, %s)''',
                    (task_id, student_id, file_path, text_answer, portfolio_link)
                )
                submission_id = cursor.lastrowid

                cursor.execute(
                    'UPDATE tasks SET current_submissions = current_submissions + 1 WHERE id = %s',
                    (task_id,)
                )
                cursor.execute(
                    'UPDATE students SET total_submissions = total_submissions + 1 WHERE id = %s',
                    (student_id,)
                )
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

        return jsonify({'message': 'Submission successful', 'submissionId': submission_id}), 201

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'message': f'Server error: {str(e)}'}), 500

def get_my_submissions():
    try:
        submissions = query(
            '''SELECT s.*, t.title as task_title, c.company_name
               FROM submissions s
               JOIN tasks t ON s.task_id = t.id
               JOIN companies c ON t.company_id = c.id
               WHERE s.student_id = %s
               ORDER BY s.submitted_at DESC''',
            (g.user['id'],)
        )
        return jsonify(submissions)
    except Exception as e:
        print(f'Get my submissions error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_task_submissions(task_id):
    try:
        task = query_one('SELECT id FROM tasks WHERE id = %s AND company_id = %s', (task_id, g.user['id']))
        if not task:
            return jsonify({'message': 'Task not found or access denied'}), 404

        submissions = query(
            '''SELECT s.*, st.full_name, st.university, st.email, st.skills, st.portfolio_link as student_portfolio, st.cv_path
               FROM submissions s
               JOIN students st ON s.student_id = st.id
               WHERE s.task_id = %s
               ORDER BY s.submitted_at DESC''',
            (task_id,)
        )
        return jsonify(submissions)
    except Exception as e:
        print(f'Get task submissions error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_all_company_submissions():
    try:
        submissions = query(
            '''SELECT s.*, st.full_name, st.university, st.email, st.skills, st.portfolio_link as student_portfolio, st.cv_path,
                      t.title as task_title
               FROM submissions s
               JOIN students st ON s.student_id = st.id
               JOIN tasks t ON s.task_id = t.id
               WHERE t.company_id = %s
               ORDER BY s.submitted_at DESC''',
            (g.user['id'],)
        )
        return jsonify(submissions)
    except Exception as e:
        print(f'Get all company submissions error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_submission(id):
    try:
        submission = query_one(
            '''SELECT s.*, st.full_name, st.university, st.email, st.skills, st.portfolio_link as student_portfolio, st.cv_path, st.phone,
                      t.title as task_title, t.description as task_description
               FROM submissions s
               JOIN students st ON s.student_id = st.id
               JOIN tasks t ON s.task_id = t.id
               WHERE s.id = %s''',
            (id,)
        )

        if not submission:
            return jsonify({'message': 'Submission not found'}), 404

        return jsonify(submission)
    except Exception as e:
        print(f'Get submission error: {e}')
        return jsonify({'message': 'Server error'}), 500
