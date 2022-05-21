import json
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
season = os.getenv("SEASON")

# files = [
#         # "wordCountByFreq.json",
#         # "wordCountNoStopwords.json",
#         # "wordCount.json"
# ]

# with open("./Jsons/"+files[0],'r') as f:
#     frequency = json.load(f)

# frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:100]


# with open("./Jsons/"+files[1],'r') as f:
#     stopwords = json.load(f)

# stopwords = sorted(stopwords.items(), key=lambda item: item[1], reverse=True)[:100]

# with open("./Jsons/"+files[2],'r') as f:
#     unfiltered = json.load(f)

# unfiltered= sorted(unfiltered.items(), key=lambda item: item[1], reverse=True)[:100]

# print("|Number|Filtered By Frequency|Count|Filtered By Stopword|Count|Unfiltered|Count|")
# print("|:-|:-|:-|:-|:-|:-|:-|")
# for i, j, k, l in zip(frequency,stopwords,unfiltered,range(1,101)):
#     print(f'|{l}|{i[0].capitalize()}|{i[1]}|{j[0].capitalize()}|{j[1]}|{k[0].capitalize()}|{k[1]}|')

files = [
        "TrashTasteWordCountFiltered.json",
        "TrashTasteStreamsWordCountFiltered.json",
        "TrashTasteWordCount.json",
        "TrashTasteStreamsWordCount.json",
]

with open(f"./Jsons/Season {season}/"+files[0],'r') as f:
    trashTasteFiltered = json.load(f)

trashTasteFiltered = sorted(trashTasteFiltered.items(), key=lambda item: item[1], reverse=True)[:100]


with open(f"./Jsons/Season {season}/"+files[1],'r') as f:
    afterDarkFiltered = json.load(f)

afterDarkFiltered = sorted(afterDarkFiltered.items(), key=lambda item: item[1], reverse=True)[:100]

with open(f"./Jsons/Season {season}/"+files[2],'r') as f:
    trashTasteUnfiltered = json.load(f)

trashTasteUnfiltered= sorted(trashTasteUnfiltered.items(), key=lambda item: item[1], reverse=True)[:100]

with open(f"./Jsons/Season {season}/"+files[3],'r') as f:
    afterDarkUnfiltered = json.load(f)

afterDarkUnfiltered= sorted(afterDarkUnfiltered.items(), key=lambda item: item[1], reverse=True)[:100]


print("|Number|Trash Taste Filtered|Count|After Dark Filtered|Count|Trash Taste Unfiltered|Count|After Dark Unfiltered|Count|")
print("|:-|:-|:-|:-|:-|:-|:-|:-|:-|")
for i, j, k, l, m in zip(trashTasteFiltered,afterDarkFiltered,trashTasteUnfiltered,afterDarkUnfiltered,range(1,101)):
    print(f'|{m}|{i[0].capitalize()}|{i[1]}|{j[0].capitalize()}|{j[1]}|{k[0].capitalize()}|{k[1]}|{l[0].capitalize()}|{l[1]}|')
