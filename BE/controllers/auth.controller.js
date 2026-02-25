const db = require('../database/db');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { validationResult } = require('express-validator');

// Register Student
exports.registerStudent = async (req, res) => {
  try {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { full_name, email, password, university, major, year_of_study, skills, phone, portfolio_link, linkedin } = req.body;

    // Check email exists
    const [existing] = await db.query('SELECT id FROM students WHERE email = ?', [email]);
    if (existing.length > 0) {
      return res.status(400).json({ message: 'Email already registered' });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);

    // CV file path
    const cv_path = req.file ? req.file.filename : null;

    const [result] = await db.query(
      `INSERT INTO students (full_name, email, password, university, major, year_of_study, skills, phone, cv_path, portfolio_link, linkedin)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      [full_name, email, hashedPassword, university, major, year_of_study, skills, phone, cv_path, portfolio_link, linkedin]
    );

    // Generate JWT
    const token = jwt.sign(
      { id: result.insertId, role: 'student', email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN }
    );

    res.status(201).json({
      message: 'Student registered successfully',
      token,
      user: { id: result.insertId, name: full_name, email, role: 'student' }
    });
  } catch (err) {
    console.error('Register student error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Register Company
exports.registerCompany = async (req, res) => {
  try {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { company_name, registration_number, email, password, industry, company_size, website, address, description } = req.body;

    // Check email exists
    const [existing] = await db.query('SELECT id FROM companies WHERE email = ?', [email]);
    if (existing.length > 0) {
      return res.status(400).json({ message: 'Email already registered' });
    }

    // Check registration number
    const [existingReg] = await db.query('SELECT id FROM companies WHERE registration_number = ?', [registration_number]);
    if (existingReg.length > 0) {
      return res.status(400).json({ message: 'Registration number already exists' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    // File paths
    const files = req.files || {};
    const business_license_path = files.business_license ? files.business_license[0].filename : null;
    const logo_path = files.logo ? files.logo[0].filename : null;

    const [result] = await db.query(
      `INSERT INTO companies (company_name, registration_number, email, password, industry, company_size, website, address, description, business_license_path, logo_path)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      [company_name, registration_number, email, hashedPassword, industry, company_size, website, address, description, business_license_path, logo_path]
    );

    const token = jwt.sign(
      { id: result.insertId, role: 'company', email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN }
    );

    res.status(201).json({
      message: 'Company registered successfully',
      token,
      user: { id: result.insertId, name: company_name, email, role: 'company' }
    });
  } catch (err) {
    console.error('Register company error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Login
exports.login = async (req, res) => {
  try {
    const { email, password, role } = req.body;

    if (!email || !password || !role) {
      return res.status(400).json({ message: 'Email, password and role are required' });
    }

    let user;
    if (role === 'student') {
      const [rows] = await db.query('SELECT * FROM students WHERE email = ?', [email]);
      user = rows[0];
    } else if (role === 'company') {
      const [rows] = await db.query('SELECT * FROM companies WHERE email = ?', [email]);
      user = rows[0];
    } else {
      return res.status(400).json({ message: 'Invalid role' });
    }

    if (!user) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }

    const name = role === 'student' ? user.full_name : user.company_name;

    const token = jwt.sign(
      { id: user.id, role, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN }
    );

    res.json({
      message: 'Login successful',
      token,
      user: { id: user.id, name, email: user.email, role }
    });
  } catch (err) {
    console.error('Login error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get current user info
exports.getMe = async (req, res) => {
  try {
    const { id, role } = req.user;
    let user;

    if (role === 'student') {
      const [rows] = await db.query(
        'SELECT id, full_name, email, university, major, year_of_study, skills, phone, cv_path, portfolio_link, linkedin, avatar_path, total_score, average_score, total_submissions, interested_count FROM students WHERE id = ?',
        [id]
      );
      user = rows[0];
    } else {
      const [rows] = await db.query(
        'SELECT id, company_name, email, industry, company_size, website, address, description, logo_path, subscription_plan, task_limit, tasks_used, subscription_expiry FROM companies WHERE id = ?',
        [id]
      );
      user = rows[0];
    }

    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    res.json({ ...user, role });
  } catch (err) {
    console.error('Get me error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Check email availability
exports.checkEmail = async (req, res) => {
  try {
    const { email, role } = req.query;
    const table = role === 'company' ? 'companies' : 'students';
    const [rows] = await db.query(`SELECT id FROM ${table} WHERE email = ?`, [email]);
    res.json({ available: rows.length === 0 });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
};
