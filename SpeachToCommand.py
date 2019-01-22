import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, 5)
    print("Say something!")
    audio = r.listen(source, phrase_time_limit=5)
    print('Got it! Now to Recognise it')
        
 # recognize speech using Google Speech Recognition
 try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recog_results = r.recognize_google(audio, show_all=True)
    trans = recog_results['alternative'].values()
    print("Google Speech Recognition thinks you said ")
    for i in trans:
    print(i)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
        