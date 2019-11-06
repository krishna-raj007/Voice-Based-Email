#importing libraries

import speech_recognition as sr
from tkinter import *
from tkinter.ttk import *

#importing other modules

import retrieve_email as rm
import text_to_speech as ts
import send_mail as sm
import Tutorial_Messages as tm

login = 'vinodassignmentiitb@gmail.com'
password = 'assignments@vinod'

account=rm.Gmail_imap(login,password)
smtp=sm.Gmail_smtp(login,password)
window_height=500
window_width=600
window_size='600x500'
root = Tk() 
root.geometry(window_size)

def get_credentials():
    ts.t2s("Speak your email id")
    userid=ts.get_command()
    ts.t2s("speak your password")
    password=ts.get_command()
    print("userid=",userid,"pass=",password)

def dashboard_gui():
    # creates tkinter window or root window 
    tm.dashboard_msg()
    # function to be called when button-2 of mouse is pressed 
    dashboard = Frame(root, height = window_height, width = window_width)
    def left_compose(event): 
        print('Button-1 left pressed at x = % d, y = % d'%(event.x, event.y))
        smtp.compose_mail()
      
    ## function to be called when button-1 is double clocked 
    def right_inbox(event): 
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
    dashboard.bind('<Button-2>', right_inbox)
    dashboard.bind('<Double-Button-2>',dright_logout)
      
    dashboard.pack() 
      
    mainloop() 
    #raise NotImplemented
#####################################################################################
def inbox_gui():
    # creates tkinter window or root window 
    tm.inbox_msg()
    inbox_window = Frame(root, height = window_height, width = window_width)
    # function to be called when button-2 of mouse is pressed 
    # def readUnseen(event): 
    #     print('Button-1 left pressed at x = % d, y = % d'%(event.x, event.y))
    #     print("readUnseen")
    #     l=account.get_unseenmail()
    #     for i in l:
    #     	mail=i.from_addr+" "+i.title+" "+i.body
    #     	ts.t2s(mail)        	
        	#readMail_brief(i)      
    # function to be called when button-3 of mouse is pressed 
    # def searchmail(event): 
    #     print('Button-3 right pressed at x = % d, y = % d'%(event.x, event.y))
    #     print("searchmail")
      
    ## function to be called when button-1 is double clocked 
    def readAll(event): 
        print('Double left clicked at x = % d, y = % d'%(event.x, event.y))
        print("readAll")
        tm.readAll_msg()
        l=account.get_allmail()
        for i in l:
        	mail=i.from_addr+" "+i.title
        	ts.t2s(mail)
        	cmd=ts.get_command()
        	if cmd=="read":
        		mail=i.body
        		ts.t2s(mail)
        	elif cmd=="next":
        		continue
        	elif cmd=="forward":
        		smtp.forward_mail(i.body)
        	elif cmd=="delete":
        		pass
        	elif cmd=="reply":
        		smtp.reply_mail(i.from_addr)
        	elif cmd=="stop":
        		break
    def gotodashboard(event): 
        print('Double right clicked at x = % d, y = % d'%(event.x, event.y))
        print("other")
        inbox_window.destroy()
        dashboard_gui()     
      
    # these lines are binding mouse 
    # buttons with the Frame widget 
    # inbox_window.bind('<Button-1>', readUnseen) 
    # inbox_window.bind('<Button-3>', searchmail) 
    inbox_window.bind('<Button-1>', readAll) 
    inbox_window.bind('<Button-2>',gotodashboard)
      
    inbox_window.pack() 
    mainloop() 
    #raise NotImplemented
def main():
    #initialise()
    #get_credentials()
    dashboard_gui()
    
main()