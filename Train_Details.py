# Train Details
import os, time 
import mysql.connector as s
con = s.connect(host="localhost",user="root",database="railway_reservation_system",password="TanujKhajanBhatt")
cur = con.cursor()
def DETAIL():
    def Detail(a):
        o = a.split(" ")
        o = "".join(o)
        if o.isalpha():
            y , z = "0" , a
        elif o.isdigit():
            y , z = a ,"0"
        else :
            z , y = "0" ,"0"
        cur.execute("select * from Train where Train_No = " + y + " or Train_Name = \"" + z + "\"")
        m = cur.fetchall()
        if m == list():
            print("\n\n No such Train Found.......\n\n")
        else :
            d = m[0]
            No, Name, Strt, Finish, Fst, Secnd, Trd, Sleeper = d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]
            print("="*80, "\n \t\t\t\tTRAIN DETAILS\n",)
            print("="*80)
            print("\nThe Entered Train Name is  : ", Name)
            print("The Train Number is        : ", No)
            print("Train starts journey from  : ", Strt)
            print("Train's Destination        : ", Finish)
            print("No. of 1st class seats     : ", Fst)
            print("No. of 2nd class seats     : ", Secnd)
            print("No. of 3rd class seats     : ", Trd)
            print("No. of sleeper class seats : ", Sleeper,"\n")
        print("="*80)
    print("="*80,"\n \t\t\t\tTRAIN DETAILS \n")
    print("="*80)
    a = input("\nEnter Train No. or Train Name : ")
    print("\n\n.......Fetching Details")
    time.sleep(2)
    print("\nProcessing.......")
    time.sleep(3)
    os.system("cls")
    Detail(a)