const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require('path');
const studentController = require('../controllers/student.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole } = require('../middleware/role');

const cvStorage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, path.join(__dirname, '../uploads/cv')),
  filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
});
const uploadCV = multer({
  storage: cvStorage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype === 'application/pdf') cb(null, true);
    else cb(new Error('Only PDF files allowed'), false);
  },
  limits: { fileSize: 5 * 1024 * 1024 }
});

router.get('/profile', authenticateToken, requireRole('student'), studentController.getProfile);
router.put('/profile', authenticateToken, requireRole('student'), uploadCV.single('cv'), studentController.updateProfile);
router.get('/dashboard', authenticateToken, requireRole('student'), studentController.getDashboard);
router.get('/notifications', authenticateToken, requireRole('student'), studentController.getNotifications);

module.exports = router;
