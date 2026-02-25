const db = require('../database/db');

const requireRole = (...roles) => {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ message: 'Authentication required' });
    }
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ message: 'Access denied. Insufficient permissions.' });
    }
    next();
  };
};

const requirePlan = (...plans) => {
  return async (req, res, next) => {
    if (!req.user || req.user.role !== 'company') {
      return res.status(403).json({ message: 'Company access required' });
    }

    try {
      const [rows] = await db.query(
        'SELECT subscription_plan FROM companies WHERE id = ?',
        [req.user.id]
      );

      if (rows.length === 0) {
        return res.status(404).json({ message: 'Company not found' });
      }

      const planHierarchy = { basic: 1, standard: 2, premium: 3 };
      const companyPlanLevel = planHierarchy[rows[0].subscription_plan] || 0;
      const requiredLevel = Math.min(...plans.map(p => planHierarchy[p] || 0));

      if (companyPlanLevel < requiredLevel) {
        return res.status(403).json({ message: `This feature requires ${plans[0]} plan or higher` });
      }

      req.companyPlan = rows[0].subscription_plan;
      next();
    } catch (err) {
      return res.status(500).json({ message: 'Server error checking subscription' });
    }
  };
};

module.exports = { requireRole, requirePlan };
