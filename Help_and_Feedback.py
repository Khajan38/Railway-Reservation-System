#Help and Feedback
import os, time 
import Railway.Sounds.Sound
def CHOICE():
    print("="*80,"\n \t\t\t\tHELP AND FEEDBACK \n")
    print("="*80)
    print('''\n \t\t\t\tDo You want : 
\n \t\t\t1. Help 
\n \t\t\t2. To Give Feedback''')
    a = int(input("\n\nEnter your Choice : "))
    time.sleep(2)
    print("\n\nInitiating.......")
    time.sleep(1)
    os.system("cls")
    return(a)
def HELP():
    myfile = open(r"D:\PYTHON IDLE\Lib\site-packages\Railway\Help_and_Feedback\Help_Message.txt","r")
    i,m = [221,366,527,731],0
    while m < 5:
        print("="*80, "\n \t\t\t\t PROJECT HELP\n",)
        print("="*80)
        if m < 4:
            print(myfile.read(i[m]))
            a = input("\t\t\t\tPress Enter...")
            os.system("cls")
        else :
            print(myfile.read())
            a = "Hope it Helps....."
            print("\n \t\t\t\t"+a+"\n")
            print("="*80)
        m = m + 1
def FEEDBACK():
    print("="*80, "\n \t\t\t\t PROJECT HELP\n",)
    print("="*80)
    print('''\t\t\t\tRatings :
     
     -> Outstanding     : ***** 
     -> Good            : ****
     -> Satisfactory    : ***
     -> Poor            : **
     -> Unsatisfactory  : *\n''')
    print("_"*80)
    time.sleep(1)
    a = input("\n Presentation     : ")
    a = input("\n Use of Functions : ")
    a = input("\n User Interaction : ")
    Railway.Sounds.Sound.FEEDBACK()
    a = "Thank you for your Feedback.... :)"
    print("\n \t\t\t"+a+"\n")
    print("="*80)