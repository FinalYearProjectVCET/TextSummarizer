from gtts import gTTS

tts = gTTS(text="Good Afternoon To One and All Present Here", lang='en')
tts.save("record.wav")
print("Text Converted Successfuplly ")
