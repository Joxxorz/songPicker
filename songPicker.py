import random;
import songList;

def getUserInput():
    return raw_input('How many songs would you like displayed? ');

def countUserSongsInList():
    size = len(songList.songs);
    return size;

# find out how many songs are in the list
numberOfSongs = countUserSongsInList();
# ask user how many songs they need
userInput = getUserInput();

# check if there are enough songs in the list
if(numberOfSongs < userInput):
    print('There are too few songs to do that. Please try again.')
else:
    print('Success!');





# on user entry, generate a random number
# map that to array in external file
# print the track then repeat * user input
