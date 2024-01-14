#PNR Status
import os, time 
import mysql.connector as s
con = s.connect(host="localhost",user="root",database="railway_reservation_system",password="TanujKhajanBhatt")
cur = con.cursor()
def STATUS():
    def Detail(a):
        o = a.split(" ")
        o = "".join(o)
        if o.isalpha():
            y , z = "0" , a
        elif o.isdigit():
            y , z = a ,"0"
        else :
            z , y = "0" ,"0"
        cur.execute("select * from Tickets where PNR_No = " + y + " or Passanger_Name = \"" + z + "\"")
        m = cur.fetchall()
        if m == list():
            print("\n\n No such Reservation Found.......\n\n")
        else :
            No, Name, Age, No1, Class, No3= m[0][0],m[0][1],m[0][2],m[0][3],m[0][4],m[0][5]
            print("="*80, "\n \t\t\t\t   PNR STATUS\n",)
            print("="*80)
            print("\nPassanger Name       : ", Name)
            print("PNR Number           : ", No)
            print("Passanger _Age       : ", Age)
            print("Train Number         : ", No1)
            print("Class of Booked Seat : ", Class)
            print("No. of Seats Booked  : ", No3,"\n")
        print("="*80)
    print("="*80,"\n \t\t\t\t   PNR STATUS \n")
    print("="*80)
    a = input("\nEnter PNR No. or Passanger Name : ")
    print("\n\n.......Fetching Details")
    time.sleep(2)
    print("\nProcessing.......")
    time.sleep(3)
    os.system("cls")
    Detail(a)