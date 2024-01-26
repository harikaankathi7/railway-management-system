import mysql.connector

class tdetails:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarthi07$",
            database="Railway"
            )
    
    def insertdetails(self,tno,src,des,tname):
        self.cur=self.con.cursor()
        self.cur.execute(f"insert into train_details values({tno},'{src}','{des}','{tname}')")
        self.con.commit()
        print("data has been inserted successfully..")
    
    def traindetails(self):
        self.cur=self.con.cursor()
        self.cur.execute(f"select train_details.train_no,train_name,source,stop1,stop2,stop3,stop4,destination from train_details inner join routes on train_details.train_no=routes.train_no")
        return self.cur.fetchall()

    def cgetdetails(self):
        self.cur=self.con.cursor()
        self.cur.execute(f"select train_details.train_no from train_details where train_no not in(select train_no from train_capacity)")
        return self.cur.fetchall()

    def rgetdetails(self):
        self.cur=self.con.cursor()
        self.cur.execute(f"select train_details.train_no,source,destination from train_details where train_no not in(select train_no from routes)")
        return self.cur.fetchall()

    def station_names(self,*x):
        for i in x:
            try:
                self.cur=self.con.cursor()
                self.cur.execute(f"insert into station_names values('{i}')")
                self.con.commit()
            except:
                pass
    
    def distinct_stations(self):
        self.cur=self.con.cursor()
        self.cur.execute(f"select names from station_names")
        return self.cur.fetchall()
    def delete(self,trainno):
        self.cur=self.con.cursor()
        self.cur.execute(f"delete from train_details where train_no={trainno}")
        self.con.commit()
        print(f"Train details of tarinno {trainno} has been deleted from train_details table")

        


