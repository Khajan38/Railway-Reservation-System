# Update Train Details
import os, time 
import mysql.connector as s
con = s.connect(host="localhost",user="root",database="railway_reservation_system",password="TanujKhajanBhatt")
cur = con.cursor()
def CHOICE():
    print("="*80,"\n \t\t\t\tTRAIN UPDATES \n")
    print("="*80)
    print('''\n \t\t\t\tDo You want to : 
\n \t\t1. Insert Details of New Train
\n \t\t2. Update detail of Existing Train''')
    a = int(input("\n\nEnter your Choice : "))
    time.sleep(2)
    print("\n\nInitiating.......")
    time.sleep(1)
    os.system("cls")
    return(a)
def INSERT():
    print("="*80, "\n \t\t\t\tTRAIN UPDATES\n",)
    print("="*80)
    No = input("\nEnter Train No             : ")
    Name = input("The Train Name is          : ")
    Strt = input("Train starts journey from  : ")
    Finish = input("Train's Destination        : ")
    Fst = input("No. of 1st class seats     : ")
    Secnd = input("No. of 2nd class seats     : ")
    Thrd = input("No. of 3rd class seats     : ")
    Sleeper = input("No. of sleeper class seats : ")
    print()
    print("*"*80)
    time.sleep(1)
    os.system('cls')
    print("\n\nWorking with Given Details......")
    time.sleep(1)
    print("\n\nInserting Details in table.....")
    time.sleep(2)
    try:
        cur.execute("Insert into Train values ("+No+",\""+Name+"\",\""+Strt+"\",\""+Finish+"\","+Fst+","+Secnd+","+Thrd+","+Sleeper+")")
        con.commit()
        print("\n\nSuccessfully Inserted......\n\n")
    except:
        print("\n\nSome error occured....  :(\n\n")
    print("="*80)
def UPDATE():
    print("="*80, "\n \t\t\t\tTRAIN UPDATES\n",)
    print("="*80)
    print('''\nEnter the detail which you want to change :

 -> Train_No
 -> Train_Name
 -> Start_Point
 -> Destination_point
 -> 1st_Class
 -> 2nd_Class
 -> 3rd_Class
 -> Sleeper_Class''')
    a = input("\n\nEnter your Choice : ")
    c = input("Enter previous Train_No \ Train_Name : ")
    b = input("Enter new "+ a+" : ") 
    os.system('cls')
    print("\n\nWorking with Given Details......")
    time.sleep(1)
    o = c.split(" ")
    o = "".join(o)
    if o.isalpha():
        y , z = "0" , c
    elif o.isdigit:
        y , z = c ,"0"
    else :
        z = y = "0"
    cur.execute("Select Train_Name from Train where Train_No = " + y + " or Train_Name = \"" + z + "\"")
    Check1 = cur.fetchall()
    if Check1 == []:
        print("\n\nNo such Train found........\n\n")
    else:
        print("\n\nUpdating Details in table.....")
        time.sleep(2)
        try:
            if a in ["Train_Name","Start_Point","Destination_Point"]:
                cur.execute("Update Train set "+a+" = \""+b+"\" where Train_No = " + y + " or Train_Name = \"" + z + "\"")
            else : 
                cur.execute("Update Train set "+a+" = "+b+" where Train_No = " + y + " or Train_Name = \"" + z + "\"")
            con.commit()
            print("\n\nSuccessfully Updated......\n\n")
        except:
            print("\n\nSome error occured....  :(\n\n")
    print("="*80)