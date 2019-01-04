import random
import sys

input = print("Welcome to Fanagrams! Get it? Cuz the creator is a 'fan' of 'anagrams'! AHAHA I'm too much.... You're probably thinking, what even are anagrams? If you want to play, type 'continue'. If not, type 'nope'.")
    if input = 'continue':
        print("Anagrams are the rearrangements of letters from a word to create another word. It simple word play at its best!")
        print("Fanagrams is designed with two levels: Easy and Hard")
        print("Easy consists of 4 letter words while Hard consists of 6 letter words. You get the option to choose either level!")
        input2 = print("So what will it be, Easy or Hard?")
            if input2 = 'easy'
                shift to easy mode
            else:
                shift to hard mode
        print("To play, you must think of an anagram per word (of ten words) in fifteen seconds! Don't worry if you're stumped, I'll hint you once to put you in the right direction!")
        print("P.S. Some of the words may have several anagrams and each hint will be specific to one option. Soooo...... ARE YOU READY? Type 'start'.")
    else:
        sys.exit()

    random_word():
    for anagram in word:
        if anagram in guesses:
            print("Already Tried! Another...)
        if anagram = True:
            random.choice():
                print("Nice choice!", + guesses +, " is CORRECT!")
                print("You're on FIRE!", + guesses +, "is CORRECT!")
                print("You're on a roll, no time to waste!", + guesses +, "is CORRECT!")
                failed += 1
        if anagram not in word:
            print("That's Not a Word! Keep Guessing, Turns are Unlimited!")


class Game_Basics:
    "'Generic game basics'"
    def __init__(self,rounds,guesses,anagram,points,time,difficulty):
        self.rounds = rounds
        self.guesses = guesses
        self.anagram = anagram
        self.points = points
        self.time = time

    e_dict = {track: 0, points: 5, time: 120}
    h_dict = {track: 0, points: 10, time: 60}

    def random_word():
        "'Chooses random word from each level list.'"
        if difficulty = easy:
            word1 = random.choice(word1)
            print(f"Word: {word1}")
            guesses = print("Anagram?")
        else:
            word2 = random.choice(word2)
            print(f"Word: {word2})
            guesses = print("Anagram?")

    def point_score():
        "'Tracks the amount of points earned in the game'"
        if difficulty = easy:
            if anagram = True:
                track += 1
                points += 5
        else:
            if anagram = True:
                track += 1
                points += 10
        return random_word()

    def end_game(self):
        "'All ten rounds of a level are completed.'"
        if rounds = 0:
            print("You've reached the end!")
        return point_track

#easy words
word1 = ['deaf','dice','disk','sole','golf','fuel','grab','gulp',
'fowl','dear','snag','mean','note','pace','pale','race','reef','ring','silo','step']
anagram1 = ['fade','iced','kids','skid','lose','flog','flue','brag','garb','plug','wolf','flow','read','dare','nags',
'amen','mane','name','tone','cape','leap','peal','plea','care','acre','free','grin','soil','oils','pets','pest']
anagram_pair = {'deaf':'fade','dice':'iced','disk':'kids'and'skid','sole':'lose','golf':'flog','fuel':'flue','grab':'brag'and'garb',
'gulp':'plug','fowl':'wolf'and'flow','dear':'read'and'dare','
#in process


#hard words
word2 = ['cinema','except','recede','friend','grease','incept','leader','marine',
'meteor','oceans','sniper','hustle','fringe','impart','listen','manors','plates','potion','resins','rustic']
anagram2 = ['iceman','anemic','expect','decree','finder','agrees','pectin','dealer','airmen','remain','remote','canoes','ripens','sleuth',
'finger','armpit','silent','enlist','tinsel','inlets','ransom','palest','pastel','petals','pleats','staple','option','rinses','sirens','citrus']
#in process