import mysql.connector

class pdetails:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarthi07$",
            database="Railway"
            )
    def insertdetails(self,pname,age,mn,gen):
        #generating passenger id
        self.cur=self.con.cursor()
        self.cur.execute(f"select p_id from passengers order by p_id desc limit 1")
        pid=self.cur.fetchall()
        if len(pid)==0:
            pid=100000
        else:
            pid=pid[0][0]+1
        #inserting passenger details
        self.cur=self.con.cursor()
        self.cur.execute(f"insert into passengers values({pid},'{pname}',{age},'{mn}','{gen}')")
        self.con.commit()
        print("data has been inserted successfully..")
        return pid