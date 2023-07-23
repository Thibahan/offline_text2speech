import pyttsx3

# One time initialization
engine = pyttsx3.init()

engine.setProperty('voice', "german")
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

text = "Hallo. Wie geht es dir?"

# Save the spoken text to an audio file
engine.save_to_file(text, 'output.mp3')

# Disconnect the TTS engine
engine.stop()
