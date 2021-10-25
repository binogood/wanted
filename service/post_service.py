from model.post_dao   import PostDao
from responses import *


class PostService():
    def __init__(self):
        pass


    def create_post_service(self, create_post_info, con):
        post_dao = PostDao()

        post_id = post_dao.create_post_dao(create_post_info, con)
        return post_id


    def delete_post_service(self, delete_post_info, con):
        post_dao = PostDao()

        post_id = post_dao.find_post_dao(delete_post_info, con)
        if not post_id:
            raise ApiException(400, NOT_THE_AUTHOR)

        post_dao.delete_post_dao(delete_post_info, con)
        return True


    def update_post_service(self, update_post_info, con):
        post_dao = PostDao()

        post_id = post_dao.find_post_dao(update_post_info, con)
        if not post_id:
            raise ApiException(400, NOT_THE_AUTHOR)

        post_dao.update_post_dao(update_post_info, con)
        return True


    def list_post_service(self, list_post_info, con):
        post_dao = PostDao()
        post_list = post_dao.list_post_dao(list_post_info, con)
        return post_list


    def detail_post_service(self, detail_info, con):
        post_dao = PostDao()

        post_detail_id = post_dao.find_detail_post_dao(detail_info, con)
        if not post_detail_id:
            raise ApiException(400, POST_NOT_FOUND)

        post_detail = post_dao.detail_post_dao(detail_info, con)
        return post_detail