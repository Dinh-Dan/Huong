import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from flask import request, jsonify, g
from database.db import query, query_one, execute

def register_student():
    try:
        # Get form data (multipart)
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        university = request.form.get('university', '').strip()
        major = request.form.get('major', '').strip()
        phone = request.form.get('phone', '').strip()
        year_of_study = request.form.get('year_of_study')
        skills = request.form.get('skills', '')
        portfolio_link = request.form.get('portfolio_link', '')
        linkedin = request.form.get('linkedin', '')

        # Validation
        errors = []
        if not full_name:
            errors.append({'path': 'full_name', 'msg': 'Full name is required'})
        if not email or '@' not in email:
            errors.append({'path': 'email', 'msg': 'Valid email is required'})
        if len(password) < 6:
            errors.append({'path': 'password', 'msg': 'Password must be at least 6 characters'})
        if not university:
            errors.append({'path': 'university', 'msg': 'University is required'})
        if not major:
            errors.append({'path': 'major', 'msg': 'Major is required'})
        if not phone:
            errors.append({'path': 'phone', 'msg': 'Phone is required'})

        if errors:
            return jsonify({'errors': errors}), 400

        # Check email exists
        existing = query_one('SELECT id FROM students WHERE email = %s', (email,))
        if existing:
            return jsonify({'message': 'Email already registered'}), 400

        # Hash password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # CV file
        cv_path = None
        if 'cv' in request.files:
            f = request.files['cv']
            if f.filename:
                filename = f"{int(datetime.now().timestamp() * 1000)}-{f.filename}"
                f.save(os.path.join('uploads', 'cv', filename))
                cv_path = filename

        cursor = execute(
            '''INSERT INTO students (full_name, email, password, university, major, year_of_study, skills, phone, cv_path, portfolio_link, linkedin)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (full_name, email, hashed, university, major, year_of_study, skills, phone, cv_path, portfolio_link, linkedin)
        )
        student_id = cursor.lastrowid

        token = jwt.encode(
            {'id': student_id, 'role': 'student', 'email': email, 'exp': datetime.utcnow() + timedelta(days=7)},
            os.getenv('JWT_SECRET'), algorithm='HS256'
        )

        return jsonify({
            'message': 'Student registered successfully',
            'token': token,
            'user': {'id': student_id, 'name': full_name, 'email': email, 'role': 'student'}
        }), 201

    except Exception as e:
        print(f'Register student error: {e}')
        return jsonify({'message': 'Server error'}), 500

def register_company():
    try:
        company_name = request.form.get('company_name', '').strip()
        registration_number = request.form.get('registration_number', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        industry = request.form.get('industry', '').strip()
        company_size = request.form.get('company_size', '')
        website = request.form.get('website', '')
        address = request.form.get('address', '')
        description = request.form.get('description', '')

        # Validation
        errors = []
        if not company_name:
            errors.append({'path': 'company_name', 'msg': 'Company name is required'})
        if not registration_number:
            errors.append({'path': 'registration_number', 'msg': 'Registration number is required'})
        if not email or '@' not in email:
            errors.append({'path': 'email', 'msg': 'Valid email is required'})
        if len(password) < 6:
            errors.append({'path': 'password', 'msg': 'Password must be at least 6 characters'})
        if not industry:
            errors.append({'path': 'industry', 'msg': 'Industry is required'})

        if errors:
            return jsonify({'errors': errors}), 400

        # Check email exists
        existing = query_one('SELECT id FROM companies WHERE email = %s', (email,))
        if existing:
            return jsonify({'message': 'Email already registered'}), 400

        # Check registration number
        existing_reg = query_one('SELECT id FROM companies WHERE registration_number = %s', (registration_number,))
        if existing_reg:
            return jsonify({'message': 'Registration number already exists'}), 400

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # File paths
        business_license_path = None
        logo_path = None

        if 'business_license' in request.files:
            f = request.files['business_license']
            if f.filename:
                filename = f"{int(datetime.now().timestamp() * 1000)}-{f.filename}"
                f.save(os.path.join('uploads', 'licenses', filename))
                business_license_path = filename

        if 'logo' in request.files:
            f = request.files['logo']
            if f.filename:
                filename = f"{int(datetime.now().timestamp() * 1000)}-{f.filename}"
                f.save(os.path.join('uploads', 'logos', filename))
                logo_path = filename

        cursor = execute(
            '''INSERT INTO companies (company_name, registration_number, email, password, industry, company_size, website, address, description, business_license_path, logo_path)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (company_name, registration_number, email, hashed, industry, company_size, website, address, description, business_license_path, logo_path)
        )
        company_id = cursor.lastrowid

        token = jwt.encode(
            {'id': company_id, 'role': 'company', 'email': email, 'exp': datetime.utcnow() + timedelta(days=7)},
            os.getenv('JWT_SECRET'), algorithm='HS256'
        )

        return jsonify({
            'message': 'Company registered successfully',
            'token': token,
            'user': {'id': company_id, 'name': company_name, 'email': email, 'role': 'company'}
        }), 201

    except Exception as e:
        print(f'Register company error: {e}')
        return jsonify({'message': 'Server error'}), 500

def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not email or not password or not role:
            return jsonify({'message': 'Email, password and role are required'}), 400

        if role == 'student':
            user = query_one('SELECT * FROM students WHERE email = %s', (email,))
        elif role == 'company':
            user = query_one('SELECT * FROM companies WHERE email = %s', (email,))
        else:
            return jsonify({'message': 'Invalid role'}), 400

        if not user:
            return jsonify({'message': 'Invalid email or password'}), 401

        if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return jsonify({'message': 'Invalid email or password'}), 401

        name = user['full_name'] if role == 'student' else user['company_name']

        token = jwt.encode(
            {'id': user['id'], 'role': role, 'email': user['email'], 'exp': datetime.utcnow() + timedelta(days=7)},
            os.getenv('JWT_SECRET'), algorithm='HS256'
        )

        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {'id': user['id'], 'name': name, 'email': user['email'], 'role': role}
        })

    except Exception as e:
        print(f'Login error: {e}')
        return jsonify({'message': 'Server error'}), 500

def get_me():
    try:
        user_id = g.user['id']
        role = g.user['role']

        if role == 'student':
            user = query_one(
                '''SELECT id, full_name, email, university, major, year_of_study, skills, phone, cv_path,
                          portfolio_link, linkedin, avatar_path, total_score, average_score, total_submissions, interested_count
                   FROM students WHERE id = %s''', (user_id,)
            )
        else:
            user = query_one(
                '''SELECT id, company_name, email, industry, company_size, website, address, description,
                          logo_path, subscription_plan, task_limit, tasks_used, subscription_expiry
                   FROM companies WHERE id = %s''', (user_id,)
            )

        if not user:
            return jsonify({'message': 'User not found'}), 404

        user['role'] = role
        return jsonify(user)

    except Exception as e:
        print(f'Get me error: {e}')
        return jsonify({'message': 'Server error'}), 500

def check_email():
    try:
        email = request.args.get('email')
        role = request.args.get('role')
        table = 'companies' if role == 'company' else 'students'
        row = query_one(f'SELECT id FROM {table} WHERE email = %s', (email,))
        return jsonify({'available': row is None})
    except Exception as e:
        return jsonify({'message': 'Server error'}), 500
