const express = require('express');
const router = express.Router();
const leaderboardController = require('../controllers/leaderboard.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole, requirePlan } = require('../middleware/role');

router.get('/task/:taskId',
  authenticateToken,
  requireRole('company'),
  requirePlan('standard'),
  leaderboardController.taskLeaderboard
);

router.get('/global',
  authenticateToken,
  requireRole('company'),
  requirePlan('premium'),
  leaderboardController.globalLeaderboard
);

router.get('/export-csv',
  authenticateToken,
  requireRole('company'),
  requirePlan('premium'),
  leaderboardController.exportCSV
);

module.exports = router;
