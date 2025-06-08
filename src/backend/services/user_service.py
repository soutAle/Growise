from backend.models.user import User
from backend.utils.validators import validate_user_data


def get_all_users():
    users = User.query.all()
    return [user.serialize() for user in users] if users else None

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    msg_error = validate_user_data(user)
    if msg_error:
        return msg_error
    return user.serialize() if user else None




