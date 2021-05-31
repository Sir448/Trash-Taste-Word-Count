
import matplotlib.pyplot as plt
import numpy as np
import json

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
]


for fileNumber in range(9):
    # Choosing file
    # fileNumber = 0
    # filename = "./Jsons/"+files[fileNumber]
    filename = files[fileNumber]

    # Setting labels
    suptitle = "Frequency of Words Spoken By The Bois "

    if fileNumber % 3 == 0:
        suptitle += "(Trash Taste and Streams)"
    elif fileNumber % 3 == 1:
        suptitle += "(Trash Taste)"
    elif fileNumber % 3 == 2:
        suptitle += "(Streams)"

    title = "Filtered by "

    if fileNumber < 3:
        title += "Frequency"
    elif fileNumber < 6:
        title += "Stopwords"
    else:
        title = "Unfiltered"

    # Load json
    with open("./Jsons/"+filename, 'r') as f:
        data = json.load(f) 

    # Sort the data by word count
    # I think it's already sorted but this is just to make sure
    sortedData = sorted(data.items(), key=lambda item: item[1], reverse=True)[:50]


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
    fig.savefig("./Graphs/"+filename[:-4]+"png")

