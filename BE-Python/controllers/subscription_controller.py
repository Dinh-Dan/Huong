from datetime import datetime, timedelta
from flask import request, jsonify, g
from database.db import query, query_one, execute

def get_plans():
    try:
        plans = query('SELECT * FROM subscription_plans ORDER BY id')
        return jsonify(plans)
    except Exception as e:
        print(f'Get plans error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_current_plan():
    try:
        company = query_one(
            'SELECT subscription_plan, task_limit, tasks_used, subscription_expiry FROM companies WHERE id = %s',
            (g.user['id'],)
        )

        if not company:
            return jsonify({'message': 'Company not found'}), 404

        plan_details = query_one(
            'SELECT * FROM subscription_plans WHERE plan_name = %s',
            (company['subscription_plan'],)
        )

        result = {**company, 'plan_details': plan_details}
        return jsonify(result)

    except Exception as e:
        print(f'Get current plan error: {e}')
        return jsonify({'message': 'Server error'}), 500

def upgrade_plan():
    try:
        data = request.get_json()
        plan = data.get('plan')

        if plan not in ('basic', 'standard', 'premium'):
            return jsonify({'message': 'Invalid plan'}), 400

        plan_details = query_one('SELECT * FROM subscription_plans WHERE plan_name = %s', (plan,))
        if not plan_details:
            return jsonify({'message': 'Plan not found'}), 400

        company = query_one('SELECT subscription_plan FROM companies WHERE id = %s', (g.user['id'],))
        if not company:
            return jsonify({'message': 'Company not found'}), 404

        if company['subscription_plan'] == plan:
            return jsonify({'message': 'You are already on this plan'}), 400

        # Check if there is already a pending request for this plan
        existing = query_one(
            "SELECT id FROM upgrade_requests WHERE company_id = %s AND requested_plan = %s AND status = 'pending'",
            (g.user['id'], plan)
        )
        if existing:
            return jsonify({'message': 'You already have a pending request for this plan. Please wait for admin approval.'}), 400

        # Create upgrade request instead of direct upgrade
        execute(
            'INSERT INTO upgrade_requests (company_id, current_plan, requested_plan) VALUES (%s, %s, %s)',
            (g.user['id'], company['subscription_plan'], plan)
        )

        return jsonify({'message': 'Upgrade request submitted successfully. Please wait for admin approval.'})

    except Exception as e:
        print(f'Upgrade plan error: {e}')
        return jsonify({'message': 'Server error'}), 500
