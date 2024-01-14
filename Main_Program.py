# Main Program
import os, sys, time
from playsound import playsound
import Railway.Sounds.Sound
import Railway.Main_Program.Main_Menu
import Railway.Train.Train_Details
import Railway.Train.Train_Update
import Railway.Tickets.Ticket_Reservation
import Railway.Tickets.Ticket_Cancellation
import Railway.Tickets.PNR_Status
import Railway.Help_and_Feedback.Help_and_Feedback
# Password Screen
import Railway.Main_Program.Password_Screen
a = Railway.Main_Program.Password_Screen.Password()
# Main Programs
while a :
    Railway.Main_Program.Main_Menu.Menu()
    a = input("\nEnter your choice : ")
    time.sleep(0.5)
    print("\n\nInitiating......\n")
    time.sleep(1)
    os.system('cls')
    if a == "1":
        Railway.Train.Train_Details.DETAIL()
    elif a == "2":
        a = Railway.Train.Train_Update.CHOICE()
        if a == 1:
            Railway.Train.Train_Update.INSERT()
        else :     
            Railway.Train.Train_Update.UPDATE()
    elif a == "3":
        Railway.Tickets.Ticket_Reservation.INSERT()
    elif a == "4":
        Railway.Tickets.Ticket_Cancellation.CANCEL()
    elif a == "5":
        Railway.Tickets.PNR_Status.STATUS()
    elif a == "6":
        a = Railway.Help_and_Feedback.Help_and_Feedback.CHOICE()
        if a == 1:
            Railway.Help_and_Feedback.Help_and_Feedback.HELP()
        else :     
            Railway.Help_and_Feedback.Help_and_Feedback.FEEDBACK()
    elif a == "7" :
        time.sleep(0.5)
        print("\n\n \t\t\t\tQuitting....")
        Railway.Sounds.Sound.THANKS()
        os.system("cls")
        sys.exit()
    else :
        print("\n\nPlease enter a valid input.... \n")
        Railway.Sounds.Sound.INPUT()
        print("_"*80)
    time.sleep(1)
    Railway.Sounds.Sound.CONTQUIT()
    a = input("\n \t  Enter M to go to Menu Or any Other key to end the program ")
    if a == "M":
        continue
    else :
        time.sleep(0.5)
        print("\nQuitting....")
        Railway.Sounds.Sound.THANKS()
        time.sleep(1.5)
        os.system("cls")
        break