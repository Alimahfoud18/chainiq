import pyttsx3
import threading


def speak(text: str, rate: int = 175, volume: float = 1.0):
    """Lit un texte à voix haute."""
    def _speak():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'french' in voice.name.lower() or 'fr' in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        clean_text = text.replace('*', '').replace('#', '').replace('`', '')
        engine.say(clean_text)
        engine.runAndWait()
        engine.stop()

    thread = threading.Thread(target=_speak)
    thread.daemon = True
    thread.start()