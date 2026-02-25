const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require('path');
const submissionController = require('../controllers/submission.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole } = require('../middleware/role');

// Multer config for submission files
const submissionStorage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, path.join(__dirname, '../uploads/submissions')),
  filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
});
const uploadSubmission = multer({
  storage: submissionStorage,
  fileFilter: (req, file, cb) => {
    const allowed = ['application/pdf', 'application/zip', 'application/x-zip-compressed'];
    if (allowed.includes(file.mimetype)) cb(null, true);
    else cb(new Error('Only PDF and ZIP files allowed'), false);
  },
  limits: { fileSize: 20 * 1024 * 1024 }
});

// Student routes
router.post('/:taskId', authenticateToken, requireRole('student'), uploadSubmission.single('file'), submissionController.submitWork);
router.get('/mine', authenticateToken, requireRole('student'), submissionController.getMySubmissions);

// Company routes
router.get('/company/all', authenticateToken, requireRole('company'), submissionController.getAllCompanySubmissions);
router.get('/task/:taskId', authenticateToken, requireRole('company'), submissionController.getTaskSubmissions);
router.get('/:id', authenticateToken, submissionController.getSubmission);

module.exports = router;
