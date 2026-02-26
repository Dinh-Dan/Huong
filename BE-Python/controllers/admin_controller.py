import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from flask import request, jsonify, g
from database.db import query, query_one, execute


def admin_login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        admin = query_one('SELECT * FROM admins WHERE username = %s', (username,))
        if not admin:
            return jsonify({'message': 'Invalid credentials'}), 401

        if not bcrypt.checkpw(password.encode('utf-8'), admin['password'].encode('utf-8')):
            return jsonify({'message': 'Invalid credentials'}), 401

        token = jwt.encode(
            {'id': admin['id'], 'role': 'admin', 'username': username, 'exp': datetime.utcnow() + timedelta(days=7)},
            os.getenv('JWT_SECRET'), algorithm='HS256'
        )

        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {'id': admin['id'], 'name': admin['full_name'], 'username': username, 'role': 'admin'}
        })

    except Exception as e:
        print(f'Admin login error: {e}')
        return jsonify({'message': 'Server error'}), 500


def get_dashboard_stats():
    try:
        total_students = query_one('SELECT COUNT(*) as count FROM students')['count']
        total_companies = query_one('SELECT COUNT(*) as count FROM companies')['count']
        total_tasks = query_one('SELECT COUNT(*) as count FROM tasks')['count']
        total_submissions = query_one('SELECT COUNT(*) as count FROM submissions')['count']

        pending_requests = query_one(
            "SELECT COUNT(*) as count FROM upgrade_requests WHERE status = 'pending'"
        )['count']

        plans_distribution = query(
            "SELECT subscription_plan, COUNT(*) as count FROM companies GROUP BY subscription_plan"
        )

        # Revenue estimate
        revenue = query_one('''
            SELECT
                COALESCE(SUM(CASE WHEN subscription_plan = 'standard' THEN 49.99
                                  WHEN subscription_plan = 'premium' THEN 99.99
                                  ELSE 0 END), 0) as total
            FROM companies
            WHERE subscription_plan != 'basic'
              AND subscription_expiry >= CURDATE()
        ''')

        recent_companies = query(
            'SELECT id, company_name, email, industry, subscription_plan, created_at FROM companies ORDER BY created_at DESC LIMIT 5'
        )

        recent_students = query(
            'SELECT id, full_name, email, university, created_at FROM students ORDER BY created_at DESC LIMIT 5'
        )

        return jsonify({
            'total_students': total_students,
            'total_companies': total_companies,
            'total_tasks': total_tasks,
            'total_submissions': total_submissions,
            'pending_requests': pending_requests,
            'revenue': float(revenue['total']) if revenue else 0,
            'plans_distribution': plans_distribution,
            'recent_companies': recent_companies,
            'recent_students': recent_students
        })

    except Exception as e:
        print(f'Admin dashboard error: {e}')
        return jsonify({'message': 'Server error'}), 500


def get_all_companies():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 20))
        search = request.args.get('search', '').strip()
        offset = (page - 1) * limit

        where = ''
        params = []
        if search:
            where = 'WHERE company_name LIKE %s OR email LIKE %s'
            params = [f'%{search}%', f'%{search}%']

        total = query_one(f'SELECT COUNT(*) as count FROM companies {where}', params)['count']

        companies = query(
            f'''SELECT id, company_name, email, industry, company_size, subscription_plan,
                       task_limit, tasks_used, subscription_expiry, created_at
                FROM companies {where}
                ORDER BY created_at DESC LIMIT %s OFFSET %s''',
            params + [limit, offset]
        )

        return jsonify({
            'data': companies,
            'pagination': {'page': page, 'limit': limit, 'total': total, 'pages': (total + limit - 1) // limit}
        })

    except Exception as e:
        print(f'Get all companies error: {e}')
        return jsonify({'message': 'Server error'}), 500


def get_all_students():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 20))
        search = request.args.get('search', '').strip()
        offset = (page - 1) * limit

        where = ''
        params = []
        if search:
            where = 'WHERE full_name LIKE %s OR email LIKE %s'
            params = [f'%{search}%', f'%{search}%']

        total = query_one(f'SELECT COUNT(*) as count FROM students {where}', params)['count']

        students = query(
            f'''SELECT id, full_name, email, university, major, average_score,
                       total_submissions, interested_count, created_at
                FROM students {where}
                ORDER BY created_at DESC LIMIT %s OFFSET %s''',
            params + [limit, offset]
        )

        return jsonify({
            'data': students,
            'pagination': {'page': page, 'limit': limit, 'total': total, 'pages': (total + limit - 1) // limit}
        })

    except Exception as e:
        print(f'Get all students error: {e}')
        return jsonify({'message': 'Server error'}), 500


def delete_company(company_id):
    try:
        company = query_one('SELECT id, company_name FROM companies WHERE id = %s', (company_id,))
        if not company:
            return jsonify({'message': 'Company not found'}), 404

        execute('DELETE FROM companies WHERE id = %s', (company_id,))
        return jsonify({'message': f'Company "{company["company_name"]}" deleted successfully'})

    except Exception as e:
        print(f'Delete company error: {e}')
        return jsonify({'message': 'Server error'}), 500


def delete_student(student_id):
    try:
        student = query_one('SELECT id, full_name FROM students WHERE id = %s', (student_id,))
        if not student:
            return jsonify({'message': 'Student not found'}), 404

        execute('DELETE FROM students WHERE id = %s', (student_id,))
        return jsonify({'message': f'Student "{student["full_name"]}" deleted successfully'})

    except Exception as e:
        print(f'Delete student error: {e}')
        return jsonify({'message': 'Server error'}), 500


def get_upgrade_requests():
    try:
        status_filter = request.args.get('status', '')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 20))
        offset = (page - 1) * limit

        where = ''
        params = []
        if status_filter in ('pending', 'approved', 'rejected'):
            where = 'WHERE ur.status = %s'
            params = [status_filter]

        total = query_one(
            f'SELECT COUNT(*) as count FROM upgrade_requests ur {where}', params
        )['count']

        requests_list = query(
            f'''SELECT ur.id, ur.company_id, c.company_name, c.email,
                       ur.current_plan, ur.requested_plan, ur.status,
                       ur.admin_note, ur.created_at, ur.processed_at
                FROM upgrade_requests ur
                JOIN companies c ON ur.company_id = c.id
                {where}
                ORDER BY ur.created_at DESC LIMIT %s OFFSET %s''',
            params + [limit, offset]
        )

        return jsonify({
            'data': requests_list,
            'pagination': {'page': page, 'limit': limit, 'total': total, 'pages': (total + limit - 1) // limit}
        })

    except Exception as e:
        print(f'Get upgrade requests error: {e}')
        return jsonify({'message': 'Server error'}), 500


def process_upgrade_request(request_id):
    try:
        data = request.get_json()
        action = data.get('action')  # 'approved' or 'rejected'
        admin_note = data.get('admin_note', '')

        if action not in ('approved', 'rejected'):
            return jsonify({'message': 'Invalid action. Must be approved or rejected'}), 400

        req = query_one('SELECT * FROM upgrade_requests WHERE id = %s', (request_id,))
        if not req:
            return jsonify({'message': 'Request not found'}), 404

        if req['status'] != 'pending':
            return jsonify({'message': 'Request already processed'}), 400

        # Update request status
        execute(
            'UPDATE upgrade_requests SET status = %s, admin_note = %s, processed_at = NOW() WHERE id = %s',
            (action, admin_note, request_id)
        )

        if action == 'approved':
            plan_details = query_one(
                'SELECT * FROM subscription_plans WHERE plan_name = %s',
                (req['requested_plan'],)
            )
            if plan_details:
                expiry = datetime.now() + timedelta(days=30)
                execute(
                    'UPDATE companies SET subscription_plan = %s, task_limit = %s, subscription_expiry = %s WHERE id = %s',
                    (req['requested_plan'], plan_details['task_limit'], expiry, req['company_id'])
                )

        return jsonify({'message': f'Request {action} successfully'})

    except Exception as e:
        print(f'Process upgrade request error: {e}')
        return jsonify({'message': 'Server error'}), 500


def create_admin():
    """Utility to create admin account - call once then remove or protect"""
    try:
        data = request.get_json()
        username = data.get('username', 'admin')
        password = data.get('password', 'admin123')
        full_name = data.get('full_name', 'Admin Huong')

        existing = query_one('SELECT id FROM admins WHERE username = %s', (username,))
        if existing:
            return jsonify({'message': 'Admin already exists'}), 400

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        execute(
            'INSERT INTO admins (username, password, full_name) VALUES (%s, %s, %s)',
            (username, hashed, full_name)
        )

        return jsonify({'message': f'Admin "{username}" created successfully'}), 201

    except Exception as e:
        print(f'Create admin error: {e}')
        return jsonify({'message': 'Server error'}), 500
