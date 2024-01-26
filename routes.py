import mysql.connector

class rdetails:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarthi07$",
            database="Railway")
    def insertdetails(self,tno,s_1,s_2,s_3,s_4):
        self.cur=self.con.cursor()
        self.cur.execute(f"insert into routes values({tno},'{s_1}','{s_2}','{s_3}','{s_4}')")
        self.con.commit()
        print("data has been inserted succes sfully..")
    def getdetails(self,source,destination):
        self.cur=self.con.cursor()
        self.cur.execute(f"select train_details.train_no,train_name,source,stop1,stop2,stop3,stop4,destination from train_details inner join routes on train_details.train_no=routes.train_no where source='{source}' or stop1='{source}' or stop2='{source}' or stop3='{source}' or stop4='{source}'")
        train_details=self.cur.fetchall()
        train_no={}
        for i in train_details:
            stop=i.index(source)
            routes=i[stop+1:]
            if destination in routes:
                train_no[i[0]]=[i[1],i.index(destination)-stop]
        return train_no
    def delete(self,trainno):
        self.cur=self.con.cursor()
        self.cur.execute(f"delete from routes where train_no={trainno}")
        self.con.commit()
        print(f"Train details of trainno {trainno} has been deleted from routes table")
    def update(self,trainno,col,val):
        self.cur=self.con.cursor()
        self.cur.execute(f"set sql_safe_updates=0")
        self.con.commit()
        self.cur=self.con.cursor()
        self.cur.execute(f"update routes set"+col+f"='{val}' where train_no={trainno}")
        self.con.commit()
        print("updated values successfully....")
