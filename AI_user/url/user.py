# AI_user/blueprints/user.py
from flask import Blueprint, jsonify

from AI_user.service.seruser import PracticeService
user_bp = Blueprint('user', __name__, url_prefix='/users')

service = PracticeService()

@user_bp.route('/', methods=['GET'])
def get_all_users():
     users = service.get_all_users()
     return jsonify(users), 200




