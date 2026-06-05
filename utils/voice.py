import pyttsx3
import threading
from gtts import gTTS
import os
import tempfile
import subprocess


def speak(text: str, rate: int = 175, volume: float = 1.0, gender: str = "female"):
    """Lit un texte a voix haute."""

    if gender == "male":
        # Youssef — voix française Google (gTTS)
        def _speak_gtts():
            try:
                clean_text = text.replace('*', '').replace('#', '').replace('`', '')
                tts = gTTS(text=clean_text[:500], lang='fr', slow=False)
                tmp_file = tempfile.NamedTemporaryFile(
                    delete=False, suffix='.mp3', dir=os.path.expanduser('~')
                )
                tmp_file.close()
                tts.save(tmp_file.name)

                # Lire avec PowerShell wmplayer
                cmd = f'powershell -c "Add-Type -AssemblyName presentationCore; $mp = New-Object system.windows.media.mediaplayer; $mp.open([uri]\\"{tmp_file.name}\\"); $mp.Play(); Start-Sleep -s 8; $mp.Stop()"'
                subprocess.run(cmd, shell=True, capture_output=True)
                
                try:
                    os.unlink(tmp_file.name)
                except:
                    pass

            except Exception as e:
                print(f"Erreur voix: {e}")

        thread = threading.Thread(target=_speak_gtts)
        thread.daemon = True
        thread.start()

    else:
        # Karima — voix Hortense (français Windows)
        def _speak_pyttsx3():
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[3].id)
            engine.setProperty('rate', rate)
            engine.setProperty('volume', volume)
            clean_text = text.replace('*', '').replace('#', '').replace('`', '')
            engine.say(clean_text)
            engine.runAndWait()
            engine.stop()

        thread = threading.Thread(target=_speak_pyttsx3)
        thread.daemon = True
        thread.start()