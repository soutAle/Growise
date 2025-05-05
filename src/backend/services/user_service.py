from backend.models.user import User


def get_all_users():
    users = User.query.all()
    return [user.serialize() for user in users] if users else None

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user.serialize() if user else None




