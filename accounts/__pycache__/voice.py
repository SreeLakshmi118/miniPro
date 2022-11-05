import speech_recognition as s


sr=s.Recognizer()

with s.Microphone() as source:
    print("IRIS is listening....")
    audio=sr.listen(source)

    try:
        text=sr.recognize_google(audio)
        print(text)

    except:
        print("cannot recognize")
