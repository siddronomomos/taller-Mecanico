import mysql.connector

class connection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'taller'
        self.con = None
        self.cursor = None
    
    def open(self):
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.cursor = self.con.cursor()
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        self.con.database = self.database
        return self.cursor
    
    def close(self):
        self.cursor.close()
        self.con.close()
        return True
    
    def commit(self):
        self.con.commit()
        return True
    
    def rollback(self):
        self.con.rollback()
        return True