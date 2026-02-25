from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import submission_controller

submission_bp = Blueprint('submissions', __name__)

@submission_bp.route('/<int:task_id>', methods=['POST'])
@authenticate_token
@require_role('student')
def submit_work(task_id):
    return submission_controller.submit_work(task_id)

@submission_bp.route('/mine', methods=['GET'])
@authenticate_token
@require_role('student')
def get_my_submissions():
    return submission_controller.get_my_submissions()

@submission_bp.route('/company/all', methods=['GET'])
@authenticate_token
@require_role('company')
def get_all_company_submissions():
    return submission_controller.get_all_company_submissions()

@submission_bp.route('/task/<int:task_id>', methods=['GET'])
@authenticate_token
@require_role('company')
def get_task_submissions(task_id):
    return submission_controller.get_task_submissions(task_id)

@submission_bp.route('/<int:id>', methods=['GET'])
@authenticate_token
def get_submission(id):
    return submission_controller.get_submission(id)
