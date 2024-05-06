# AI_user/url/url.py
from flask import Blueprint, jsonify

from AI_user.service.service import PracticeService
user_bp = Blueprint('user', __name__, url_prefix='/users')

service = PracticeService()

@user_bp.route('/', methods=['GET'])
def get_all_users():
     users = service.get_all_users()
     return jsonify(users), 200

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
     user = service.get_user(user_id)
     return jsonify(user), 200

