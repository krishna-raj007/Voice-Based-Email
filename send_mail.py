
import smtplib    
import text_to_speech as ts
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib

class Gmail_smtp:
    """Class to create SMTP object and implement various features of SMTP protocol"""
    def __init__(self, userid, password):
        """init to get user name and password .
        :param userid: gmail user id of user
        :type userid: string
        :param password: user account password
        :type password: string"""
        self.userid = userid
        self.password = password

    def compose_mail(self):
        """compose a mail """
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


    def send_mail(self, msg):
        """function to send mails
        :param msg: message to send
        :type msg: string"""
        print("in send_mail")
        ts.t2s(" Speak recepient's email address")
        print(" Speak recepient's email address")
        receiever = ts.get_email()
        print(receiever)
        reciever = "gaurav.singh.atoria@gmail.com"
        ts.t2s("Your message reciever is:" + reciever)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("Connected to gmail server")
        server.starttls()
        server.login(self.userid, self.password)
        print("logged in")
        server.sendmail(self.userid,receiver, msg)
        ts.t2s("your message has been sent")
        return

    def forward_mail(self, msg):
        """function to forward mail
        :param msg: message to forward
        :type msg: string"""
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

    def reply_mail(self,recepient_id):
        """function to send reply of a  mail
        :param recepient_id: gmail user id of receiver
        :type recepient_id: string"""
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

    def save_mail(self, message):
        """functioin to save composed mail as draft.
        :param message: message of mail to save as draft.
        :type message: string"""
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
