## @mainpage
# @brief Fully voice controlled Emailling Application
# @details Voice Based Email is an application which can be used by anyone to manage his mailbox through voice commands.
# Once the application starts the user can speak what he needs to do without using his hands or or eyes as the application will guide the user at each step through voice commands.
# The system will take the voice input from the user process the instructions and move to the next step accordingly.
#   -# login to gmail account
#   -# retrieve emails from inbox
#   -# compose and send emails
#   -# read mails and perform actions such as reply, forwarding,deleting , etc.
#   -# other feature related to speech and user convenience.
#
# The packages used:
# - smtplib :to send emails
# - imaplib : to retrieve mails
# - speech_recognition : to get voice commands
# - easyimap : to get emails

## @file
# @brief The driver program
# @details This manages all functionalities of the application and interaction with other file/modules

import speech_recognition as sr
import retrieve_email as rm
import text_to_speech as ts
import send_mail as sm
import Tutorial_Messages as tms

## @var account
# object of Gmail_imap class to implement member methods.
# \hideinitializer
#

tm=tms.Tutorial_Messages()
account=0
## @var smtp
# object of Gmail_smtp class to implement member methods.
# \hideinitializer
#
smtp =0

##
# @brief initialise  variables and create starting environment
#
# @details Creating object of Gmail_imap class and Gmail_smtp class
#        read user id and password from file userIDPassword.txt
#        global variable account stores imap information
#        global variable smtp stores smtp information
#
def initialise():

    file1 = open("userIDPassword.txt", "r")
    login, password = file1.readline().split(",")
    print(login, password)
    file1.close()
    global account
    account = rm.Gmail_imap(login, password)
    global smtp
    smtp = sm.Gmail_smtp(login, password)

#
# def get_credentials():
#     """function to get user id and password from user as voice input"""
#     ts.t2s("Speak your email id")
#     userid = ts.get_command()
#     ts.t2s("speak your password")
#     password = ts.get_command()
#     print("userid=", userid, "pass=", password)

def get_mailbox(st):
    #tm.mailboxes_msg()
    #cmd =ts.get_command(["inbox","sent","important","drafts"])
    account.change_mailbox(st)
##
# @brief Read all mails
#
# @details This function read out sender and subject of mail to user.Then perform action given by user
#     such as read entire mail, forward this mail, reply to current mail, delete, read next, and stop reading.
#     User is informed about available commands.
#
# @param[in]    mail_list    list of mails to read
#
#
def readAll(mail_list):

    #print("readAll")
    tm.readAll_msg()
    for i in mail_list:
        mail = i.from_addr + " " + i.title
        ts.t2s(mail)
        cmd = ts.get_command(["read","next","forward","delete","reply","stop"])
        if cmd == "read":
            mail = i.body
            ts.t2s(mail)
        elif cmd == "next":
            continue
        elif cmd == "forward":
            smtp.forward_mail(i.body)
        elif cmd == "delete":
            account.delete_mail(i.from_addr, i.from_addr)
            print("deleted")
        elif cmd == "reply":
            smtp.reply_mail(i.from_addr)
        elif cmd == "stop":
            break
##
# @brief Get all unseen mails
#
# @details This function retrieves all unseen mails from user's inbox
#
#
def get_allUnseenMail():

    l = account.get_unseenmail()
    list=account.fetch_mail_id(l)
    return list
##
# @brief Inbox
#
# @details Retrieve mails of user account.User can choose to get all mails or only unseen mails.
#         If no command is given ,user goes back to dashboard.
#
#
def inbox():

    tm.inbox_msg()
    cmd = ts.get_command(["unseen", "read all"])
    if cmd == "read all":
        l = account.get_allmail()
        readAll(l)
    elif cmd == "unseen":
        l=get_allUnseenMail()
        readAll(l)
    dashboard()
#
# def sentbox():
#     #account.change_mailbox("sent")
#     tm.box_msg()
#     cmd = ts.get_command(["read all","dashboard"])
#     if cmd == "read all":
#         l = account.get_allmail()
#         readAll(l)
#     elif cmd == "dashboard":
#         dashboard()
#
# def important_box():
#     account.change_mailbox("important")
#     tm.box_msg()
#     cmd = ts.get_command(["read all","dashboard"])
#     if cmd == "read all":
#         l = account.get_allmail()
#         readAll(l)
#     elif cmd == "dashboard":
#         dashboard()
#
#
# def draft_box():
#     account.change_mailbox("drafts")
#     tm.box_msg()
#     cmd = ts.get_command(["read all","dashboard"])
#     if cmd == "read all":
#         l = account.get_allmail()
#         readAll(l)
#     elif cmd == "dashboard":
#         dashboard()

##
# @brief Dashboard
#
# @details Dashboard for user after successful login. User can go to inbox, mailbox, logout or compose mail
#
#
def dashboard():
    """Dashboard for user after successful login. User can go to inbox, mailbox, logout or compose mail """
    tm.dashboard_msg()
    cmd = ts.get_command(["inbox", "compose", "mailbox", "logout"])
    if cmd == "inbox":
        inbox()
    elif cmd == "compose":
        smtp.compose_mail()
    elif cmd == "mailbox":
        get_mailbox()
    elif cmd == "logout":
        account.account_logout()
##
# @brief Mian()
#
# @details Main function to initialise and lunch account dashboard.
#
#
def main():

    initialise()
    dashboard()

    # get_mailbox("sent")
    # l = account.get_allmail()
    # print(l)

main()
