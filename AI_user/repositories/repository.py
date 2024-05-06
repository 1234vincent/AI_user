from AI_user.models.model import User
class User_Repository:
   def get_user_repo(self):
       all_users = User.query.first()
       if all_users is None:
           return []
       return all_users
 