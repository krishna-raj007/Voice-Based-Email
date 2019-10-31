#importing libraries
import smtplib
import speech_recognition as sr

#importing other modules
import retrieve_email
import text_to_speech as ts
email_id = "lionsofmirzapur699@gmail.com"
password = "LionsOfMirzapur"

srObj = sr.Recognizer()
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


##############################################
def mouse_click():
    raise NotImplemented
