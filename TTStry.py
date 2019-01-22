from gtts import gTTS
import winsound

tts = gTTS(text='Enter the command to move')
tts.save("inst.wav")

winsound.PlaySound('inst.wav', winsound.SND_FILENAME)
