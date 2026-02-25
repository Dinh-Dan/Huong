const db = require('../database/db');
const { validationResult } = require('express-validator');

// Browse tasks (public)
exports.browseTasks = async (req, res) => {
  try {
    const { industry, difficulty, search, page = 1, limit = 12 } = req.query;
    const offset = (page - 1) * limit;

    let where = 'WHERE t.status = "active"';
    const params = [];

    if (industry) {
      where += ' AND t.industry = ?';
      params.push(industry);
    }
    if (difficulty) {
      where += ' AND t.difficulty = ?';
      params.push(difficulty);
    }
    if (search) {
      where += ' AND (t.title LIKE ? OR t.description LIKE ?)';
      params.push(`%${search}%`, `%${search}%`);
    }

    // Get total count
    const [countResult] = await db.query(
      `SELECT COUNT(*) as total FROM tasks t ${where}`, params
    );

    // Get tasks with company info
    const [tasks] = await db.query(
      `SELECT t.*, c.company_name, c.logo_path, c.industry as company_industry
       FROM tasks t
       JOIN companies c ON t.company_id = c.id
       ${where}
       ORDER BY t.created_at DESC
       LIMIT ? OFFSET ?`,
      [...params, parseInt(limit), parseInt(offset)]
    );

    res.json({
      tasks,
      pagination: {
        total: countResult[0].total,
        page: parseInt(page),
        limit: parseInt(limit),
        totalPages: Math.ceil(countResult[0].total / limit)
      }
    });
  } catch (err) {
    console.error('Browse tasks error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get task detail
exports.getTask = async (req, res) => {
  try {
    const [tasks] = await db.query(
      `SELECT t.*, c.company_name, c.logo_path, c.industry as company_industry, c.website as company_website
       FROM tasks t
       JOIN companies c ON t.company_id = c.id
       WHERE t.id = ?`,
      [req.params.id]
    );

    if (tasks.length === 0) {
      return res.status(404).json({ message: 'Task not found' });
    }

    res.json(tasks[0]);
  } catch (err) {
    console.error('Get task error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Create task (company)
exports.createTask = async (req, res) => {
  try {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const companyId = req.user.id;

    // Check task limit
    const [company] = await db.query(
      'SELECT task_limit, tasks_used FROM companies WHERE id = ?',
      [companyId]
    );

    if (company[0].tasks_used >= company[0].task_limit) {
      return res.status(403).json({ message: 'Task limit reached. Please upgrade your plan.' });
    }

    const { title, description, expected_output, estimated_time, deadline, difficulty, industry, max_submissions } = req.body;

    const [result] = await db.query(
      `INSERT INTO tasks (company_id, title, description, expected_output, estimated_time, deadline, difficulty, industry, max_submissions)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      [companyId, title, description, expected_output, estimated_time, deadline, difficulty, industry, max_submissions || 50]
    );

    // Increment tasks_used
    await db.query('UPDATE companies SET tasks_used = tasks_used + 1 WHERE id = ?', [companyId]);

    res.status(201).json({ message: 'Task created successfully', taskId: result.insertId });
  } catch (err) {
    console.error('Create task error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Update task
exports.updateTask = async (req, res) => {
  try {
    const taskId = req.params.id;
    const companyId = req.user.id;

    // Verify ownership
    const [task] = await db.query('SELECT id FROM tasks WHERE id = ? AND company_id = ?', [taskId, companyId]);
    if (task.length === 0) {
      return res.status(404).json({ message: 'Task not found or access denied' });
    }

    const { title, description, expected_output, estimated_time, deadline, difficulty, industry, max_submissions, status } = req.body;

    await db.query(
      `UPDATE tasks SET title=?, description=?, expected_output=?, estimated_time=?, deadline=?, difficulty=?, industry=?, max_submissions=?, status=?
       WHERE id = ? AND company_id = ?`,
      [title, description, expected_output, estimated_time, deadline, difficulty, industry, max_submissions, status, taskId, companyId]
    );

    res.json({ message: 'Task updated successfully' });
  } catch (err) {
    console.error('Update task error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Delete task
exports.deleteTask = async (req, res) => {
  try {
    const [result] = await db.query(
      'DELETE FROM tasks WHERE id = ? AND company_id = ?',
      [req.params.id, req.user.id]
    );

    if (result.affectedRows === 0) {
      return res.status(404).json({ message: 'Task not found or access denied' });
    }

    res.json({ message: 'Task deleted successfully' });
  } catch (err) {
    console.error('Delete task error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get company's own tasks
exports.getMyTasks = async (req, res) => {
  try {
    const [tasks] = await db.query(
      `SELECT t.*, (SELECT COUNT(*) FROM submissions WHERE task_id = t.id) as submission_count
       FROM tasks t
       WHERE t.company_id = ?
       ORDER BY t.created_at DESC`,
      [req.user.id]
    );

    res.json(tasks);
  } catch (err) {
    console.error('Get my tasks error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
