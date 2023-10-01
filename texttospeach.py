from gtts import gTTS

import os

mytext = input(print("Enter text:"))
title = input(print("Enter title:"))
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(f"{title}.mp3")

os.system(f"{title}.mp3")