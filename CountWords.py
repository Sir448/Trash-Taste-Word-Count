from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
import json

# from ScanAudio import scan_audio

pp = pprint.PrettyPrinter()

# Trash Taste Channel ID
# UCcmxOGYGF51T1XsqQLewGtQ
# Trash Taste After Dark Channel ID
# UCKaN3mt53ATqRjzalb2ALFQ

channelIds = ["UCcmxOGYGF51T1XsqQLewGtQ","UCKaN3mt53ATqRjzalb2ALFQ"]

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = os.getenv("TOKEN")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
api_key = os.getenv("API_KEY")

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = api_key)

wordCount = {}

nextPageToken = None

channels = 2
# 0 for only Trash Taste
# 1 for both
# 2 for only Trash Taste After Dark

season = os.getenv("SEASON")

for channelId in channelIds[max(0,channels-1):channels+1]:
    # while True: # While loop to loop through all pages
    for o in range(2): # Only get the season 2 videos
        # Get search result
        request = youtube.search().list(
                    part="id,snippet",
                    maxResults=50 if o == 0 else 2, # Only get the season 2 videos
                    # maxResults=50,
                    type="video",
                    channelId=channelId,
                    order="date",
                    pageToken=nextPageToken
                )
        response = request.execute()


        for i in response['items']:
            print(i['snippet']['title'])
            # Get dict of words
            script = ""
            try:
                # Get the transcript of a specific video
                transcript = YouTubeTranscriptApi.get_transcript(i['id']['videoId'])

                # Put all dialogue in one string
                for j in transcript:
                    script += j['text']+" "

            except TranscriptsDisabled:
                print("Subtitles disabled, skipping video")
                continue # For testing purposes, scanning the audio in the video takes too long, I might remove this but I think I'd rather wait for them to add subtitles to the most recent video
                # Scans the audio when there are no subtitles on the video
                # script = scan_audio(i['id']['videoId'])

            # Remove punctuation
            script = script.replace(".","").replace(",","").replace("?","").replace("!","").replace("-","").replace(";","")

            # Split into a list of characters for processing
            words = list(script)

            # Filter out quotation marks
            words = list(filter(("\"").__ne__,words))

            # Remove brackets and any words in them
            openBrackets = [i for i, x in enumerate(words) if (x == "(" or x == "[")]
            closeBrackets = [i for i, x in enumerate(words) if (x == ")" or x == "]")]
            for start, end in zip(openBrackets[::-1],closeBrackets[::-1]):
                del words[start:end+1]

            # Remove any anything between an apostraphe and the end of the word
            # If there is an n before the apostraphe, just leave it, this includes words like don't or wasn't
            # I chose to do this because otherwise it would create words like don and wasn
            # I could very easily have just taken out the n as well but if feel like negative words change the meaning enough for it to be it's own word anyways
            # i.e. don't vs do is more different than I've vs I (if that makes sense)
            # Regardless, when I filter the results later, all of these words are going to be filtered out anyways so it only really matters for the raw data
            apostraphes = [i for i, x in enumerate(words) if (x == "'" and words[i-1] != 'n')]
            for j in apostraphes[::-1]:
                del words[j:words.index(" ",j)]
            
            # Recombine characters into a string, make it all lowercase, then split by spaces
            words = "".join(words).lower().split()

            # Add to word count
            for j in words:
                if j in wordCount.keys():
                    wordCount[j] += 1
                else:
                    wordCount[j] = 1

        # Go to next page or finish
        if "nextPageToken" in response.keys():
            nextPageToken = response["nextPageToken"]
        else:
            nextPageToken = None
            break

# Choosing name of outfile
outfile = "wordCount.json"
if channels == 0:
    outfile = "TrashTasteW" + outfile[1:]
if channels == 2:
    outfile = "TrashTasteStreamsW" + outfile[1:]

# Write to json
with open(f"./Jsons/Season {season}/{outfile}","w") as f:
    json.dump(wordCount,f)


