class serializer:
    @staticmethod
    def serialize_user(user):
        return {
            "id": user.user_id,
            "name": user.username,
            "email": user.email,
            "password": user.password,
            "created_at": user.created_at
        }