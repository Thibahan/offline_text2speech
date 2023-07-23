import pyttsx3


def get_language_id(language):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        language_in_languages = language.lower() in ' '.join(voice.languages).lower()
        language_in_name = language.lower() in voice.name.lower()
        
        if language_in_languages or language_in_name:
            return voice.id
    engine.stop()
    return None
        