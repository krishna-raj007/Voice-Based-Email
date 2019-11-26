# importing libraries

import speech_recognition as sr
import retrieve_email as rm
import text_to_speech as ts
import send_mail as sm
import Tutorial_Messages as tm

account, smtp =0,0
def initialise():
    file1 = open("userIDPassword.txt", "r")
    login, password = file1.readline().split(",")
    print(login, password)
    file1.close()
    global account
    account = rm.Gmail_imap(login, password)
    global smtp
    smtp = sm.Gmail_smtp(login, password)

def get_credentials():
    ts.t2s("Speak your email id")
    userid = ts.get_command()
    ts.t2s("speak your password")
    password = ts.get_command()
    print("userid=", userid, "pass=", password)


def readAll():
    print("readAll")
    tm.readAll_msg()
    l = account.get_allmail()
    for i in l:
        mail = i.from_addr + " " + i.title
        ts.t2s(mail)
        cmd = ts.get_command()
        if cmd == "read":
            mail = i.body
            ts.t2s(mail)
        elif cmd == "next":
            continue
        elif cmd == "forward":
            smtp.forward_mail(i.body)
        elif cmd == "delete":
            pass
        elif cmd == "reply":
            smtp.reply_mail(i.from_addr)
        elif cmd == "stop":
            break



def inbox():
    # creates tkinter window or root window
    tm.inbox_msg()

    cmd = ts.get_command()
    if cmd == "readall":
        readAll()
    elif cmd == "dashboard":
        dashboard()



def dashboard():
    # creates tkinter window or root window 
    tm.dashboard_msg()
    cmd = ts.get_command()
    if cmd == "inbox":
        inbox()
    elif cmd == "compose":
        smtp.compose_mail()
    elif cmd == "logout":
        rm.logout()
  
def get_user_response():
    pass


def main():
    initialise()
    # get_credentials()
    dashboard()


main()
