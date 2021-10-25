import bcrypt
import jwt

from flask            import jsonify
from config           import SECRET_KEY, ALGORITHM
from model.user_dao   import UserDao

from responses import *

class UserService():
    def __init__(self):
        pass

    def create_user_service(self, create_user_info, con):
        user_dao = UserDao()

        is_existing_username = user_dao.find_user_dao(create_user_info, con)
        if is_existing_username:
            raise ApiException(400, EXISTING_USERNAME)
        
        bcrypt_password = bcrypt.hashpw(create_user_info['password'].encode('utf-8'),bcrypt.gensalt())
        create_user_info['password'] = bcrypt_password
        user_id = user_dao.create_user_dao(create_user_info, con)

        return user_id

    def login_user_service(self, login_user_info, con):

        user_dao = UserDao()
        user = user_dao.find_user_dao(login_user_info, con)
        if user:
            if bcrypt.checkpw(login_user_info['password'].encode('utf-8'), user['password']):
                token = jwt.encode({'user_id': user['id']}, SECRET_KEY, ALGORITHM)
                user_id = user['id']
                return jsonify({'accessToken': token, 'userId': user_id}), 201
            raise ApiException(400, PASSWORD_MISMATCH)
        raise ApiException(400, USER_NOT_FOUND)