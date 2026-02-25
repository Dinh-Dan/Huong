from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import evaluation_controller

evaluation_bp = Blueprint('evaluation', __name__)

@evaluation_bp.route('/<int:submission_id>', methods=['PUT'])
@authenticate_token
@require_role('company')
def evaluate_submission(submission_id):
    return evaluation_controller.evaluate_submission(submission_id)
