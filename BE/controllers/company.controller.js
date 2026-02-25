const db = require('../database/db');

// Get company profile
exports.getProfile = async (req, res) => {
  try {
    const [company] = await db.query(
      `SELECT id, company_name, email, industry, company_size, website, address, description,
              logo_path, business_license_path, subscription_plan, task_limit, tasks_used, subscription_expiry, created_at
       FROM companies WHERE id = ?`,
      [req.user.id]
    );

    if (company.length === 0) {
      return res.status(404).json({ message: 'Company not found' });
    }

    res.json(company[0]);
  } catch (err) {
    console.error('Get company profile error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Update company profile
exports.updateProfile = async (req, res) => {
  try {
    const { company_name, industry, company_size, website, address, description } = req.body;

    const files = req.files || {};
    const logo_path = files.logo ? files.logo[0].filename : undefined;

    let query = `UPDATE companies SET company_name=?, industry=?, company_size=?, website=?, address=?, description=?`;
    const params = [company_name, industry, company_size, website, address, description];

    if (logo_path) {
      query += ', logo_path=?';
      params.push(logo_path);
    }

    query += ' WHERE id=?';
    params.push(req.user.id);

    await db.query(query, params);

    res.json({ message: 'Profile updated successfully' });
  } catch (err) {
    console.error('Update company profile error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get company dashboard stats
exports.getDashboard = async (req, res) => {
  try {
    const companyId = req.user.id;

    const [company] = await db.query(
      'SELECT subscription_plan, task_limit, tasks_used FROM companies WHERE id = ?',
      [companyId]
    );

    const [totalTasks] = await db.query(
      'SELECT COUNT(*) as count FROM tasks WHERE company_id = ?',
      [companyId]
    );

    const [totalSubmissions] = await db.query(
      `SELECT COUNT(*) as count FROM submissions s
       JOIN tasks t ON s.task_id = t.id
       WHERE t.company_id = ?`,
      [companyId]
    );

    const [interestedCount] = await db.query(
      `SELECT COUNT(*) as count FROM submissions s
       JOIN tasks t ON s.task_id = t.id
       WHERE t.company_id = ? AND s.status = 'interested'`,
      [companyId]
    );

    const [recentTasks] = await db.query(
      `SELECT t.*, (SELECT COUNT(*) FROM submissions WHERE task_id = t.id) as submission_count
       FROM tasks t WHERE t.company_id = ?
       ORDER BY t.created_at DESC LIMIT 5`,
      [companyId]
    );

    res.json({
      subscription_plan: company[0]?.subscription_plan || 'basic',
      task_limit: company[0]?.task_limit || 2,
      tasks_used: company[0]?.tasks_used || 0,
      total_tasks: totalTasks[0].count,
      total_submissions: totalSubmissions[0].count,
      interested_candidates: interestedCount[0].count,
      recent_tasks: recentTasks
    });
  } catch (err) {
    console.error('Get company dashboard error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
