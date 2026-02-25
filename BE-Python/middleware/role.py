from functools import wraps
from flask import jsonify, g
from database.db import query_one

def require_role(*roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = getattr(g, 'user', None)
            if not user:
                return jsonify({'message': 'Authentication required'}), 401
            if user.get('role') not in roles:
                return jsonify({'message': 'Access denied. Insufficient permissions.'}), 403
            return f(*args, **kwargs)
        return decorated
    return decorator

def require_plan(*plans):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = getattr(g, 'user', None)
            if not user or user.get('role') != 'company':
                return jsonify({'message': 'Company access required'}), 403

            row = query_one('SELECT subscription_plan FROM companies WHERE id = %s', (user['id'],))
            if not row:
                return jsonify({'message': 'Company not found'}), 404

            plan_hierarchy = {'basic': 1, 'standard': 2, 'premium': 3}
            company_level = plan_hierarchy.get(row['subscription_plan'], 0)
            required_level = min(plan_hierarchy.get(p, 0) for p in plans)

            if company_level < required_level:
                return jsonify({'message': f'This feature requires {plans[0]} plan or higher'}), 403

            g.company_plan = row['subscription_plan']
            return f(*args, **kwargs)
        return decorated
    return decorator
