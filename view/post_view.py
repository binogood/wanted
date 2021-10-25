from flask import request, Blueprint, g
from responses import *
from utils import login_decorator

import sqlite3  as sql

from service.post_service import PostService


class PostView:
    post_app = Blueprint('post_dp', __name__, url_prefix='/post')

    def __init__(self):
        pass

    @post_app.route('create', methods=['POST'])
    @login_decorator
    def create_post_view():
        data = request.json
        user_id = g.token_info['user_id']

        if 'title' not in data:
            raise ApiException(400, INVALID_INPUT_POST_TITLE)
        if 'contents' not in data:
            raise ApiException(400, INVALID_INPUT_POST_CONTENTS)
                
        create_post_info = {
            'title' : data['title'],
            'contents' : data['contents'],
            'user_id' : user_id
        }
        try:
            con = sql.connect('wanted.db')
            con.row_factory = sql.Row
            post_service = PostService()

            post_service.create_post_service(create_post_info, con)
            
            con.commit()
            return {"message": "CREATE_POST", 'resutl':'POST'}
        
        except ApiException as e:
            con.rollback()
            raise e

        finally:
            if con:
                con.close()


    @post_app.route('/delete/<int:post_id>', methods=['DELETE'])
    @login_decorator
    def delete_post_view(post_id):
        # data = request.json
        user_id = g.token_info['user_id']
        delete_post_info = {
            'user_id' : user_id,
            'post_id' : post_id
        }

        try:
            con = sql.connect('wanted.db')
            con.row_factory = sql.Row
            post_service = PostService()

            post_service.delete_post_service(delete_post_info, con)
            con.commit()
            return {"message": "DELETE_POST", "result":"DELETE"}

        except ApiException as e:
            con.rollback()
            raise e

        finally:
            if con:
                con.close()


    @post_app.route('update/<int:post_id>', methods=['PATCH'])
    @login_decorator
    def update_post_view(post_id):
        data = request.json
        user_id = g.token_info['user_id']

        update_post_info = {
            'user_id' : user_id,
            'post_id' : post_id
        }

        if 'title' in data:
            update_post_info['title'] = data['title']

        if 'contents' in data:
            update_post_info['contents'] = data['contents']
        
        try:
            con = sql.connect('wanted.db')
            post_service = PostService()

            post_service.update_post_service(update_post_info, con)
            con.commit()
            return {"message": "UPDATE_POST", "result":"PATCH"}

        except ApiException as e:
            con.rollback()
            raise e

        finally:
            if con:
                con.close()

    @post_app.route('list', methods=["GET"])
    def list_post_view():
        limit = request.args.get('limit', 10)
        offset = request.args.get('offset', 0)

        list_post_info = {  
            'limit' : limit,
            'offset' : offset 
        }

        try:
            con = sql.connect('wanted.db')
            post_service = PostService()
            list_post = post_service.list_post_service(list_post_info, con)

            return {'data':list_post}

        except ApiException as e:
            con.rollback()
            raise e

        finally:
            if con:
                con.close()


    @post_app.route('<int:post_id>', methods=['GET'])
    def detail_post_view(post_id):

        detail_info = {
            'post_id' : post_id
        }

        try:
            con = sql.connect('wanted.db')

            post_service = PostService()
            detail_post = post_service.detail_post_service(detail_info, con)

            return {'data':detail_post}
            # return jsonify(json.dumps(detail_post))

        except ApiException as e:
            con.rollback()
            raise e

        finally:
            if con:
                con.close()