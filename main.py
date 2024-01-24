# importing required libraries
import pandas as pd
from traindetails import tdetails
from traincapacity import tcdetails
from routes import rdetails
from passenger import pdetails
from transaction import trandetails
from bookticket import bkdetails

print("***************Welcome to Railway Management System***************")
print("\n")
print("----To insert the data enter 1----")
print("----To read the data enter 2------")
print("----To book a ticket 3----")
# delete,update need to be done
print("----To delete the data enter 4----")
print("----To update the data enter 5----")

opr=int(input("Please enter the operation you want to perform:"))

if opr==1:
    print("----To insert the data in traindetails enter 1----")
    print("----To insert the data in traincapacity enter 2---")
    print("----To insert the data in routes enter 3----------")
    insert_opr=int(input("Please enter the operation you want to perform:"))
    if insert_opr==1:
        obj=tdetails()
        tno=int(input("Please enter Train Number:"))
        src=input("Please enter Source Station:")
        des=input("Please enter Destination Station:")
        tname=input("Please enter Train Name:")
        try:
            obj.insertdetails(tno,src,des,tname)
        except Exception as e:
            print(f"Try again..Error {e}")
        # adding the src,des into distinct station names table
        obj.station_names(src,des)
    if insert_opr==2:
        obj=tcdetails()
        obj1=tdetails()
        list1=obj1.cgetdetails()
        if len(list1)==0:
            print("no trains avaiable to insert the capacity")
        else:
            print("---------------------------")
            print(pd.DataFrame(list1,columns=["Trainno."]))
            print("---------------------------")
            tno=int(input("Please enter Train Number:"))
            ac_1=int(input("Please enter capacity for AC_1:"))
            ac_2=int(input("Please enter capacity for AC_2:"))
            ac_3=int(input("Please enter capacity for AC_3:"))
            sl=int(input("Please enter capacity for Sleeper:"))
            gen=int(input("Please enter capacity for General:"))
            try:
                obj.insertdetails(tno,ac_1,ac_2,ac_3,sl,gen)
            except Exception as e:
                print(f"error inserting the data :{e}")

    if insert_opr==3:
        obj=rdetails()
        obj1=tdetails()
        list1=obj1.rgetdetails()
        if len(list1)==0:
            print("no trains are available to insert the routes")
        else:
            print("---------------------------")
            print(pd.DataFrame(list1,columns=["Trainno","Source","Destination"]))
            print("---------------------------")
            tno=int(input("Please enter Train Number:"))
            s_1=input("Please enter stop_1:")
            s_2=input("Please enter stop_2:")
            s_3=input("Please enter stop_3:")
            s_4=input("Please enter stop_4:")
            try:
                obj.insertdetails(tno,s_1,s_2,s_3,s_4)
            except Exception as e:
                print(f"Error in inserting the data :{e}")
            # insert the stations in a table that contains distict station names for booking
            obj1.station_names(s_1,s_2,s_3,s_4)

if opr==2:
    print("----To read the data in traindetails enter 1----")
    print("----To read the data in traincapacity enter 2---")
    insert_opr=int(input("Please enter the operation you want to perform:"))
    if insert_opr==1:
       obj1=tdetails()
       list1=obj1.traindetails()
       print("---------------------------")
       print(pd.DataFrame(list1,columns=["Trainno","Train Name","source","stop1","stop2","stop3","stop4","destination"]))
       print("---------------------------")
    if insert_opr==2:
        obj1=tcdetails()
        list1=obj1.read_details()
        print("---------------------------")
        print(pd.DataFrame(list1,columns=["Trainno","ac_1","ac_2","ac_3","sleeper","general"]))
        print("---------------------------")
if opr==3:
    obj1=tdetails()
    print("--------------")
    station_names=obj1.distinct_stations()
    print(pd.DataFrame(station_names,columns=["Station Name"]))
    print("--------------")
    source_station=input('Enter source from above Station Names:')
    destination=input('Enter destination from above Station Names:')
    obj=rdetails()
    print("------Available Trains------")
    train_details=obj.getdetails(source_station,destination)
    obj2=tcdetails()
    capacity=obj2.traincapacity(train_details.keys())
    if len(capacity)==0:
        print("No available trains")
    else:
        df=pd.DataFrame(capacity,columns=["Trainno","ac_1","ac_2","ac_3","sl","gen"])
        print("-----------------")
        print(df)
        print("-----------------")
        # taking train no,compartment from user to book a ticket
        train_no=int(input("Enter train no:"))
        while train_no not in list(df['Trainno'].unique()):
            print("please enter trainno from available trains")
            train_no=int(input("Enter train no:"))
        classes=["ac_1","ac_2","ac_3","sl","gen"]
        cls=input("Enter class:")
        while cls not in classes:
            print("please enter class from available classes")
            cls=input("Enter class:")
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        mbno=input("Enter your mobile number:")
        gender=input("Gender:")
        #adding data to passenger table
        obj3=pdetails()
        try:
            pid=obj3.insertdetails(name,age,mbno,gender)
        except Exception as e:
            print(f"Error while inserting the data :{e}")
        # payment (tid generated by payment app,fare to be calcuated)
        num_stations=train_details[train_no][-1]
        # dictionary containing charge for type of class per station
        charges={"ac_1":50,"ac_2":60,"ac_3":70,"sl":40,"gen":20}
        fare=charges[cls]*num_stations
        obj4=trandetails()
        tid=int(input("Enter your Transaction ID:"))
        try:
            obj4.insertdetails(tid,pid,fare)
        except Exception as e:
            print(f"Error while inserting the data :{e}")
        # update seats availability
        try:
            seat_no=obj2.update_traincapacity(train_no,cls)
        except Exception as e:
            print(f"Error :{e}")
        # adding details to booktickets
        obj5=bkdetails()
        try:
            bid=obj5.insertdetails(pid,cls,seat_no,tid,source_station,destination,train_no)
        except Exception as e:
            print(f"Error:{e}")
        # print the booking ticket details
        print("Your ticket is booked successfully")
        print("\n")
        print("******Train Ticket Details******")
        print("BookingID:",bid)
        print("PassengerID:",pid)
        print("TransactionID:",tid)
        print("Class:",cls)
        print("Seatno:",seat_no)
        print("Train_no:",train_no)











