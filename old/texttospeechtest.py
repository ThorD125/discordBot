from gtts import gTTS
from io import BytesIO
import pygame


def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')

    # Save the speech to a BytesIO object
    speech_buffer = BytesIO()
    tts.write_to_fp(speech_buffer)
    speech_buffer.seek(0)

    # Initialize Pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(speech_buffer)

    # Play the speech
    pygame.mixer.music.play()

    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        pass


text = "Hello, I am a text-to-speech example in Python."
text_to_speech(text)
