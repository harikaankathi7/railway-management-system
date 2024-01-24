import mysql.connector

class trandetails:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarthi07$",
            database="Railway"
            )
    def insertdetails(self,tid,pid,fare):
        
        self.cur=self.con.cursor()
        self.cur.execute(f"insert into transactions values({tid},{pid},{fare})")
        self.con.commit()
        print("data has been inserted successfully..")
    