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
