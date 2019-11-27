
import smtplib    
import text_to_speech as ts
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib


##
# @brief Class to create SMTP object and implement various features of SMTP protocol
#
class Gmail_smtp:


    ##
    # @brief init()
    #
    # @details nit to get user name and password
    #
    # @param[in]    userid    user email id
    # @param[in]    password    password for login
    #
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

    ##
    # @brief Compose mails
    #
    # @details compose a mail
    #
    def compose_mail(self):

        print("incompose")
        ts.t2s("Welcome to compose mail. Speak subject of message")
        print(" Speak your message")
        subject = ts.get_command()
        ts.t2s("Now speak the email content")
        text = ts.get_command()
        # ts.t2s("Your message is:"+msg)
        # ts.t2s("If corect say yes else say no")
        print("Your message is:" + text)
        print("If correct say yes else say no")
        msg = 'Subject: {}\n\n{}'.format(subject, text)

        # msg = email.message.Message()
        # msg['Subject'] = 'subject of the message'
        # msg['From'] = self.userid
        #
        # msg.set_payload(text)


        ts.t2s("Your message has been recorded. Say send to send this mail and save to save it to drafts")
        choice = ts.get_command(["send","save"])
        if choice == "send":
            self.send_mail(msg)
        elif choice == "save":
            self.save_mail(msg)
        return

    ##
    # @brief Send mail
    #
    # @details function to send mails
    #
    # @param[in]    msg    message to send
    #
    def send_mail(self, msg):

        print("in send_mail")
        ts.t2s(" Speak recepient's email address")
        print(" Speak recepient's email address")
        receiver = ts.get_email()
        print(receiver)

        ts.t2s("Your message reciever is:" + receiver)
        receiver = "vkmzp8896@gmail.com"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("Connected to gmail server")
        server.starttls()
        server.login(self.userid, self.password)
        print("logged in")
        server.sendmail(self.userid,receiver, msg)
        ts.t2s("your message has been sent")
        return


    ##
    # @brief Forward mail
    #
    # @details function to forward mail
    #
    # @param[in]    msg    message to forward
    #
    def forward_mail(self, msg):

        ts.t2s(" Speak recepient's email id")
        print(" Speak recepient's email id")

        receiever = ts.get_email()
        print(receiever)
        reciever = "gaurav.singh.atoria@gmail.com"
        ts.t2s("Your message reciever is:" + reciever)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("Connected to gmail server")
        server.starttls()
        server.login(self.userid, self.password)
        print("logged in")
        server.sendmail(self.userid, "gaurav.singh.atoria@gmail.com", msg)
        ts.t2s("your message has been sent")
        return

    ##
    # @brief Reply mail
    #
    # @details function to send reply of a  mail
    #
    # @param[in]    recepient_id    gmail user id of receiver
    #
    def reply_mail(self,recepient_id):

        ts.t2s("Please provide your reply")
        print(" Speak your reply")
        reply = ts.get_command()
        # ts.t2s("Your message is:"+msg)
        # ts.t2s("If corect say yes else say no")
        #print("Your message is:" + reply)
        #print("If correct say yes else say no")
        ts.t2s("Your reply has been recorded. Say send to send the reply")
        choice = ts.get_command(["send","save"])
        if choice == "send":
            server = smtplib.SMTP('smtp.gmail.com', 587)
            print("Connected to gmail server")
            server.starttls()
            server.login(self.userid, self.password)
            print("logged in")
            server.sendmail(self.userid, recepient_id, reply)
            ts.t2s("your reply has been sent to " + recepient_id)
            return
        else:
            ts.t2s("Reply not sent")

    ##
    # @brief Save mail
    #
    # @details functioin to save composed mail as draft
    #
    # @param[in]    message    message of mail to save as draft
    #
    def save_mail(self, message):
        # msg = email.message.Message()
        # msg['Subject'] = 'subject of the message'
        # msg['From'] = self.userid
        # msg['To'] = MY_EMAIL
        # msg.set_payload(message)
        # # append the message to the drafts folder
        # now = imaplib.Time2Internaldate(time.time())
        # imap.append('[Gmail]/Drafts', '', now, msg.as_bytes())
        msg = MIMEMultipart("alternative")
        msg.set_charset("utf-8")
        msg.attach(MIMEText(message, "plain", "utf-8"))
        msg['Subject'] = "SUBJECT"
        msg['From'] = self.userid
        msg['To'] = "rajsrivastava871@gmail.com"
        conn = imaplib.IMAP4_SSL('imap.gmail.com', port=993)
        conn.login(self.userid, self.password)
        conn.select('[Gmail]/Drafts')
        conn.append("[Gmail]/Drafts", '', imaplib.Time2Internaldate(time.time()), msg.as_bytes())
        ts.t2s("Saved to drafts")
