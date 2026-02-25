const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require('path');
const { body } = require('express-validator');
const authController = require('../controllers/auth.controller');
const { authenticateToken } = require('../middleware/auth');

// Multer config for CV uploads
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

// Multer config for company files
const companyStorage = multer.diskStorage({
  destination: (req, file, cb) => {
    const dest = file.fieldname === 'logo'
      ? path.join(__dirname, '../uploads/logos')
      : path.join(__dirname, '../uploads/licenses');
    cb(null, dest);
  },
  filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
});
const uploadCompany = multer({
  storage: companyStorage,
  limits: { fileSize: 10 * 1024 * 1024 }
});

// Routes
router.post('/register/student',
  uploadCV.single('cv'),
  [
    body('full_name').notEmpty().withMessage('Full name is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters'),
    body('university').notEmpty().withMessage('University is required'),
    body('major').notEmpty().withMessage('Major is required'),
    body('phone').notEmpty().withMessage('Phone is required')
  ],
  authController.registerStudent
);

router.post('/register/company',
  uploadCompany.fields([
    { name: 'business_license', maxCount: 1 },
    { name: 'logo', maxCount: 1 }
  ]),
  [
    body('company_name').notEmpty().withMessage('Company name is required'),
    body('registration_number').notEmpty().withMessage('Registration number is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters'),
    body('industry').notEmpty().withMessage('Industry is required')
  ],
  authController.registerCompany
);

router.post('/login', authController.login);
router.get('/me', authenticateToken, authController.getMe);
router.get('/check-email', authController.checkEmail);

module.exports = router;
