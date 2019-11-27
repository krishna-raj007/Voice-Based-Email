from gtts import gTTS
import speech_recognition as sr
import os 
## @var srObj
# Speech recognition object to use its methods for reading input at microphone.
# \hideinitializer
#
srObj = sr.Recognizer()


##
# @brief Text to Speech
#
# @details the function converts text to voice.
#
# @param[in]    text    sentence to convert to speech.
#
def t2s(text):

    print(text)
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("./VoiceFiles/audio.mp3")
    os.system("mpg321 ./VoiceFiles/audio.mp3")
    #os.remove("../VoiceFiles/audio.mp3")
    #raise NotImplemented

##
# @brief Distance
#
# @details the function calculate distance between two commands.
#
# @param[in]    word1    command .
# @param[in]    word2    command .
#
def distance(word1,word2):
    l1=len(word1)
    l2=len(word2)
    matrix = [[0 for x in range(l2 + 1)] for x in range(l1 + 1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0 or j==0:
                matrix[i][j] = i+j
            else:
                e=0
                if word1[i-1]!=word2[j-1]:
                    e = 1 + (i/l1)
                matrix[i][j] = min(matrix[i][j-1]+1,matrix[i-1][j]+1,matrix[i-1][j-1]+e)
    return matrix[l1][l2]

def closest(inp,options):
    min_dist=9999
    for i in options:
        d=distance(i, inp)
        if d < min_dist:
            min_dist= d
            closest_word=i
    return closest_word

##
# @brief Take Command from user
#
# @details function to take user input as voice and convert it into sentence/text. On receiving command as input, compares it with
#      list of possible commands provided as argument and return command. Otherwise requires user conformation.
#
# @param[in]    options    list of possible commands that user should give. .
#
def get_command(options=None):

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
        if options != None:
            if voice_inp not in options:
                return closest(voice_inp,options)
            else:
                return voice_inp

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

##
# @brief Take Email Address from user
#
# @details function to take mail address of user  as voice input and parse it in a valid mail address.
#
#
def get_email():

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
        voice_inp.replace("dot", ".")
        voice_inp.replace("underscore", "_")
        voice_inp.replace("at", "@")
        voice_inp.replace(" ", "")
        print("You said:", voice_inp)
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
            t2s("Some problem occured. Kindly repeat you message")
            continue
    print("returning message")
    return voice_inp