import math
from flask import request, jsonify, g
from database.db import query, query_one, execute

def browse_tasks():
    try:
        industry = request.args.get('industry')
        difficulty = request.args.get('difficulty')
        search = request.args.get('search')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 12))
        offset = (page - 1) * limit

        where = 'WHERE t.status = "active"'
        params = []

        if industry:
            where += ' AND t.industry = %s'
            params.append(industry)
        if difficulty:
            where += ' AND t.difficulty = %s'
            params.append(difficulty)
        if search:
            where += ' AND (t.title LIKE %s OR t.description LIKE %s)'
            params.extend([f'%{search}%', f'%{search}%'])

        count_result = query_one(f'SELECT COUNT(*) as total FROM tasks t {where}', params)
        total = count_result['total']

        tasks = query(
            f'''SELECT t.*, c.company_name, c.logo_path, c.industry as company_industry
                FROM tasks t
                JOIN companies c ON t.company_id = c.id
                {where}
                ORDER BY t.created_at DESC
                LIMIT %s OFFSET %s''',
            params + [limit, offset]
        )

        return jsonify({
            'tasks': tasks,
            'pagination': {
                'total': total,
                'page': page,
                'limit': limit,
                'totalPages': math.ceil(total / limit) if limit else 0
            }
        })

    except Exception as e:
        print(f'Browse tasks error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_task(id):
    try:
        task = query_one(
            '''SELECT t.*, c.company_name, c.logo_path, c.industry as company_industry, c.website as company_website
               FROM tasks t
               JOIN companies c ON t.company_id = c.id
               WHERE t.id = %s''', (id,)
        )

        if not task:
            return jsonify({'message': 'Task not found'}), 404

        return jsonify(task)

    except Exception as e:
        print(f'Get task error: {e}')
        return jsonify({'message': 'Server error'}), 500

def create_task():
    try:
        data = request.get_json()

        # Validation
        errors = []
        if not data.get('title'):
            errors.append({'path': 'title', 'msg': 'Title is required'})
        if not data.get('description'):
            errors.append({'path': 'description', 'msg': 'Description is required'})
        if not data.get('deadline'):
            errors.append({'path': 'deadline', 'msg': 'Deadline is required'})
        if data.get('difficulty') not in ('easy', 'medium', 'hard'):
            errors.append({'path': 'difficulty', 'msg': 'Invalid difficulty'})
        if errors:
            return jsonify({'errors': errors}), 400

        company_id = g.user['id']

        # Check task limit
        company = query_one('SELECT task_limit, tasks_used FROM companies WHERE id = %s', (company_id,))
        if company['tasks_used'] >= company['task_limit']:
            return jsonify({'message': 'Task limit reached. Please upgrade your plan.'}), 403

        cursor = execute(
            '''INSERT INTO tasks (company_id, title, description, expected_output, estimated_time, deadline, difficulty, industry, max_submissions)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (company_id, data['title'], data['description'], data.get('expected_output'),
             data.get('estimated_time'), data['deadline'], data['difficulty'],
             data.get('industry'), data.get('max_submissions', 50))
        )

        execute('UPDATE companies SET tasks_used = tasks_used + 1 WHERE id = %s', (company_id,))

        return jsonify({'message': 'Task created successfully', 'taskId': cursor.lastrowid}), 201

    except Exception as e:
        print(f'Create task error: {e}')
        return jsonify({'message': 'Server error'}), 500

def update_task(id):
    try:
        company_id = g.user['id']

        task = query_one('SELECT id FROM tasks WHERE id = %s AND company_id = %s', (id, company_id))
        if not task:
            return jsonify({'message': 'Task not found or access denied'}), 404

        data = request.get_json()
        execute(
            '''UPDATE tasks SET title=%s, description=%s, expected_output=%s, estimated_time=%s,
               deadline=%s, difficulty=%s, industry=%s, max_submissions=%s, status=%s
               WHERE id = %s AND company_id = %s''',
            (data.get('title'), data.get('description'), data.get('expected_output'),
             data.get('estimated_time'), data.get('deadline'), data.get('difficulty'),
             data.get('industry'), data.get('max_submissions'), data.get('status'),
             id, company_id)
        )

        return jsonify({'message': 'Task updated successfully'})

    except Exception as e:
        print(f'Update task error: {e}')
        return jsonify({'message': 'Server error'}), 500

def delete_task(id):
    try:
        cursor = execute('DELETE FROM tasks WHERE id = %s AND company_id = %s', (id, g.user['id']))
        if cursor.rowcount == 0:
            return jsonify({'message': 'Task not found or access denied'}), 404
        return jsonify({'message': 'Task deleted successfully'})
    except Exception as e:
        print(f'Delete task error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_my_tasks():
    try:
        tasks = query(
            '''SELECT t.*, (SELECT COUNT(*) FROM submissions WHERE task_id = t.id) as submission_count
               FROM tasks t
               WHERE t.company_id = %s
               ORDER BY t.created_at DESC''',
            (g.user['id'],)
        )
        return jsonify(tasks)
    except Exception as e:
        print(f'Get my tasks error: {e}')
        return jsonify({'message': 'Server error'}), 500
