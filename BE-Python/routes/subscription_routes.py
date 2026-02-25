from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import subscription_controller

subscription_bp = Blueprint('subscription', __name__)

@subscription_bp.route('/plans', methods=['GET'])
def get_plans():
    return subscription_controller.get_plans()

@subscription_bp.route('/current', methods=['GET'])
@authenticate_token
@require_role('company')
def get_current_plan():
    return subscription_controller.get_current_plan()

@subscription_bp.route('/upgrade', methods=['PUT'])
@authenticate_token
@require_role('company')
def upgrade_plan():
    return subscription_controller.upgrade_plan()
