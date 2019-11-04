
import smtplib    
import text_to_speech as ts
import speech_recognition as sr
#import voiceBasedEmail as vbe

class Gmail_smtp:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

    def compose_mail(self):
        print("incompose")
        ts.t2s("Welcome to compose mail. Speak your text message")
        print(" Speak your message")
        msg = ts.get_command()
        # ts.t2s("Your message is:"+msg)
        # ts.t2s("If corect say yes else say no")
        print("Your message is:" + msg)
        print("If corect say yes else say no")
        ts.t2s("Your message has been recorded. Say 1 to send mail and 2 to save")
        choice=ts.get_command()
        if choice == "1":
            self.send_mail(msg)
        elif choice == "2":
            self.save_mail(msg)
        return


    def send_mail(self, msg):
        print("in send_mail")
        # the function should take take user name and password and return the contents of inbox
        # in a format that we can extract mails from it
        # raise NotImplemented
        ts.t2s(" Speak recepient's email id")
        print(" Speak recepient's email id")

        receiever=ts.get_command()
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



    # def save_mail(self, msg):
    #     pass
