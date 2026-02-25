from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role, require_plan
from controllers import leaderboard_controller

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/task/<int:task_id>', methods=['GET'])
@authenticate_token
@require_role('company')
@require_plan('standard')
def task_leaderboard(task_id):
    return leaderboard_controller.task_leaderboard(task_id)

@leaderboard_bp.route('/global', methods=['GET'])
@authenticate_token
@require_role('company')
@require_plan('premium')
def global_leaderboard():
    return leaderboard_controller.global_leaderboard()

@leaderboard_bp.route('/export-csv', methods=['GET'])
@authenticate_token
@require_role('company')
@require_plan('premium')
def export_csv():
    return leaderboard_controller.export_csv()
