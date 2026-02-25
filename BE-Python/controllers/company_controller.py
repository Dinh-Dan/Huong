import os
from datetime import datetime
from flask import request, jsonify, g
from database.db import query, query_one, execute

def get_profile():
    try:
        company = query_one(
            '''SELECT id, company_name, email, industry, company_size, website, address, description,
                      logo_path, business_license_path, subscription_plan, task_limit, tasks_used, subscription_expiry, created_at
               FROM companies WHERE id = %s''',
            (g.user['id'],)
        )

        if not company:
            return jsonify({'message': 'Company not found'}), 404

        return jsonify(company)

    except Exception as e:
        print(f'Get company profile error: {e}')
        return jsonify({'message': 'Server error'}), 500

def update_profile():
    try:
        data = request.form
        company_name = data.get('company_name')
        industry = data.get('industry')
        company_size = data.get('company_size')
        website = data.get('website')
        address = data.get('address')
        description = data.get('description')

        logo_path = None
        if 'logo' in request.files:
            f = request.files['logo']
            if f.filename:
                filename = f"{int(datetime.now().timestamp() * 1000)}-{f.filename}"
                f.save(os.path.join('uploads', 'logos', filename))
                logo_path = filename

        sql = 'UPDATE companies SET company_name=%s, industry=%s, company_size=%s, website=%s, address=%s, description=%s'
        params = [company_name, industry, company_size, website, address, description]

        if logo_path:
            sql += ', logo_path=%s'
            params.append(logo_path)

        sql += ' WHERE id=%s'
        params.append(g.user['id'])

        execute(sql, params)
        return jsonify({'message': 'Profile updated successfully'})

    except Exception as e:
        print(f'Update company profile error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_dashboard():
    try:
        company_id = g.user['id']

        company = query_one(
            'SELECT subscription_plan, task_limit, tasks_used FROM companies WHERE id = %s',
            (company_id,)
        )

        total_tasks = query_one(
            'SELECT COUNT(*) as count FROM tasks WHERE company_id = %s',
            (company_id,)
        )

        total_submissions = query_one(
            '''SELECT COUNT(*) as count FROM submissions s
               JOIN tasks t ON s.task_id = t.id
               WHERE t.company_id = %s''',
            (company_id,)
        )

        interested_count = query_one(
            '''SELECT COUNT(*) as count FROM submissions s
               JOIN tasks t ON s.task_id = t.id
               WHERE t.company_id = %s AND s.status = 'interested' ''',
            (company_id,)
        )

        recent_tasks = query(
            '''SELECT t.*, (SELECT COUNT(*) FROM submissions WHERE task_id = t.id) as submission_count
               FROM tasks t WHERE t.company_id = %s
               ORDER BY t.created_at DESC LIMIT 5''',
            (company_id,)
        )

        return jsonify({
            'subscription_plan': company['subscription_plan'] if company else 'basic',
            'task_limit': company['task_limit'] if company else 2,
            'tasks_used': company['tasks_used'] if company else 0,
            'total_tasks': total_tasks['count'],
            'total_submissions': total_submissions['count'],
            'interested_candidates': interested_count['count'],
            'recent_tasks': recent_tasks
        })

    except Exception as e:
        print(f'Get company dashboard error: {e}')
        return jsonify({'message': 'Server error'}), 500
