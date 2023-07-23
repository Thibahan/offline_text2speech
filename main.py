import pyttsx3

# One time initialization
engine = pyttsx3.init()

engine.setProperty('voice', "german")
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

text = "Hallo. Wie geht es dir? Mir geht es gut!"

# Save the spoken text to an audio file
engine.save_to_file(text, 'output.flac')

# Run engine
engine.runAndWait()

# Disconnect the TTS engine
engine.stop()
