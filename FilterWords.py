
import json
from wordfreq import word_frequency
from nltk.corpus import stopwords
import gensim
from myStopwords import myStopwords
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

channels = 2
season = os.getenv("SEASON")

# Choose filename
filename = "wordCount"
if channels == 0:
    filename = "TrashTasteW" + filename[1:]
if channels == 2:
    filename = "TrashTasteStreamsW" + filename[1:]

# Load Word Count
with open(f'./Jsons/Season {season}/{filename}.json','r') as f:
    data = json.load(f)

# Create list of tuples (word, count) in order of count
orderedWords = sorted(data.items(), key=lambda item: item[1], reverse=True)

# Filters words by word frequency
# I used to use 0.000215 because the word "f******" has a frequency 0.000214
# This time I chose 0.000303 because the word "shit" has a frequency of 0.000302
filteredWords = []
for i in orderedWords:
    if word_frequency(i[0],'en') < 0.000303 and i[0] not in stopwords.words() and i[0] not in gensim.parsing.preprocessing.STOPWORDS and i[0] not in myStopwords:
        filteredWords.append(i)
    if len(filteredWords) >= 100:
        break

# Save to json
filteredWordCount = {key: value for (key, value) in filteredWords}
with open(f'./Jsons/Season {season}/{filename}Filtered.json','w') as f:
    json.dump(filteredWordCount,f)