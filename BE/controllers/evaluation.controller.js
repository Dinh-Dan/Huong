const db = require('../database/db');

// Evaluate submission (score + feedback + status)
exports.evaluateSubmission = async (req, res) => {
  try {
    const submissionId = req.params.submissionId;
    const { score, feedback, status } = req.body;

    if (score === undefined || !status) {
      return res.status(400).json({ message: 'Score and status are required' });
    }

    if (score < 0 || score > 100) {
      return res.status(400).json({ message: 'Score must be between 0 and 100' });
    }

    if (!['reviewed', 'interested', 'rejected'].includes(status)) {
      return res.status(400).json({ message: 'Invalid status' });
    }

    // Verify the submission belongs to a task owned by this company
    const [submission] = await db.query(
      `SELECT s.*, t.company_id, s.student_id
       FROM submissions s
       JOIN tasks t ON s.task_id = t.id
       WHERE s.id = ? AND t.company_id = ?`,
      [submissionId, req.user.id]
    );

    if (submission.length === 0) {
      return res.status(404).json({ message: 'Submission not found or access denied' });
    }

    const prevStatus = submission[0].status;
    const studentId = submission[0].student_id;

    // Update submission
    await db.query(
      `UPDATE submissions SET score = ?, feedback = ?, status = ?, evaluated_at = NOW()
       WHERE id = ?`,
      [score, feedback, status, submissionId]
    );

    // Update student stats
    // Recalculate average score
    const [scoreResult] = await db.query(
      'SELECT AVG(score) as avg_score, SUM(score) as total_score FROM submissions WHERE student_id = ? AND score IS NOT NULL',
      [studentId]
    );

    const avgScore = scoreResult[0].avg_score || 0;
    const totalScore = scoreResult[0].total_score || 0;

    await db.query(
      'UPDATE students SET average_score = ?, total_score = ? WHERE id = ?',
      [avgScore, totalScore, studentId]
    );

    // Update interested count if status changed to interested
    if (status === 'interested' && prevStatus !== 'interested') {
      await db.query('UPDATE students SET interested_count = interested_count + 1 WHERE id = ?', [studentId]);
    } else if (prevStatus === 'interested' && status !== 'interested') {
      await db.query('UPDATE students SET interested_count = GREATEST(interested_count - 1, 0) WHERE id = ?', [studentId]);
    }

    res.json({ message: 'Submission evaluated successfully' });
  } catch (err) {
    console.error('Evaluate submission error:', err);
    res.status(500).json({ message: 'Server error' });
  }
};
