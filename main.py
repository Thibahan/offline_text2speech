import pyttsx3
from utils import get_language_id



def create_file(text, language="german",
                rate= 150, volume= 0.9,
                output_file="output.flac"):
    language_id = get_language_id(language)

    # One time initialization
    engine = pyttsx3.init()

    # Set properties voice, speed and volume
    engine.setProperty('voice', language_id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Save the spoken text to an audio file
    engine.save_to_file(text, output_file)

    # Run engine
    engine.runAndWait()

    # Disconnect the TTS engine
    engine.stop()


if __name__ == '__main__':
    text = "Hallo, wie gehts?"
    create_file(text)