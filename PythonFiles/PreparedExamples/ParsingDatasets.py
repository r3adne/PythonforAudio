import statistics as stats
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import csv
import time


####################################
# New concepts: 
#   csv
#   try...except(...else)
#   file i/o
#   matplotlib.pyplot



raw_songs = []
with open('billboard_lyrics.csv') as f:
    for i in range(5100): # this is how many songs are in the dataset...
        try:
            raw_songs.append(f.readline().split(','))
        except UnicodeDecodeError as err: 
            print('not sure why this error is coming up, but it should be fine.' + str(err))


# let's make sure every part of this dataset is properly input -- if there are any songs in the list songs that don't have 6 items, they are errors. I had some random error with song number 87. I have no idea why, and couldn't see any decent solution, so I just excluded it.

songs = []
for song in raw_songs:
    if len(song) != 6: 
        print('this song has the wrong number of items... filtering it out')
    elif song[0] in ['87']:
        print('this one had some weird text that I don\'t think was right...')
    else:
        songs.append(song)



for song in songs: 
    song.pop() # removes last item from song -- an int that represents the place that they got the lyrics. We don't need this. 
    
    song.append({}) # appends an empty dictionary to song -- this will store the word as a key and the number of times the word is used as a value (i.e. hello : 12) means the word 'hello' was used 12 times. 

    wordList = song[4].split(' ') # this is the list of the lyrics in the song, word by word. 

    for word in list(set(wordList)): # removes duplicates from list by using python's set data type.
        song[5][word] = wordList.count(word) # sets the dictionary values appropriately.


###### In this example, we'll analyze how often the word word_to_check was used in the songs by year. This is just one example of what we could do with the lyric data.

word_to_check = "love"
year_to_word = {}

# this sets up our dictionary to have the proper year values so that we can add to them later.
for year in range(1964, 2016):
    year_to_word[year] = 0
 
for song in songs:
    try: 
        song[5][word_to_check]
    except KeyError:
        # this means that song[5] does not have word as an index. This means the song doesn't have word_to_check in it.
        pass # pass does nothing. 
    else:
        year_to_word[int(song[3])] += song[5][word_to_check]


years = list(range(1964, 2016))
values = []
for year in years:
    values.append(year_to_word[year])

plt.plot(years, values)


plt.xlabel('year')
plt.ylabel('occurrences of {}'.format(word_to_check))
plt.title('Occurrences of {} over time'.format(word_to_check))

plt.show()