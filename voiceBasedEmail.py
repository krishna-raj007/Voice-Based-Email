#importing libraries

import speech_recognition as sr
from tkinter import *
from tkinter.ttk import *

#importing other modules

import retrieve_email as rm
import text_to_speech as ts
import send_mail as sm

login = 'vinodassignmentiitb@gmail.com'
password = 'assignments@vinod'

account=rm.Gmail_imap(login,password)
smtp=sm.Gmail_smtp(login,password)
window_height=500
window_width=600
window_size='600x500'
root = Tk() 
root.geometry(window_size)
def initialise():
	rm.connection(login,password)


def tutorial_msg():
    ts.t2s("Welcome to your email account. Please enter your choice:")
    ts.t2s("Single left click to compose ")
    ts.t2s("Single right click to send")
    ts.t2s("Double left click to inbox")
    ts.t2s("Double right click to logout")

def get_credentials():
    ts.t2s("Speak your email id")
    userid=ts.get_command()
    ts.t2s("speak your password")
    password=ts.get_command()
    print("userid=",userid,"pass=",password)

def dashboard_gui():
    # creates tkinter window or root window 
    #tutorial_msg()
    # function to be called when button-2 of mouse is pressed 
    dashboard = Frame(root, height = window_height, width = window_width)
    def left_compose(event): 
        print('Button-1 left pressed at x = % d, y = % d'%(event.x, event.y))
        smtp.compose_mail()
      
    # function to be called when button-3 of mouse is pressed 
    def right_send(event): 
        print('Button-3 right pressed at x = % d, y = % d'%(event.x, event.y))
        #smtp.send_mail()
      
    ## function to be called when button-1 is double clocked 
    def dleft_inbox(event): 
        print('Double left clicked at x = % d, y = % d'%(event.x, event.y))
        dashboard.destroy()
        inbox_gui()
        #rm.get_inbox() 
    def dright_logout(event): 
        print('Double right clicked at x = % d, y = % d'%(event.x, event.y))
        #rm.logout()
     
 
      
    # these lines are binding mouse 
    # buttons with the Frame widget 
    dashboard.bind('<Button-1>', left_compose) 
    #dashboard.bind('<Button-3>', right_send) 
    dashboard.bind('<Button-3>', dleft_inbox) 
    dashboard.bind('<Double-Button-3>',dright_logout)
      
    dashboard.pack() 
      
    mainloop() 
    #raise NotImplemented
#####################################################################################
def inbox_gui():
    # creates tkinter window or root window 
    #inbox_tutorial_msg()
    inbox_window = Frame(root, height = window_height, width = window_width)
    # function to be called when button-2 of mouse is pressed 
    def readUnseen(event): 
        print('Button-1 left pressed at x = % d, y = % d'%(event.x, event.y))
        print("readUnseen")
        l=account.get_unseenmail()
        for i in l:
        	mail=i.from_addr+" "+i.title+" "+i.body
        	ts.t2s(mail)        	
        	#readMail_brief(i)      
    # function to be called when button-3 of mouse is pressed 
    def searchmail(event): 
        print('Button-3 right pressed at x = % d, y = % d'%(event.x, event.y))
        print("searchmail")
      
    ## function to be called when button-1 is double clocked 
    def readAll(event): 
        print('Double left clicked at x = % d, y = % d'%(event.x, event.y))
        print("readAll")
        l=account.get_allmail()
        for i in l:
        	mail=i.from_addr+" "+i.title
        	ts.t2s(mail)
        	cmd=ts.get_command()
        	#readMail_brief(i)
    def gotodashboard(event): 
        print('Double right clicked at x = % d, y = % d'%(event.x, event.y))
        print("other")
        inbox_window.destroy()
        dashboard_gui()     
      
    # these lines are binding mouse 
    # buttons with the Frame widget 
    inbox_window.bind('<Button-1>', readUnseen) 
    inbox_window.bind('<Button-3>', searchmail) 
    inbox_window.bind('<Double-Button-1>', readAll) 
    inbox_window.bind('<Double-Button-3>',gotodashboard)
      
    inbox_window.pack() 
    mainloop() 
    #raise NotImplemented
#####################################################################################
"""def readMail_full(mail):
	print("from:",mail.from_addr)
	print("to:",mail.to)
	print("cc:",mail.cc)
	print("title:",mail.title)
	print("body:",mail.body)
	print("attch:",mail.attachments)

def readMail_brief(mail):
	read_window=Frame(root, height = window_height, width = window_width)
	print("from:",mail.from_addr)
	print("title:",mail.title)
	read_window.bind('<Button-1',readMail_full(mail))
	read_window.pack()
	return
	"""
def main():
    #initialise()
    #get_credentials()
    dashboard_gui()
    
main()