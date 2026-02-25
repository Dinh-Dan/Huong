from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import student_controller

student_bp = Blueprint('student', __name__)

@student_bp.route('/profile', methods=['GET'])
@authenticate_token
@require_role('student')
def get_profile():
    return student_controller.get_profile()

@student_bp.route('/profile', methods=['PUT'])
@authenticate_token
@require_role('student')
def update_profile():
    return student_controller.update_profile()

@student_bp.route('/dashboard', methods=['GET'])
@authenticate_token
@require_role('student')
def get_dashboard():
    return student_controller.get_dashboard()
