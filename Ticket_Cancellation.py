#Ticket_Cancellation
import os, sys, time 
import mysql.connector as s
con = s.connect(host="localhost",user="root",database="railway_reservation_system",password="TanujKhajanBhatt")
cur = con.cursor()
def CANCEL():
    m = []
    while m== []:
        print("="*80, "\n \t\t\t\tTICKET CANCELLATION\n",)
        print("="*80)
        PNR_No = input("\nEnter PNR Name : ")
        time.sleep(1.5)
        cur.execute("select PNR_No from Tickets where PNR_No = " + PNR_No)
        m = cur.fetchall()
        if m == []:
            print("\nNo such Reservation Found......")
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
            try:
                cur.execute("delete from Tickets where PNR_No = " + PNR_No )
                con.commit()
                print("\n\nSuccessfully cancelled......\n\n")
            except:
                print("\n\nSome error occured....  :(\n\n")
        print("_"*80)