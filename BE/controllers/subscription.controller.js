const db = require('../database/db');

// Get all plans
exports.getPlans = async (req, res) => {
  try {
    const [plans] = await db.query('SELECT * FROM subscription_plans ORDER BY id');
    res.json(plans);
  } catch (err) {
    console.error('Get plans error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get current subscription
exports.getCurrentPlan = async (req, res) => {
  try {
    const [company] = await db.query(
      'SELECT subscription_plan, task_limit, tasks_used, subscription_expiry FROM companies WHERE id = ?',
      [req.user.id]
    );

    if (company.length === 0) {
      return res.status(404).json({ message: 'Company not found' });
    }

    const [planDetails] = await db.query(
      'SELECT * FROM subscription_plans WHERE plan_name = ?',
      [company[0].subscription_plan]
    );

    res.json({
      ...company[0],
      plan_details: planDetails[0] || null
    });
  } catch (err) {
    console.error('Get current plan error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Upgrade plan
exports.upgradePlan = async (req, res) => {
  try {
    const { plan } = req.body;

    if (!['basic', 'standard', 'premium'].includes(plan)) {
      return res.status(400).json({ message: 'Invalid plan' });
    }

    const [planDetails] = await db.query('SELECT * FROM subscription_plans WHERE plan_name = ?', [plan]);
    if (planDetails.length === 0) {
      return res.status(400).json({ message: 'Plan not found' });
    }

    // Set expiry to 30 days from now
    const expiry = new Date();
    expiry.setDate(expiry.getDate() + 30);

    await db.query(
      `UPDATE companies SET subscription_plan = ?, task_limit = ?, subscription_expiry = ?
       WHERE id = ?`,
      [plan, planDetails[0].task_limit, expiry, req.user.id]
    );

    res.json({ message: `Plan upgraded to ${plan} successfully` });
  } catch (err) {
    console.error('Upgrade plan error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
