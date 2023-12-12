import speech_recognition as sr


def get_speech_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")
    return ""
