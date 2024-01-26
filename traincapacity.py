import mysql.connector

class tcdetails:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarthi07$",
            database="Railway"
            )
    def insertdetails(self,tno,ac_1,ac_2,ac_3,sl,gen):
        self.cur=self.con.cursor()
        self.cur.execute(f"insert into train_capacity values({tno},{ac_1},{ac_2},{ac_3},{sl},{gen})")
        self.con.commit()
        print("data has been inserted successfully..")
    def read_details(self):
        self.cur=self.con.cursor()
        self.cur.execute(f"select*from train_capacity")
        return self.cur.fetchall()
    def traincapacity(self,train_no):
        list1=[]
        for i in train_no:
            self.cur=self.con.cursor()
            self.cur.execute(f"select * from train_capacity where train_no={i}")
            list1.extend(self.cur.fetchall())
        return list1
    def update_traincapacity(self,train_no,compartment):
        self.cur=self.con.cursor()
        self.cur.execute(f"select "+compartment+f" from train_capacity where train_no={train_no}")
        for i in self.cur.fetchall():
            seatno=i[0]-1
            break
        self.cur=self.con.cursor()
        self.cur.execute(f"set sql_safe_updates=0")
        self.con.commit()
        self.cur=self.con.cursor()
        self.cur.execute(f"update train_capacity set "+compartment+f"={seatno} where train_no={train_no}")
        self.con.commit()
        return seatno
    def delete(self,trainno):
        self.cur=self.con.cursor()
        self.cur.execute(f"delete from train_capacity where train_no={trainno}")
        self.con.commit()
        print(f"Train details of trainno {trainno} has been deleted from train_capacity table")
    def update(self,trainno,col,val):
        self.cur=self.con.cursor()
        self.cur.execute(f"set sql_safe_updates=0")
        self.con.commit()
        self.cur=self.con.cursor()
        self.cur.execute(f"update train_capacity set "+col+f"={val} where train_no={trainno}")
        self.con.commit()
        print(f"Values updated successfully...")


        