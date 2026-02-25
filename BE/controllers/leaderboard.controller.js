const db = require('../database/db');

// Task leaderboard (Standard+)
exports.taskLeaderboard = async (req, res) => {
  try {
    const taskId = req.params.taskId;

    // Verify company owns the task
    const [task] = await db.query('SELECT id FROM tasks WHERE id = ? AND company_id = ?', [taskId, req.user.id]);
    if (task.length === 0) {
      return res.status(404).json({ message: 'Task not found or access denied' });
    }

    const { sort = 'score' } = req.query;

    let orderBy = 's.score DESC';
    if (sort === 'date') orderBy = 's.submitted_at ASC';
    if (sort === 'tasks') orderBy = 'st.total_submissions DESC';

    const [rankings] = await db.query(
      `SELECT s.id, st.full_name, st.university, s.score, s.status, s.submitted_at,
              st.total_submissions, st.average_score
       FROM submissions s
       JOIN students st ON s.student_id = st.id
       WHERE s.task_id = ? AND s.score IS NOT NULL
       ORDER BY ${orderBy}`,
      [taskId]
    );

    // Add rank
    const ranked = rankings.map((r, i) => ({ ...r, rank: i + 1 }));

    res.json(ranked);
  } catch (err) {
    console.error('Task leaderboard error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Global leaderboard (Premium)
exports.globalLeaderboard = async (req, res) => {
  try {
    const { industry, skill, university, score_min, score_max, year_of_study, page = 1, limit = 50 } = req.query;
    const offset = (page - 1) * limit;

    let where = 'WHERE st.total_submissions > 0';
    const params = [];

    if (university) {
      where += ' AND st.university LIKE ?';
      params.push(`%${university}%`);
    }
    if (year_of_study) {
      where += ' AND st.year_of_study = ?';
      params.push(year_of_study);
    }
    if (skill) {
      where += ' AND st.skills LIKE ?';
      params.push(`%${skill}%`);
    }
    if (score_min) {
      where += ' AND st.average_score >= ?';
      params.push(parseFloat(score_min));
    }
    if (score_max) {
      where += ' AND st.average_score <= ?';
      params.push(parseFloat(score_max));
    }

    const [students] = await db.query(
      `SELECT st.id, st.full_name, st.university, st.major, st.skills, st.year_of_study,
              st.average_score, st.total_submissions, st.interested_count
       FROM students st
       ${where}
       ORDER BY st.average_score DESC, st.interested_count DESC
       LIMIT ? OFFSET ?`,
      [...params, parseInt(limit), parseInt(offset)]
    );

    const ranked = students.map((s, i) => ({ ...s, rank: offset + i + 1 }));

    // Get total count
    const [countResult] = await db.query(
      `SELECT COUNT(*) as total FROM students st ${where}`, params
    );

    res.json({
      students: ranked,
      pagination: {
        total: countResult[0].total,
        page: parseInt(page),
        limit: parseInt(limit),
        totalPages: Math.ceil(countResult[0].total / limit)
      }
    });
  } catch (err) {
    console.error('Global leaderboard error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Export CSV (Premium)
exports.exportCSV = async (req, res) => {
  try {
    const { industry, skill, university } = req.query;

    let where = 'WHERE st.total_submissions > 0';
    const params = [];

    if (university) {
      where += ' AND st.university LIKE ?';
      params.push(`%${university}%`);
    }
    if (skill) {
      where += ' AND st.skills LIKE ?';
      params.push(`%${skill}%`);
    }

    const [students] = await db.query(
      `SELECT st.full_name, st.email, st.university, st.major, st.skills, st.year_of_study,
              st.average_score, st.total_submissions, st.interested_count, st.phone, st.portfolio_link, st.linkedin
       FROM students st
       ${where}
       ORDER BY st.average_score DESC`,
      params
    );

    // Build CSV
    const headers = 'Name,Email,University,Major,Skills,Year,Avg Score,Submissions,Accepted,Phone,Portfolio,LinkedIn\n';
    const rows = students.map(s =>
      `"${s.full_name}","${s.email}","${s.university || ''}","${s.major || ''}","${s.skills || ''}",${s.year_of_study || ''},"${s.average_score}",${s.total_submissions},${s.interested_count},"${s.phone || ''}","${s.portfolio_link || ''}","${s.linkedin || ''}"`
    ).join('\n');

    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', 'attachment; filename=skillrank-candidates.csv');
    res.send(headers + rows);
  } catch (err) {
    console.error('Export CSV error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
