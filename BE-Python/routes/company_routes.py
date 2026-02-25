from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import company_controller

company_bp = Blueprint('company', __name__)

@company_bp.route('/profile', methods=['GET'])
@authenticate_token
@require_role('company')
def get_profile():
    return company_controller.get_profile()

@company_bp.route('/profile', methods=['PUT'])
@authenticate_token
@require_role('company')
def update_profile():
    return company_controller.update_profile()

@company_bp.route('/dashboard', methods=['GET'])
@authenticate_token
@require_role('company')
def get_dashboard():
    return company_controller.get_dashboard()
