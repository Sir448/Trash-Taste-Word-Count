
import json
from wordfreq import word_frequency

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
# I chose 0.000215 because the word "f******" has a frequency 0.000214
filteredWords = []
for i in orderedWords:
    if word_frequency(i[0],'en') < 0.000215:
        filteredWords.append(i)
    if len(filteredWords) >= 100:
        break

# Save to json
filteredWordCount = {key: value for (key, value) in filteredWords}
with open('./Jsons/'+filename+'ByFreq.json','w') as f:
    json.dump(filteredWordCount,f)