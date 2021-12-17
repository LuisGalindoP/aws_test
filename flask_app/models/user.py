from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import app



class User:
    db_name = "aws_test"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        result = MySQLConnection(cls.db_name).query_db(query)
        all_users = []
        for row in result:
            this_user = cls(row)
            all_users.append(this_user)
        return all_users


