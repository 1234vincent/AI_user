import AI_user.repositories.repository as user_repository
from AI_user.serialize.serializeuser import serializer

repo = user_repository.User_Repository()
serialize = serializer()
class PracticeService:
    def get_all_users(self):
        user =  repo.get_user_repo()
        return serialize.serialize_user(user)
    