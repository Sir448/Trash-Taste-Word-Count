# Trash-Taste-Word-Count

This series of scripts displays the frequency at which words are spoken on the YouTube channels Trash Taste and Trash Taste After Dark

### Counting Words
[CountWords.py](CountWords.py) creates a jsons for the word count of every word said. It does so by scanning the subtitles in the YouTube video.
When no subtitles are available, it downloads the audio then uses Google's Web Speech API to scan the words said.
Although it's functional, it doesn't work particularly well.
This function is in [ScanAudio.py](ScanAudio.py).
You can change the channels variable to decide which channels to scan. You can choose to scan on of or both of them.
It writes to different files so running the script again for a different setting won't overwrite the previous file.

### Filtering words
I decided to filter the words because otherwise you get many "mundane" words that make for an uninteresting presentation.
(i.e. Like, I, And, etc.)

[FilterWordsByFreq.py](FilterWordsByFreq.py) takes the first 50 words filtered by the frequency of which the word is used in the English language based on the wordfreq library.
It filters out anything with a frequency above 0.000214. I chose this number because that is the frequency of the word "f\*\*\*\*\*\*" and I thought that word should be included. 

[FilterStopwords.py](FilterStopwords.py) takes the first 50 words after filtering out all the stopwords.
Stopwords, as you might have guessed, are the mundane words I mentioned earlier.
I use two different libraries (nltk and gensim) to filter out stopwords.
I was also going to use the spaCy library but it was loading tensorflow (a machine learning library) which I thought was unnecessary.

My first attempt was filtering out stopwords, but that still left a lot of words that I didn't want, so I think filtering by frequency overall gives better results since I can tune it to my preferences.

After using both filtering methods, a total of 9 jsons are created.
Each is a different combination of the different channels (Trash Taste, Trash Taste After Dark, or Both) and filtering method (By Frequency, By Stopword, Unfiltered).

### Creating graphs
[CreateGraph.py](CreateGraph.py) uses all 9 of the jsons to create and save a separate graph for each json using the matplotlib library.

### Graphs

![wordCountByFreq](https://user-images.githubusercontent.com/71520681/120131486-c7184600-c185-11eb-8fba-e0e2a4d83249.png)

![TrashTasteStreamsWordCountByFreq](https://user-images.githubusercontent.com/71520681/120131522-d4cdcb80-c185-11eb-9845-6d147e36604a.png)

![TrashTasteWordCountByFreq](https://user-images.githubusercontent.com/71520681/120131510-cf708100-c185-11eb-95bd-3f496e41d2c5.png)

![wordCountNoStopwords](https://user-images.githubusercontent.com/71520681/120131548-e1eaba80-c185-11eb-8e85-a055d369f5da.png)

![TrashTasteStreamsWordCountNoStopwords](https://user-images.githubusercontent.com/71520681/120131555-e4e5ab00-c185-11eb-9add-70fe35811343.png)

![TrashTasteWordCountNoStopwords](https://user-images.githubusercontent.com/71520681/120131562-e6af6e80-c185-11eb-910a-ab6062734c57.png)

![wordCount](https://user-images.githubusercontent.com/71520681/120131567-e8793200-c185-11eb-9ec1-f05e8ae5b1c4.png)

![TrashTasteStreamsWordCount](https://user-images.githubusercontent.com/71520681/120131576-ee6f1300-c185-11eb-98ec-ade708ec6ea1.png)

![TrashTasteWordCount](https://user-images.githubusercontent.com/71520681/120131571-eb742280-c185-11eb-871f-799ebe2ec9ab.png)
