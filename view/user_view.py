from flask import request, Blueprint
from responses import *

import re
import sqlite3 as sql

from service.user_service import UserService


# PASSWORD_EXPRESSION = re.compile('^(?=.*[a-z])(?=.*[A-z])(?=.*[0-9])\(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$')

class UserView:
    
    user_app = Blueprint('user_dp', __name__, url_prefix='/user')

    @user_app.route('/create', methods=['POST'])
    def sign_up_user_view():
        data = request.json
        # if not PASSWORD_EXPRESSION.search(data['password']):
        #     raise ApiException(400, INVALID_PASSWORD)
        if 'username' not in data:
            raise ApiException(400, INVALID_INPUT_USERNAME)
        if 'password' not in data:
            raise ApiException(400, INVALID_INPUT_PASSWORD)

        create_user_info = {
            'username' : data['username'],
            'password' : data['password'],
        }

        con = sql.connect('wanted.db')
        con.row_factory = sql.Row

        if con:
            account_service = UserService()
            try:
                account_service.create_user_service(create_user_info, con)
                con.commit()
                return {"message":"USER_CREATED", "result":"POST"}

            except ApiException as e:
                con.rollback()
                raise e

            finally:
                if con:
                    con.close()


    @user_app.route('/login', methods=['POST'])
    def login_user_view():
        con = None
        data = request.json

        if 'username' not in data:
            raise ApiException(400, INVALID_INPUT_USERNAME)
        if 'password' not in data:
            raise ApiException(400, INVALID_INPUT_PASSWORD)

        login_user_info = {
            'username' : data['username'],
            'password' : data['password']
        }

        con = sql.connect('wanted.db')
        con.row_factory = sql.Row

        if con:
            user_service = UserService()
            try:
                login_info = user_service.login_user_service(login_user_info, con)
                return login_info

            except ApiException as e:
                con.rollback()
                raise e

            finally:
                if con:
                    con.close()