import json
from nltk.corpus import stopwords
import gensim

channels = 2

# Choose filename
filename = "wordCount"
if channels == 0:
    filename = "TrashTasteW" + filename[1:]
if channels == 2:
    filename = "TrashTasteStreamsW" + filename[1:]

# Load Word Count
with open('./Jsons/'+filename+'.json','r') as f:
    data = json.load(f)

# Create list of tuples (word, count) in order of count
orderedWords = sorted(data.items(), key=lambda item: item[1], reverse=True)

# Filters words by word frequency
# Used two lists of stopwords to cut down as many as possible
# I didn't want to use spacy because it loads tensorflow for whatever reason
filteredWords = []
for i in orderedWords:
    if i[0] not in stopwords.words() and i[0] not in gensim.parsing.preprocessing.STOPWORDS:
        filteredWords.append(i)
    if len(filteredWords) >= 100:
        break
    
# Save to json
filteredWordCount = {key: value for (key, value) in filteredWords}
with open('./Jsons/'+filename+'NoStopwords.json','w') as f:
    json.dump(filteredWordCount,f)