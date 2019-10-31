from gtts import gTTS 
import os 
def t2s(text):
    #the function should take a string in text and we should get an output through the speakers
    print(text)
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("./VoiceFiles/audio.mp3")
    os.system("mpg321 ./VoiceFiles/audio.mp3")
    #os.remove("../VoiceFiles/audio.mp3")
    #raise NotImplemented


