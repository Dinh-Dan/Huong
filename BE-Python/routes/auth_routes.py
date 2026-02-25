from flask import Blueprint
from middleware.auth import authenticate_token
from controllers import auth_controller

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register/student', methods=['POST'])(auth_controller.register_student)
auth_bp.route('/register/company', methods=['POST'])(auth_controller.register_company)
auth_bp.route('/login', methods=['POST'])(auth_controller.login)
auth_bp.route('/me', methods=['GET'])(authenticate_token(auth_controller.get_me))
auth_bp.route('/check-email', methods=['GET'])(auth_controller.check_email)
