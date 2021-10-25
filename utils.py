import jwt

from functools  import wraps
from flask      import request, g

from config         import SECRET_KEY, ALGORITHM
from model.user_dao import UserDao
from responses import *
import sqlite3 as sql



def login_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access_token = request.headers.get('AUTHORIZATION', None)
        try:
            if access_token:
                payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
                user_id = payload['user_id']
                user_info = {'user_id': user_id}
                con = sql.connect('wanted.db')
                con.row_factory = sql.Row
                user_dao = UserDao()
                user = user_dao.user_identifier_dao(user_info, con)
                if not user:
                    raise (400, USER_NOT_FOUND)

                g.token_info = {
                    'user_id': user_id,
                }

                return func(*args, **kwargs)

            else:
                raise ApiException(401, LOGIN_REQUIRED)
        except jwt.InvalidTokenError:
            raise ApiException(400, INVALID_TOKEN)
        except ApiException as e:
            raise e
    
    return wrapper