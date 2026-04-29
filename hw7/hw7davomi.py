import pymysql

class Mysql1:
    def __init__(self):
        self.connection()
        self.CreateDB()
    

    def connection(self):
        
        self.db=pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )

        self.c=self.db.cursor()

    def CreateDB(self):
        self.c.execute("""create database if not exists uy_ish_2""")
        self.c.execute("""use uy_ish_2""")



mysql1=Mysql1()