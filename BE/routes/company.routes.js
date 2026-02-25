const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require('path');
const companyController = require('../controllers/company.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole } = require('../middleware/role');

const companyStorage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, path.join(__dirname, '../uploads/logos')),
  filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
});
const uploadLogo = multer({
  storage: companyStorage,
  limits: { fileSize: 5 * 1024 * 1024 }
});

router.get('/profile', authenticateToken, requireRole('company'), companyController.getProfile);
router.put('/profile', authenticateToken, requireRole('company'), uploadLogo.fields([{ name: 'logo', maxCount: 1 }]), companyController.updateProfile);
router.get('/dashboard', authenticateToken, requireRole('company'), companyController.getDashboard);

module.exports = router;
