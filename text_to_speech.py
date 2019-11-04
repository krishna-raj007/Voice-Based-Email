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

    while (1):
        t2s("speak now")
        try:
            with sr.Microphone() as source:
                choice_audio = srObj.listen(source)
            voice_inp = srObj.recognize_google(choice_audio)
            break
        except:
            t2s("Pardon me. Could you please repeat")
            print("Pardon me. Could you please repeat")
        # put a check if only one of the two choices are present or not
    print("You said:", voice_inp)
    t2s("You said:" + voice_inp)
    return voice_inp