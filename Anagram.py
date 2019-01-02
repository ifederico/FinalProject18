#supplied with a word and identify anagrams to that word
#easy and hard levels based on amount of letters
#hint based on the definition of the anagram listed
#    ex. "cinema" *there are 2 anagrams*
#    listing how many anagrams there are; part of difficulty or choose anagrams that have a single anagram
#25 words per level
#4 letters per anagram in easy mode
#6 or more per anagram in hard mode

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
    def __init__(self,rounds,guesses,anagram):
        self.rounds = rounds
        self.guesses = guesses
        self.anagram = anagram

    #while rounds > 0:
        #if rounds = 0:
            #end_game()





    def end_game(self):
        "'All ten rounds of a level are completed.'"



class Game_Basics(Easy):
    "'Game rules for easy level'"
    def __init__(self):
        self.

#easy words
word1 = ['deaf'fade,'dice'iced,'disk'kids/skid,'sole'lose,
'golf'flog,'fuel'flue,'grab'brag/garb,'gulp'plug,'fowl'wolf/flow,'dear'read/dare,'snag'nags,'mean'amen/mane/name,
'note'tone,'pace'cape,'pale'leap/peal/plea,'race'care/acre,'reef'free,'ring'grin,'silo'soil/oils,'step'pets/pest]

word1 = random.choice(word1)

def point_escore():
        "'Tracks the points earned from each easy round.'"



class Game_Basics(Hard):
    "'Game rules for hard level'"
    def __init__(self):
        self.

#hard words
word2 = ['cinema'iceman/anemic,'except'expect,'recede'decree,'friend'finder,
'grease'agrees,'incept'pectin,'leader'dealer,'marine'airmen/remain,'meteor'remote,'oceans'canoes,'sniper'ripens,'hustle'sleuth,
'fringe'finger,'impart'armpit,'listen'silent/enlist/tinsel/inlets,'manors'ransom,'plates'palest/pastel/petals/pleats/staple,
'potion'option,'resins'rinses/sirens,'rustic'citrus]

word2 = random.choice(word2)

def point_hscore():
    "'Tracks the points earned from each hard round.'"
