import pyttsx3
from utils import get_language_id
import os



def create_file(text: str, language="german", rate= 150, volume= 0.9,
                output_file="output.flac") -> str:
    """This function will create an audio file with the input text in as speech.

    Args:
        text (str): Text that should be conveterd to speech.
        language (str, optional): Language of the text. Defaults to "german".
        rate (int, optional): Speed of the text. Defaults to 150.
        volume (float, optional): Volume of the text. Defaults to 0.9.
        output_file (str, optional): Outputfile path with audio file extension. Defaults to "output.flac".

    Returns:
        str: Absolute path to output file.
    """
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
    return os.path.abspath(output_file)


if __name__ == '__main__':
    text = "Hallo, wie gehts?"
    path = create_file(text)
    print(path)