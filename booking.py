#importing required libraries
from traindetails import tdetails
from traincapacity import tcdetails
from routes import rdetails
from passenger import pdetails
from transaction import trandetails
from bookticket import bkdetails
class book_ticket:
    def bookticket(self):
        obj1=tdetails()
        print("---Station Names---")
        obj1.distinct_stations()
        source_station=input('Enter source from above Station Names:')
        destination=input('Enter destination from above Station Names:')
        obj=rdetails()
        print("--Available Trains--")
        train_details=obj.getdetails(source_station,destination)
        obj2=tcdetails()
        obj2.traincapacity(train_details.keys())
        # taking train no,compartment from user to book a ticket
        train_no=int(input("Enter train no:"))
        cls=input("Enter class:")
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        mbno=int(input("Enter your mobile number:"))
        gender=input("Gender:")
        #adding data to passenger table
        obj3=pdetails
        pid=obj3.insertdetails(name,age,mbno,gender)
        # payment (tid generated by payment app,fare to be calcuated)
        num_stations=train_details[train_no][-1]
        # dictionary containing charge for type of cls per station
        charges={"ac_1":50,"ac_2":60,"ac_3":70,"slr":40,"gen":20}
        fare=charges[cls]*num_stations
        obj4=trandetails()
        tid=int(input("Enter your Transaction ID:"))
        obj4.insertdetails(tid,pid,fare)
        # update seats availability
        seat_no=obj2.update_traincapacity(train_no,cls)
        # adding details to booktickets
        obj5=bkdetails()
        obj5.insertdetails(pid,cls,seat_no,tid,destination)
        








