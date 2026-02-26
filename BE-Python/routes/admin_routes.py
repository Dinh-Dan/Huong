from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import admin_controller

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/login', methods=['POST'])
def admin_login():
    return admin_controller.admin_login()


@admin_bp.route('/create', methods=['POST'])
def create_admin():
    return admin_controller.create_admin()


@admin_bp.route('/dashboard', methods=['GET'])
@authenticate_token
@require_role('admin')
def get_dashboard_stats():
    return admin_controller.get_dashboard_stats()


@admin_bp.route('/companies', methods=['GET'])
@authenticate_token
@require_role('admin')
def get_all_companies():
    return admin_controller.get_all_companies()


@admin_bp.route('/students', methods=['GET'])
@authenticate_token
@require_role('admin')
def get_all_students():
    return admin_controller.get_all_students()


@admin_bp.route('/companies/<int:company_id>', methods=['DELETE'])
@authenticate_token
@require_role('admin')
def delete_company(company_id):
    return admin_controller.delete_company(company_id)


@admin_bp.route('/students/<int:student_id>', methods=['DELETE'])
@authenticate_token
@require_role('admin')
def delete_student(student_id):
    return admin_controller.delete_student(student_id)


@admin_bp.route('/upgrade-requests', methods=['GET'])
@authenticate_token
@require_role('admin')
def get_upgrade_requests():
    return admin_controller.get_upgrade_requests()


@admin_bp.route('/upgrade-requests/<int:request_id>', methods=['PUT'])
@authenticate_token
@require_role('admin')
def process_upgrade_request(request_id):
    return admin_controller.process_upgrade_request(request_id)
