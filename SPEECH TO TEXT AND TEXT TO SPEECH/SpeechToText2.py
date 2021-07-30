import speech_recognition as sr
from os import path
from pydub import AudioSegment


def main():

    # files
    # src = "recorded.mp3"
    # dst = "test.wav"
    #
    # # convert wav to mp3
    # sound = AudioSegment.from_mp3(src)
    # sound.export(dst, format="wav")

    sound = "conv.wav"

    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print("Converting Audio To Text ..... ")

        audio = r.listen(source)

    try:
        print("Converted Audio Is : \n" + r.recognize_google(audio))

    except Exception as e:
        print("Error {} : ".format(e))


if __name__ == "__main__":
    main()
