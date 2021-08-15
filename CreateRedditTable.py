import json

files = [
        "wordCountByFreq.json",
        "wordCountNoStopwords.json",
        "wordCount.json"
]

with open("./Jsons/"+files[0],'r') as f:
    frequency = json.load(f)

frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:100]


with open("./Jsons/"+files[1],'r') as f:
    stopwords = json.load(f)

stopwords = sorted(stopwords.items(), key=lambda item: item[1], reverse=True)[:100]

with open("./Jsons/"+files[2],'r') as f:
    unfiltered = json.load(f)

unfiltered= sorted(unfiltered.items(), key=lambda item: item[1], reverse=True)[:100]


print("|Number|Filtered By Frequency|Count|Filtered By Stopword|Count|Unfiltered|Count|")
print("|:-|:-|:-|:-|:-|:-|:-|")
for i, j, k, l in zip(frequency,stopwords,unfiltered,range(1,101)):
    print(f'|{l}|{i[0].capitalize()}|{i[1]}|{j[0].capitalize()}|{j[1]}|{k[0].capitalize()}|{k[1]}|')