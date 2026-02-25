from flask import request, jsonify, g
from database.db import query, query_one, execute

def evaluate_submission(submission_id):
    try:
        data = request.get_json()
        score = data.get('score')
        feedback = data.get('feedback')
        status = data.get('status')

        if score is None or not status:
            return jsonify({'message': 'Score and status are required'}), 400

        if score < 0 or score > 100:
            return jsonify({'message': 'Score must be between 0 and 100'}), 400

        if status not in ('reviewed', 'interested', 'rejected'):
            return jsonify({'message': 'Invalid status'}), 400

        # Verify submission belongs to company's task
        submission = query_one(
            '''SELECT s.*, t.company_id, s.student_id
               FROM submissions s
               JOIN tasks t ON s.task_id = t.id
               WHERE s.id = %s AND t.company_id = %s''',
            (submission_id, g.user['id'])
        )

        if not submission:
            return jsonify({'message': 'Submission not found or access denied'}), 404

        prev_status = submission['status']
        student_id = submission['student_id']

        # Update submission
        execute(
            'UPDATE submissions SET score = %s, feedback = %s, status = %s, evaluated_at = NOW() WHERE id = %s',
            (score, feedback, status, submission_id)
        )

        # Recalculate student stats
        score_result = query_one(
            'SELECT AVG(score) as avg_score, SUM(score) as total_score FROM submissions WHERE student_id = %s AND score IS NOT NULL',
            (student_id,)
        )

        avg_score = score_result['avg_score'] or 0
        total_score = score_result['total_score'] or 0

        execute(
            'UPDATE students SET average_score = %s, total_score = %s WHERE id = %s',
            (avg_score, total_score, student_id)
        )

        # Update interested count
        if status == 'interested' and prev_status != 'interested':
            execute('UPDATE students SET interested_count = interested_count + 1 WHERE id = %s', (student_id,))
        elif prev_status == 'interested' and status != 'interested':
            execute('UPDATE students SET interested_count = GREATEST(interested_count - 1, 0) WHERE id = %s', (student_id,))

        return jsonify({'message': 'Submission evaluated successfully'})

    except Exception as e:
        print(f'Evaluate submission error: {e}')
        return jsonify({'message': 'Server error'}), 500
