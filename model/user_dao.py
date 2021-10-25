import sqlite3

class UserDao():
    def __init__(self):
        pass


    def find_user_dao(self, user_info, con):
        cur = con.cursor()
        cur.execute("SELECT id, username, password FROM users WHERE username=(?)",\
                    (user_info['username'],))
        return cur.fetchone()


    def create_user_dao(self, user_info, con):
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, password, create_at) VALUES(?,?,datetime('now','localtime'))",\
                    (user_info['username'],user_info['password']))
        return cur.lastrowid


    def user_identifier_dao(self, user_info, con):
        cur = con.cursor()
        cur.execute("SELECT id FROM users WHERE id=(?)",(user_info['user_id'],))
        return cur.fetchone()
