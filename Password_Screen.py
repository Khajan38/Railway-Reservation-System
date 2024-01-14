#Password Screen
import os, time
import Railway.Sounds.Sound
def Password():
    os.system("cls")
    print("="*80)
    print("\t\t\tWELCOME TO THE GREAT INDIAN SUBWAY !! \n")
    print("="*80)
    a = input("\nEnter Password to Continue : ")
    time.sleep(0.5)
    print("\n\nMatching with Administrator.....\n")
    time.sleep(1.5)
    while a != "India" :
        os.system("cls")
        print("="*80)
        print("\t\t\tWELCOME TO THE GREAT INDIAN SUBWAY !! \n")
        print("="*80)
        print("\n\n \t\t\tYou enetered Wrong Password.....\n")
        Railway.Sounds.Sound.ADERROR()
        time.sleep(0.5)
        a = input("\n\nEnter correct password : ")
        time.sleep(0.5)
        print("\n\nMatching with Administrator..... \n ")
        time.sleep(1.5)
    else :
        print("_"*80)
        print("\n \t\t\t\tWelcome.....\n")
        Railway.Sounds.Sound.WELCOME()
        time.sleep(1)
    return a