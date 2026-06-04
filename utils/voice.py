import pyttsx3
import threading


def speak(text: str, rate: int = 175, volume: float = 1.0, gender: str = "female"):
    """Lit un texte a voix haute."""
    def _speak():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if gender == "male":
            # Microsoft David — voix masculine
            engine.setProperty('voice', voices[0].id)
        else:
            # Microsoft Hortense — voix française feminine
            engine.setProperty('voice', voices[3].id)

        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        clean_text = text.replace('*', '').replace('#', '').replace('`', '')
        engine.say(clean_text)
        engine.runAndWait()
        engine.stop()

    thread = threading.Thread(target=_speak)
    thread.daemon = True
    thread.start()