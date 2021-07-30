import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")

        # recognize speech using google

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")

        except Exception as e:
            print("Error :  " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()

# https://geekscoders.com/python-speech-recognition-tutorial-for-beginners/
#     In here we have created the object of our Recognizer and also we are using Microphone

# as source.

# r = sr.Recognizer()
# 1
# r = sr.Recognizer()


# also we need to add this line of code, it is used for removing noises if we have in the sound.

# r.adjust_for_ambient_noise(source)
# 1
# r.adjust_for_ambient_noise(source)


# And in here we are recognizing the speech using Google Speech.

#  print("You have said \n" + r.recognize_google(audio))
# 1
#  print("You have said \n" + r.recognize_google(audio))


# If you need to record your audio than you can use this code.

#  with open("recorded.wav", "wb") as f:
#             f.write(audio.get_wav_data())
# 1
# 2
#  with open("recorded.wav", "wb") as f:
#             f.write(audio.get_wav_data())
