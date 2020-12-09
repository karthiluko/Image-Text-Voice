from gtts import gTTS 
import os
from playsound import playsound
def voice(filename):
    file = open(filename, "r").read()
    speech=gTTS(text=str(file),lang='en',slow=False)
    path='voicefile.mp3'
    speech.save(path)
    playsound(path)
    if os.path.exists(path):
        os.remove(path)


if __name__=="__main__":
    voice("newtext.txt")

