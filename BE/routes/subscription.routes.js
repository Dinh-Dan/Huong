const express = require('express');
const router = express.Router();
const subscriptionController = require('../controllers/subscription.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole } = require('../middleware/role');

router.get('/plans', subscriptionController.getPlans);
router.get('/current', authenticateToken, requireRole('company'), subscriptionController.getCurrentPlan);
router.put('/upgrade', authenticateToken, requireRole('company'), subscriptionController.upgradePlan);

module.exports = router;
