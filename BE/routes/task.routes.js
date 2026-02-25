const express = require('express');
const router = express.Router();
const { body } = require('express-validator');
const taskController = require('../controllers/task.controller');
const { authenticateToken } = require('../middleware/auth');
const { requireRole } = require('../middleware/role');

// Public routes
router.get('/', taskController.browseTasks);
router.get('/company/mine', authenticateToken, requireRole('company'), taskController.getMyTasks);
router.get('/:id', taskController.getTask);

// Company-only routes
router.post('/',
  authenticateToken,
  requireRole('company'),
  [
    body('title').notEmpty().withMessage('Title is required'),
    body('description').notEmpty().withMessage('Description is required'),
    body('deadline').notEmpty().withMessage('Deadline is required'),
    body('difficulty').isIn(['easy', 'medium', 'hard']).withMessage('Invalid difficulty')
  ],
  taskController.createTask
);

router.put('/:id', authenticateToken, requireRole('company'), taskController.updateTask);
router.delete('/:id', authenticateToken, requireRole('company'), taskController.deleteTask);

module.exports = router;
