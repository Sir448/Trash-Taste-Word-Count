
import matplotlib.pyplot as plt
import numpy as np
import json
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# List of files
# Note: If you're trying to follow the code, you'll notice that this is the first reference to some of these files
#       That's because I manually renamed them and I don't think it's worth writing code for them to be automatically name
files = [
        "wordCountByFreq.json", # 0
        "TrashTasteWordCountByFreq.json", # 1
        "TrashTasteStreamsWordCountByFreq.json", # 2
        "wordCountNoStopwords.json", # 3
        "TrashTasteWordCountNoStopwords.json", # 4
        "TrashTasteStreamsWordCountNoStopwords.json", # 5
        "wordCount.json", # 6
        "TrashTasteWordCount.json", # 7
        "TrashTasteStreamsWordCount.json", # 8
        "TrashTasteWordCountFiltered.json", # 9
        "TrashTasteStreamsWordCountFiltered.json" # 10
]

numberOfWords = 50
season = os.getenv("SEASON")


for fileNumber in range(11):
    if fileNumber not in {7,8,9,10}: 
        #This year I'm only doing four graphs and I'm too lazy to change my code a lot
        continue
    # Choosing file
    # fileNumber = 0
    # filename = "./Jsons/"+files[fileNumber]
    filename = files[fileNumber]

    # Setting labels
    suptitle = f'Top {numberOfWords} Words Spoken By The Boys '

    if fileNumber in {7,9}:
        suptitle += "(Trash Taste)"
    else:
        suptitle += "(After Dark)"
    
    # if fileNumber % 3 == 0:
    #     suptitle += "(Trash Taste and Streams)"
    # elif fileNumber % 3 == 1:
    #     suptitle += "(Trash Taste)"
    # elif fileNumber % 3 == 2:
    #     suptitle += "(Streams)"

    title = ""
    
    if fileNumber in {7,8}:
        title = "Unfiltered"
    else:
        title = "Filtered"

    # if fileNumber < 3:
    #     title += "Frequency"
    # elif fileNumber < 6:
    #     title += "Stopwords"
    # else:
    #     title = "Unfiltered"

    # Load json
    with open(f"./Jsons/Season {season}/"+filename, 'r') as f:
        data = json.load(f) 

    # Sort the data by word count
    # I think it's already sorted but this is just to make sure
    sortedData = sorted(data.items(), key=lambda item: item[1], reverse=True)[:numberOfWords]
    # print(sortedData)

    # quit()
    # Creates separated (but still sorted) lists for the words and counts
    # Also capitalizes all the words
    words = [key.capitalize() for (key,value) in sortedData]
    count = [value for (key,value) in sortedData]


    # Creates the graph
    # If I'm being honest, I'm not a wizard with matplotlib so I barely understand what this does
    fig = plt.figure(figsize=(18,15))
    ax = fig.add_axes([0.1,0.12,0.8,0.8])
    ax.bar(words,count,width=1)
    plt.bar(np.arange(len(count)),count,width = 1, color = ['#8cddff','#66d1ff'])
    plt.xticks(rotation = -70)
    plt.xlabel("Words")
    plt.ylabel("Number of times said")
    plt.suptitle(suptitle,fontsize=14)
    plt.title(title,fontsize=12)
    fig.savefig(f"./Graphs/Season {season}/"+filename[:-4]+"png")

