import pyttsx3


def get_language_id(language: str) -> str:
    """This function will return the id of the language package.
    It will search in the language packages of the operating system in the name and laguages
    attributes.

    Args:
        language (str): Language to get the ID of.

    Returns:
        str: ID of the language. Will return None, if language not found.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        language_in_languages = language.lower() in ' '.join(voice.languages).lower()
        language_in_name = language.lower() in voice.name.lower()
        
        if language_in_languages or language_in_name:
            return voice.id
    engine.stop()
    return None
        