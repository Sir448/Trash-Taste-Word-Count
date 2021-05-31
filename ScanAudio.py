import speech_recognition as sr
from speech_recognition import UnknownValueError
import youtube_dl
from os import path,remove
from pydub import AudioSegment
import subprocess
import librosa
from math import ceil

filePath = "D:/Python Scripts/VideoScan/TrashTasteAudio"

def scan_audio(videoId):

    # Delete exisiting audio file
    if path.exists(filePath+".wav"):
        remove(filePath+".wav")

    ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': filePath+".webm",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
            }

    # Downloads audio and converts to wav (necessary for speech-to-text)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={videoId}\n'])


    # Set up recognizer
    r = sr.Recognizer()

    # Prep audio segments
    theBoys = sr.AudioFile(filePath+".wav")
    segments = ceil(librosa.get_duration(filename='./test.wav')/60)
    audio = []
    print("Splitting audio source")
    with theBoys as source:
        for _ in range(segments):
            audio.append(r.record(source,duration=60))

    # Scans audio segments
    print("Starting to scan audio segments")
    words = ""
    for i,x in enumerate(audio):
        print(f'On segment {i+1} of {segments}')
        try:
            words += r.recognize_google(x) + " "
        except:
            print(f'Skipped segment {i+1}')

    # Censored word filter
    def censored(word):
        return "*" not in word

    # Filters out censored word
    words = " ".join(list(filter(censored,words.split())))

    return words
