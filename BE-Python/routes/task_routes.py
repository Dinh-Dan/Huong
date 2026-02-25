from flask import Blueprint
from middleware.auth import authenticate_token
from middleware.role import require_role
from controllers import task_controller

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['GET'])
def browse_tasks():
    return task_controller.browse_tasks()

@task_bp.route('/company/mine', methods=['GET'])
@authenticate_token
@require_role('company')
def get_my_tasks():
    return task_controller.get_my_tasks()

@task_bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    return task_controller.get_task(id)

@task_bp.route('/', methods=['POST'])
@authenticate_token
@require_role('company')
def create_task():
    return task_controller.create_task()

@task_bp.route('/<int:id>', methods=['PUT'])
@authenticate_token
@require_role('company')
def update_task(id):
    return task_controller.update_task(id)

@task_bp.route('/<int:id>', methods=['DELETE'])
@authenticate_token
@require_role('company')
def delete_task(id):
    return task_controller.delete_task(id)
