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

        expiry = datetime.now() + timedelta(days=30)

        execute(
            'UPDATE companies SET subscription_plan = %s, task_limit = %s, subscription_expiry = %s WHERE id = %s',
            (plan, plan_details['task_limit'], expiry, g.user['id'])
        )

        return jsonify({'message': f'Plan upgraded to {plan} successfully'})

    except Exception as e:
        print(f'Upgrade plan error: {e}')
        return jsonify({'message': 'Server error'}), 500
