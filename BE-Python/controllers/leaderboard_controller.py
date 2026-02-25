import math
import io
from flask import request, jsonify, g, Response
from database.db import query, query_one

def task_leaderboard(task_id):
    try:
        # Verify company owns the task
        task = query_one('SELECT id FROM tasks WHERE id = %s AND company_id = %s', (task_id, g.user['id']))
        if not task:
            return jsonify({'message': 'Task not found or access denied'}), 404

        sort = request.args.get('sort', 'score')

        order_by = 's.score DESC'
        if sort == 'date':
            order_by = 's.submitted_at ASC'
        elif sort == 'tasks':
            order_by = 'st.total_submissions DESC'

        rankings = query(
            f'''SELECT s.id, st.full_name, st.university, s.score, s.status, s.submitted_at,
                       st.total_submissions, st.average_score
                FROM submissions s
                JOIN students st ON s.student_id = st.id
                WHERE s.task_id = %s AND s.score IS NOT NULL
                ORDER BY {order_by}''',
            (task_id,)
        )

        ranked = [{**r, 'rank': i + 1} for i, r in enumerate(rankings)]
        return jsonify(ranked)

    except Exception as e:
        print(f'Task leaderboard error: {e}')
        return jsonify({'message': 'Server error'}), 500

def global_leaderboard():
    try:
        university = request.args.get('university')
        skill = request.args.get('skill')
        year_of_study = request.args.get('year_of_study')
        score_min = request.args.get('score_min')
        score_max = request.args.get('score_max')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 50))
        offset = (page - 1) * limit

        where = 'WHERE st.total_submissions > 0'
        params = []

        if university:
            where += ' AND st.university LIKE %s'
            params.append(f'%{university}%')
        if year_of_study:
            where += ' AND st.year_of_study = %s'
            params.append(year_of_study)
        if skill:
            where += ' AND st.skills LIKE %s'
            params.append(f'%{skill}%')
        if score_min:
            where += ' AND st.average_score >= %s'
            params.append(float(score_min))
        if score_max:
            where += ' AND st.average_score <= %s'
            params.append(float(score_max))

        students = query(
            f'''SELECT st.id, st.full_name, st.university, st.major, st.skills, st.year_of_study,
                       st.average_score, st.total_submissions, st.interested_count
                FROM students st
                {where}
                ORDER BY st.average_score DESC, st.interested_count DESC
                LIMIT %s OFFSET %s''',
            params + [limit, offset]
        )

        ranked = [{**s, 'rank': offset + i + 1} for i, s in enumerate(students)]

        count_result = query_one(f'SELECT COUNT(*) as total FROM students st {where}', params)
        total = count_result['total']

        return jsonify({
            'students': ranked,
            'pagination': {
                'total': total,
                'page': page,
                'limit': limit,
                'totalPages': math.ceil(total / limit) if limit else 0
            }
        })

    except Exception as e:
        print(f'Global leaderboard error: {e}')
        return jsonify({'message': 'Server error'}), 500

def export_csv():
    try:
        university = request.args.get('university')
        skill = request.args.get('skill')

        where = 'WHERE st.total_submissions > 0'
        params = []

        if university:
            where += ' AND st.university LIKE %s'
            params.append(f'%{university}%')
        if skill:
            where += ' AND st.skills LIKE %s'
            params.append(f'%{skill}%')

        students = query(
            f'''SELECT st.full_name, st.email, st.university, st.major, st.skills, st.year_of_study,
                       st.average_score, st.total_submissions, st.interested_count, st.phone, st.portfolio_link, st.linkedin
                FROM students st
                {where}
                ORDER BY st.average_score DESC''',
            params
        )

        headers = 'Name,Email,University,Major,Skills,Year,Avg Score,Submissions,Accepted,Phone,Portfolio,LinkedIn\n'
        rows = []
        for s in students:
            row = f'"{s["full_name"]}","{s["email"]}","{s.get("university") or ""}","{s.get("major") or ""}","{s.get("skills") or ""}",{s.get("year_of_study") or ""},"{s["average_score"]}",{s["total_submissions"]},{s["interested_count"]},"{s.get("phone") or ""}","{s.get("portfolio_link") or ""}","{s.get("linkedin") or ""}"'
            rows.append(row)

        csv_content = headers + '\n'.join(rows)

        return Response(
            csv_content,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=skillrank-candidates.csv'}
        )

    except Exception as e:
        print(f'Export CSV error: {e}')
        return jsonify({'message': 'Server error'}), 500
