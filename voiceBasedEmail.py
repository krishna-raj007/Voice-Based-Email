#importing libraries
import smtplib
import speech_recognition as sr
<<<<<<< HEAD

#importing other modules
import retrieve_email
=======
import retrieve_email as rm
>>>>>>> 7a99ba00381260de34c6cbde0db4af927cdbb605
import text_to_speech as ts
from tkinter import *
from tkinter.ttk import *

login = 'vinodassignmentiitb@gmail.com'
password = 'assignments@vinod'
srObj = sr.Recognizer()
<<<<<<< HEAD
ts.t2s("Welcome to your email account. Please enter your choice:")
print("Welcome to your email account. Please enter your choice:")
ts.t2s("1: Compose Mail")
ts.t2s("2: Read from inbox")
ts.t2s("3: Read from sendbox")
ts.t2s("4: Set Reminder Mail")
print("1: Compose Mail")
print("2: Read from inbox")

with sr.Microphone() as source:
    choice_audio=srObj.listen(source)

choice=srObj.recognize_google(choice_audio)
#put a check if only one of the two choices are present or not
print ("You said:", choice)
ts.t2s("You said:"+choice)

if choice == '1' or choice == 'one':
=======


def initialise():
    pass

def tutorial_msg():
    ts.t2s("Welcome to your email account. Please enter your choice:")
    ts.t2s("Single left click to compose ")
    ts.t2s("Single right click to send")
    ts.t2s("Double left click to inbox")
    ts.t2s("Double right click to logout")
def get_command():
    with sr.Microphone() as source:
        choice_audio=srObj.listen(source)
    choice=srObj.recognize_google(choice_audio)
    #put a check if only one of the two choices are present or not
    print ("You said:", choice)
    ts.t2s("You said:"+choice)
    return choice

def get_credentials():
    ts.t2s("Speak your email id")
    userid=get_command()
    ts.t2s("speak your password")
    password=get_command()
    print("userid=",userid,"pass=",password)
"""
if choice == '1':
>>>>>>> 7a99ba00381260de34c6cbde0db4af927cdbb605
    ts.t2s(" Speak your message")
    print(" Speak your message")
    with sr.Microphone() as source:
        choice_audio=srObj.listen(source)
    msg=srObj.recognize_google(choice_audio)
    ts.t2s("Your message is:"+msg)
    ts.t2s("If corect say yes else say no")
    print("Your message is:"+msg)
    print("If corect say yes else say no")
    with sr.Microphone() as source:
        choice_audio=srObj.listen(source)
    choice=srObj.recognize_google(choice_audio)
    if choice == "yes":
        ts.t2s("You said Yes")
<<<<<<< HEAD
        ts.t2s(" Speak recepient's email id")
        print(" Speak recepient's email id")
        #with sr.Microphone() as source:
        #    choice_audio=srObj.listen(source)
        #receiever=srObj.recognize_google(choice_audio)
        #ts.t2s("Your message reciever is:"+receiever)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_id, password)
        server.sendmail(email_id, "gaurav.singh.atoria@gmail.com", msg)
        ts.t2s("your message has been sent")
    elif choice == "no":
        print ("no")
elif choice == '2' or choice == 'tu' or  choice == 'to':
    ts.t2s("you chose 2")

=======
        ts.t2s("your message has been sent")
"""
>>>>>>> 7a99ba00381260de34c6cbde0db4af927cdbb605

##############################################
def dashboard_gui():
    # creates tkinter window or root window 
    root = Tk() 
    root.geometry('500x400') 
    tutorial_msg()
    # function to be called when button-2 of mouse is pressed 
    def left_compose(event): 
        print('Button-1 left pressed at x = % d, y = % d'%(event.x, event.y))
        rm.compose_mail() 
      
    # function to be called when button-3 of mouse is pressed 
    def right_send(event): 
        print('Button-3 right pressed at x = % d, y = % d'%(event.x, event.y))
        rm.send_mail() 
      
    ## function to be called when button-1 is double clocked 
    def dleft_inbox(event): 
        print('Double left clicked at x = % d, y = % d'%(event.x, event.y))
        rm.get_inbox() 
    def dright_logout(event): 
        print('Double right clicked at x = % d, y = % d'%(event.x, event.y))
        rm.logout()
     
    dashboard = Frame(root, height = 100, width = 200) 
      
    # these lines are binding mouse 
    # buttons with the Frame widget 
    dashboard.bind('<Button-1>', left_compose) 
    dashboard.bind('<Button-3>', right_send) 
    dashboard.bind('<Double-Button-1>', dleft_inbox) 
    dashboard.bind('<Double-Button-3>',dright_logout)
      
    dashboard.pack() 
      
    mainloop() 
    #raise NotImplemented
#####################################################################################
def main():
    initialise()
    get_credentials()
    dashboard_gui()
    
main()