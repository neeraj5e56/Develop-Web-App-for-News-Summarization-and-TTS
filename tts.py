from gtts import gTTS
import os

def generate_tts(text, language="hi"):
    tts = gTTS(text, lang=language)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Play the audio (Windows)
    # For macOS/Linux, use: os.system("afplay output.mp3")

# Test TTS
if __name__ == "__main__":
    text = input("Enter text: ")
    generate_tts(text)