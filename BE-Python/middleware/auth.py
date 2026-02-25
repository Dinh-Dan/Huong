import jwt
import os
from functools import wraps
from flask import request, jsonify, g

def authenticate_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        token = auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else None

        if not token:
            return jsonify({'message': 'Access token required'}), 401

        try:
            decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
            g.user = decoded
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Invalid or expired token'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid or expired token'}), 403

        return f(*args, **kwargs)
    return decorated

def optional_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        token = auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else None

        g.user = None
        if token:
            try:
                decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                g.user = decoded
            except Exception:
                pass

        return f(*args, **kwargs)
    return decorated
