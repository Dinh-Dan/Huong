const db = require('../database/db');

// Submit work
exports.submitWork = async (req, res) => {
  try {
    const taskId = req.params.taskId;
    const studentId = req.user.id;

    // Check task exists and active
    const [task] = await db.query('SELECT * FROM tasks WHERE id = ? AND status = "active"', [taskId]);
    if (task.length === 0) {
      return res.status(404).json({ message: 'Task not found or closed' });
    }

    // Check deadline
    if (new Date(task[0].deadline) < new Date()) {
      return res.status(400).json({ message: 'Task deadline has passed' });
    }

    // Check max submissions
    if (task[0].current_submissions >= task[0].max_submissions) {
      return res.status(400).json({ message: 'Maximum submissions reached for this task' });
    }

    // Check duplicate submission
    const [existing] = await db.query(
      'SELECT id FROM submissions WHERE task_id = ? AND student_id = ?',
      [taskId, studentId]
    );
    if (existing.length > 0) {
      return res.status(400).json({ message: 'You have already submitted for this task' });
    }

    const { text_answer, portfolio_link } = req.body;
    const file_path = req.file ? req.file.filename : null;

    const [result] = await db.query(
      `INSERT INTO submissions (task_id, student_id, file_path, text_answer, portfolio_link)
       VALUES (?, ?, ?, ?, ?)`,
      [taskId, studentId, file_path, text_answer, portfolio_link]
    );

    // Increment counters
    await db.query('UPDATE tasks SET current_submissions = current_submissions + 1 WHERE id = ?', [taskId]);
    await db.query('UPDATE students SET total_submissions = total_submissions + 1 WHERE id = ?', [studentId]);

    res.status(201).json({ message: 'Submission successful', submissionId: result.insertId });
  } catch (err) {
    console.error('Submit work error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get student's submissions
exports.getMySubmissions = async (req, res) => {
  try {
    const [submissions] = await db.query(
      `SELECT s.*, t.title as task_title, c.company_name
       FROM submissions s
       JOIN tasks t ON s.task_id = t.id
       JOIN companies c ON t.company_id = c.id
       WHERE s.student_id = ?
       ORDER BY s.submitted_at DESC`,
      [req.user.id]
    );

    res.json(submissions);
  } catch (err) {
    console.error('Get my submissions error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get submissions for a task (company)
exports.getTaskSubmissions = async (req, res) => {
  try {
    const taskId = req.params.taskId;

    // Verify company owns the task
    const [task] = await db.query('SELECT id FROM tasks WHERE id = ? AND company_id = ?', [taskId, req.user.id]);
    if (task.length === 0) {
      return res.status(404).json({ message: 'Task not found or access denied' });
    }

    const [submissions] = await db.query(
      `SELECT s.*, st.full_name, st.university, st.email, st.skills, st.portfolio_link as student_portfolio, st.cv_path
       FROM submissions s
       JOIN students st ON s.student_id = st.id
       WHERE s.task_id = ?
       ORDER BY s.submitted_at DESC`,
      [taskId]
    );

    res.json(submissions);
  } catch (err) {
    console.error('Get task submissions error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get all submissions for all tasks of a company
exports.getAllCompanySubmissions = async (req, res) => {
  try {
    const [submissions] = await db.query(
      `SELECT s.*, st.full_name, st.university, st.email, st.skills, st.portfolio_link as student_portfolio, st.cv_path,
              t.title as task_title
       FROM submissions s
       JOIN students st ON s.student_id = st.id
       JOIN tasks t ON s.task_id = t.id
       WHERE t.company_id = ?
       ORDER BY s.submitted_at DESC`,
      [req.user.id]
    );

    res.json(submissions);
  } catch (err) {
    console.error('Get all company submissions error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};

// Get single submission detail
exports.getSubmission = async (req, res) => {
  try {
    const [submissions] = await db.query(
      `SELECT s.*, st.full_name, st.university, st.email, st.skills, st.portfolio_link as student_portfolio, st.cv_path, st.phone,
              t.title as task_title, t.description as task_description
       FROM submissions s
       JOIN students st ON s.student_id = st.id
       JOIN tasks t ON s.task_id = t.id
       WHERE s.id = ?`,
      [req.params.id]
    );

    if (submissions.length === 0) {
      return res.status(404).json({ message: 'Submission not found' });
    }

    res.json(submissions[0]);
  } catch (err) {
    console.error('Get submission error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
