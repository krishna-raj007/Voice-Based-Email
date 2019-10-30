import smtplib
import speech_recognition as sr
import retrieve_email as rm
import text_to_speech as ts
from tkinter import *
from tkinter.ttk import *

login = 'vinodassignmentiitb@gmail.com'
password = 'assignments@vinod'
srObj = sr.Recognizer()


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
    ts.t2s(" Speak your message")
    with sr.Microphone() as source:
        choice_audio=srObj.listen(source)
    msg=srObj.recognize_google(choice_audio)
    ts.t2s("Your message is:"+msg)
    ts.t2s("If corect say yes else say no")
    with sr.Microphone() as source:
        choice_audio=srObj.listen(source)
    choice=srObj.recognize_google(choice_audio)
    if choice == "yes":
        ts.t2s("You said Yes")
        ts.t2s("your message has been sent")
"""

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