import os
from datetime import datetime
from flask import request, jsonify, g
from database.db import query, query_one, execute

def get_profile():
    try:
        student = query_one(
            '''SELECT id, full_name, email, university, major, year_of_study, skills, phone, cv_path,
                      portfolio_link, linkedin, avatar_path, total_score, average_score, total_submissions, interested_count, created_at
               FROM students WHERE id = %s''',
            (g.user['id'],)
        )

        if not student:
            return jsonify({'message': 'Student not found'}), 404

        return jsonify(student)

    except Exception as e:
        print(f'Get student profile error: {e}')
        return jsonify({'message': 'Server error'}), 500

def update_profile():
    try:
        data = request.form
        full_name = data.get('full_name')
        university = data.get('university')
        major = data.get('major')
        year_of_study = data.get('year_of_study')
        skills = data.get('skills')
        phone = data.get('phone')
        portfolio_link = data.get('portfolio_link')
        linkedin = data.get('linkedin')

        cv_path = None
        if 'cv' in request.files:
            f = request.files['cv']
            if f.filename:
                filename = f"{int(datetime.now().timestamp() * 1000)}-{f.filename}"
                f.save(os.path.join('uploads', 'cv', filename))
                cv_path = filename

        sql = 'UPDATE students SET full_name=%s, university=%s, major=%s, year_of_study=%s, skills=%s, phone=%s, portfolio_link=%s, linkedin=%s'
        params = [full_name, university, major, year_of_study, skills, phone, portfolio_link, linkedin]

        if cv_path:
            sql += ', cv_path=%s'
            params.append(cv_path)

        sql += ' WHERE id=%s'
        params.append(g.user['id'])

        execute(sql, params)
        return jsonify({'message': 'Profile updated successfully'})

    except Exception as e:
        print(f'Update student profile error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_dashboard():
    try:
        student_id = g.user['id']

        student = query_one(
            'SELECT total_submissions, interested_count FROM students WHERE id = %s',
            (student_id,)
        )

        pending = query_one(
            'SELECT COUNT(*) as count FROM submissions WHERE student_id = %s AND status = "pending"',
            (student_id,)
        )

        recent = query(
            '''SELECT s.*, t.title as task_title, c.company_name
               FROM submissions s
               JOIN tasks t ON s.task_id = t.id
               JOIN companies c ON t.company_id = c.id
               WHERE s.student_id = %s
               ORDER BY s.submitted_at DESC
               LIMIT 5''',
            (student_id,)
        )

        return jsonify({
            'total_submissions': student['total_submissions'] if student else 0,
            'pending_review': pending['count'],
            'interested_count': student['interested_count'] if student else 0,
            'recent_submissions': recent
        })

    except Exception as e:
        print(f'Get dashboard error: {e}')
        return jsonify({'message': 'Server error'}), 500
