from gtts import gTTS 
import speech_recognition as sr
import os 

srObj = sr.Recognizer()
def t2s(text):
    #the function should take a string in text and we should get an output through the speakers
    print(text)
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("./VoiceFiles/audio.mp3")
    os.system("mpg321 ./VoiceFiles/audio.mp3")
    #os.remove("../VoiceFiles/audio.mp3")
    #raise NotImplemented


def get_command():
    while(1):
        while (1):
            #t2s("Speak now")
            try:
                with sr.Microphone() as source:
                    choice_audio = srObj.listen(source)
                voice_inp = srObj.recognize_google(choice_audio)
                break
            except:
                t2s("I dint get you . Could you please repeat")
                print("I dint get you . Could you please repeat")
            # put a check if only one of the two choices are present or not
        print("You said:", voice_inp)
        t2s("You said:" + voice_inp + ". Say yes to confirm and no to try again ")
        try:
            with sr.Microphone() as source:
                choice_audio = srObj.listen(source)
            confirmation = srObj.recognize_google(choice_audio)
            print ("you said"+confirmation)
            if confirmation == "yes":
                break
            elif confirmation == "no":
                t2s("You said no. Kindly repeat you message")
            else:
                t2s("Couldn't recognize that taking its as no. Kindly repeat you message")
        except Exception as e:
            print(e)
            t2s("Some problem occured . Kindly repeat you message")
            continue
    print ("returning message")
    return voice_inp


def get_email():
    while(1):
        while (1):
            t2s("Speak now")
            try:
                with sr.Microphone() as source:
                    choice_audio = srObj.listen(source)
                voice_inp = srObj.recognize_google(choice_audio)
                break
            except:
                t2s("I dint get you . Could you please repeat")
                print("I dint get you . Could you please repeat")
            # put a check if only one of the two choices are present or not
        print("You said:", voice_inp)
        voice_inp.replace("dot", ".")
        voice_inp.replace("underscore", "_")
        voice_inp.replace("at", "@")
        voice_inp.replace(" ", "")
        t2s("You said:" + voice_inp + ". Say yes to confirm and no to try again ")
        try:
            with sr.Microphone() as source:
                choice_audio = srObj.listen(source)
            confirmation = srObj.recognize_google(choice_audio)
            print("you said" + confirmation)
            if confirmation == "yes":
                break
            elif confirmation == "no":
                t2s("You said no. Kindly repeat you message")
            else:
                t2s("Couldn't recognize that taking its as no. Kindly repeat you message")
        except Exception as e:
            print(e)
            t2s("Some problem occured . Kindly repeat you message")
            continue
    print("returning message")
    return voice_inp