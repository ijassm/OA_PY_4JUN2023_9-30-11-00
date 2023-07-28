# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = "நானே ஆதிநாராயணன். நான் கடலில் மலைப்பாம்பு வகுப்பு படிக்கிறேன். நான் இசையை கேட்க விரும்புகிறேன் நண்பர்களே"

# Language in which you want to convert
language = "ta"

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
