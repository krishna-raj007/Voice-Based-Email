import smtplib
import speech_recognition as sr


srObj = sr.Recognizer()
print("Welcome to your email account. Please enter your choice:")
print("1: Compose Mail")
print("2: Read from inbox")
with sr.Microphone() as source:
    choice_audio=srObj.listen(source)

choice=srObj.recognize_google(choice_audio)
#put a check if only one of the two choices are present or not

if choice == '1':
    print ("Your Choice is 1. Speak your message")
    with sr.Microphone() as source:
        choice_audio=srObj.listen(source)
    msg=srObj.recognize_google(choice_audio)
    print ("Your message is:",msg)
    # Say confirm or go back
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("rajsrivastava871@gmail.com", "9721377988Krishna@7")
    server.sendmail("rajsrivastava871@gmail.com", "krishna_raj007@yahoo.in", msg)
    print ("your message has been sent")
