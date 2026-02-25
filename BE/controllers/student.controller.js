const db = require('../database/db');

// Get student profile
exports.getProfile = async (req, res) => {
  try {
    const [student] = await db.query(
      `SELECT id, full_name, email, university, major, year_of_study, skills, phone, cv_path,
              portfolio_link, linkedin, avatar_path, total_score, average_score, total_submissions, interested_count, created_at
       FROM students WHERE id = ?`,
      [req.user.id]
    );

    if (student.length === 0) {
      return res.status(404).json({ message: 'Student not found' });
    }

    res.json(student[0]);
  } catch (err) {
    console.error('Get student profile error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Update student profile
exports.updateProfile = async (req, res) => {
  try {
    const { full_name, university, major, year_of_study, skills, phone, portfolio_link, linkedin } = req.body;

    // CV file update
    const cv_path = req.file ? req.file.filename : undefined;

    let query = `UPDATE students SET full_name=?, university=?, major=?, year_of_study=?, skills=?, phone=?, portfolio_link=?, linkedin=?`;
    const params = [full_name, university, major, year_of_study, skills, phone, portfolio_link, linkedin];

    if (cv_path) {
      query += ', cv_path=?';
      params.push(cv_path);
    }

    query += ' WHERE id=?';
    params.push(req.user.id);

    await db.query(query, params);

    res.json({ message: 'Profile updated successfully' });
  } catch (err) {
    console.error('Update student profile error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get new notifications (submissions evaluated since last check)
exports.getNotifications = async (req, res) => {
  try {
    const studentId = req.user.id;
    const { since } = req.query; // ISO timestamp from client

    let whereTime = '';
    const params = [studentId];

    if (since) {
      whereTime = ' AND s.evaluated_at > ?';
      params.push(since);
    }

    const [notifications] = await db.query(
      `SELECT s.id, s.score, s.feedback, s.status, s.evaluated_at,
              t.title as task_title, c.company_name
       FROM submissions s
       JOIN tasks t ON s.task_id = t.id
       JOIN companies c ON t.company_id = c.id
       WHERE s.student_id = ? AND s.status != 'pending' AND s.evaluated_at IS NOT NULL${whereTime}
       ORDER BY s.evaluated_at DESC
       LIMIT 20`,
      params
    );

    res.json(notifications);
  } catch (err) {
    console.error('Get notifications error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get student dashboard stats
exports.getDashboard = async (req, res) => {
  try {
    const studentId = req.user.id;

    const [student] = await db.query(
      'SELECT total_submissions, interested_count FROM students WHERE id = ?',
      [studentId]
    );

    const [pending] = await db.query(
      'SELECT COUNT(*) as count FROM submissions WHERE student_id = ? AND status = "pending"',
      [studentId]
    );

    const [recent] = await db.query(
      `SELECT s.*, t.title as task_title, c.company_name
       FROM submissions s
       JOIN tasks t ON s.task_id = t.id
       JOIN companies c ON t.company_id = c.id
       WHERE s.student_id = ?
       ORDER BY s.submitted_at DESC
       LIMIT 5`,
      [studentId]
    );

    res.json({
      total_submissions: student[0]?.total_submissions || 0,
      pending_review: pending[0].count,
      interested_count: student[0]?.interested_count || 0,
      recent_submissions: recent
    });
  } catch (err) {
    console.error('Get dashboard error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
