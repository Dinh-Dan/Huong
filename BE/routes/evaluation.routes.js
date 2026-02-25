const express = require('express');
const router = express.Router();
const evaluationController = require('../controllers/evaluation.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole } = require('../middleware/role');

router.put('/:submissionId', authenticateToken, requireRole('company'), evaluationController.evaluateSubmission);

module.exports = router;
