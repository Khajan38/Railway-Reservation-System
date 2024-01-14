#Tickets Reservation 
import os, sys, time 
import mysql.connector as s
con = s.connect(host="localhost",user="root",database="railway_reservation_system",password="TanujKhajanBhatt")
cur = con.cursor()
def INSERT():
    m = []
    while m == []:
        print("="*80, "\n \t\t\t\tTICKET RESERVATION\n",)
        print("="*80)
        Name = input("\nEnter Train No\Train Name : ")
        o = Name.split(" ")
        o = "".join(o)
        if o.isalpha():
            y , z = "0" , Name
        elif o.isdigit():
            y , z = Name ,"0"
        else :
            z = y = "0"
        cur.execute("select Train_No from Train where Train_No = " + y + " or Train_Name = \"" + z + "\"")
        m = cur.fetchall()
        if m == []:
            print("\nNo such Trains Found......")
            time.sleep(0.5)
            print("\nPlease Try again...\n")
            print("_"*80)
            Cont = input("\n \t\tPress Enter to continue Or Q to quit the Program")
            os.system("cls")
            if Cont == "":
                continue
            else :
                time.sleep(0.5)
                os.system("cls")
                sys.exit()
        else : 
            print("\n\nLoading....\n")
            print("_"*80)
            time.sleep(1)
            os.system("cls")
            print("="*80, "\n \t\t\t\tTICKET RESERVATION\n",)
            print("="*80)
            Name = input("\nEnter Passanger's Name : ")
            Age = input("\nEnter Passanger's Age  : ")
            print('''\nWhich Class of seat will you tike to travel :
\t1st     : 1st Class
\t2nd     : 2nd Class
\t3rd     : 3rd Class
\tSleeper : Sleeper Class''')
            Class = input("\nEnter Your Choice : ")
            print()
            print("_"*80)
            print("\nChecking Available Seats....\n")
            time.sleep(1)
            cur.execute("select %s_Class-sum(No_of_Seats) from Tickets,Train where Tickets.Train_No = %s and Train.Train_No = %s and Seat_Class = \"%s\"" %(Class,m[0][0],m[0][0],Class))
            M = cur.fetchall()
            if M == [(None,)]:
                cur.execute("select %s_Class from Train where Train_No = %s" %(Class,m[0][0]))
                M = cur.fetchall()
            if M[0][0] > 0:
                print("\nAvailable seats : ", M[0][0])
                Seats = input("\n\nNo. of seats to be booked : ")
                print()
                print("*"*80)
                time.sleep(1)
                os.system('cls')
                print("\n\nWorking with Given Details......")
                time.sleep(1)    
                try:
                    cur.execute("Insert into Tickets(Passanger_Name,Passanger_Age, Train_No, Seat_Class, No_of_Seats) values (\""+Name+"\","+Age+","+str(m[0][0])+",\""+Class+"\","+Seats+")")
                    cur.execute("Update Tickets set PNR_No = PNR_No - 16983 where Passanger_Name = \""+Name+"\"")
                    con.commit()
                    cur.execute("select PNR_No from Tickets where Passanger_Name = \""+Name+"\" and Passanger_Age ="+Age+" and Train_No = "+str(m[0][0]))
                    m = cur.fetchall()
                    print("\n\nSuccessfully reserved......\n\n")
                    print("\t\t\tYour PNR No. is "+str(m[0][0])+"\n\n")
                except:
                    print("\n\nSome error occured....  :(\n\n")
                print("_"*80)
            else:
                print("\nSorry no seats available.... :( \n\n")