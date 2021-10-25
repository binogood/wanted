import sqlite3
from datetime import datetime

class PostDao():
    def __init__(self):
        pass

    def find_post_dao(self, post_info, con):
        cur = con.cursor()
        cur.execute("SELECT user_id FROM posts WHERE id=(?) AND user_id=(?)",\
                    (post_info['post_id'],post_info['user_id']))
        return cur.fetchone()


    def find_detail_post_dao(self, post_info, con):
        cur = con.cursor()
        cur.execute("SELECT id FROM posts WHERE id=(?)", (post_info['post_id'],))
        return cur.fetchone()


    def create_post_dao(self, create_post_info, con):
        cur = con.cursor()
        cur.execute("INSERT INTO posts (title, contents, user_id, create_at, update_at)\
                    VALUES(?,?,?,datetime('now','localtime'),datetime('now','localtime'))",\
                    (create_post_info['title'],create_post_info['contents'],create_post_info['user_id']))
        return cur.lastrowid


    def delete_post_dao(self, delete_post_info, con):
        cur = con.cursor()
        cur.execute("DELETE FROM posts WHERE id=(?)",(delete_post_info['post_id'],))
        return cur.lastrowid


    def update_post_dao(self, update_post_info, con):
        cur = con.cursor()
        temp = {}
        query = """
            UPDATE posts SET
        """

        if 'title' in update_post_info:
            if 'contents' in update_post_info:
                query += """
                    title = :title,
                """
            else:
                query += """
                    title = :title
                """
            temp['title'] = update_post_info['title']
        if 'contents' in update_post_info:
            query += """
                contents = :contents
            """
            temp['contents'] = update_post_info['contents']
        
        query += """
                ,update_at = :update_at
            WHERE user_id = :user_id and id = :post_id
        """
        temp['update_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temp['user_id'] = update_post_info['user_id']
        temp['post_id'] = update_post_info['post_id']

        cur.execute(query, temp)
        return cur.lastrowid


    def list_post_dao(self, list_post_info, con):
        cur = con.cursor()
        cur.execute("SELECT p.title, u.username, p.update_at FROM posts AS p \
                    INNER JOIN users AS u ON p.user_id = u.id LIMIT (?) OFFSET (?)",\
                    (list_post_info['limit'], list_post_info['offset']))
        return cur.fetchall()


    def detail_post_dao(self, detail_info, con):
        cur = con.cursor()
        cur.execute("SELECT p.title, p.contents, u.username, p.create_at FROM posts AS p \
                    INNER JOIN users AS u ON p.user_id = u.id WHERE p.id = (?)",(detail_info['post_id'],))
        return cur.fetchone()