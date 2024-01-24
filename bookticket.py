import mysql.connector

class bkdetails:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarthi07$",
            database="Railway"
            )
    def insertdetails(self,pid,Class,seatno,tid,src,des,tno):
        #generating booking id
        self.cur=self.con.cursor()
        self.cur.execute(f"select booking_id from book_tickets order by booking_id desc limit 1")
        bid=self.cur.fetchall()
        if len(bid)==0:
            bid=100000
        else:
            bid=bid[0][0]+1
        #adding ddtails to table                                    
        self.cur=self.con.cursor()
        self.cur.execute(f"insert into book_tickets values({bid},{pid},'{Class}',{seatno},{tid},'{src}','{des}',{tno})")
        self.con.commit()
        print("data has been inserted successfully..")
        return bid