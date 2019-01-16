import random
import sys

chosen_word = ""

class Game_Basics:
    "'Generic game basics'"
    def __init__(self,rounds,guesses,anagram,points,time,difficulty,easy,hard):
        self.rounds = rounds
        self.guesses = guesses
        self.anagram = anagram
        self.points = points
        self.time = time
        self.difficulty = difficulty
        self.easy = easy
        self.hard = hard
        self.word = ""

    #e_dict = {track: 0, points: 5, time: 120}
    #h_dict = {track: 0, points: 10, time: 60}

# def random_word():
#     "'Chooses random word from each level list.'"
#     if difficulty == easy:
#         word1 = random.choice(easy_words)
#         print(f"Word: {word1}")
#         guesses = print("Anagram?")
#     else:
#         word2 = random.choice(hard_words)
#         print(f"Word: {word2}")
#         guesses = print("Anagram?")

def random_word(dict_to_choose_from):
    """Choose random word from specified level list"""
    word = random.choice(list(dict_to_choose_from.keys()))
    print(f"Word: {word}")
    return word

def anagram_guess():
    "'Determines if your guesses were correct.'"
    for anagram in word:
        if anagram in guesses:
            print("Already Tried! Another...")
        if anagram == True:
            correct = ["Nice choice!", "You're on FIRE!", "You're on a roll, no time to waste!"]
            print(f"{random.choice(correct)} {guesses} is CORRECT!")
        if anagram not in word:
            print("That's Not a Word! Keep Guessing, Turns are Unlimited!")

def point_score():
    "'Track the amount of points earned in the game.'"
    if difficulty == easy:
        if anagram == True:
            track += 1
            points += 5
    else:
        if anagram == True:
            track += 1
            points += 10
    return random_word()

def end_game(self):
    "'All ten rounds of a level are completed.'"
    if rounds == 0:
        print("You've reached the end!")
    return point_track

#easy
easy_words = {'deaf':'fade','dice':'iced','disk':'kids'and'skid','sole':'lose','golf':'flog','fuel':'flue','grab':'brag'and'garb',
'gulp':'plug','fowl':'wolf'and'flow','dear':'read'and'dare','snag':'nags','mean':'amen'and'mane'and'name','note':'tone','pace':'cape',
'pale':'peal'and'plea'and'leap','race':'care'and'acre','reef':'free','ring':'grin','silo':'soil'and'oils','step':'pets'and'pest'}

#hard
hard_words = {'cinema':'iceman'and'anemic','except':'expect','recede':'decree','friend':'finder','grease':'agrees','incept':'pectin',
'leader':'dealer','marine':'airmen'and'remain','meteor':'remote','oceans':'canoes','sniper':'ripens','hustle':'sleuth','fringe':'finger',
'impart':'armpit','listen':'silent'and'enlist'and'tinsel'and'inlets','manors':'ransom','plates':'palest'and'pastel'and'petals'and'pleats'and'staple',
'potion':'option','resins':'rinses'and'sirens','rustic':'citrus'}


input1 = input("Welcome to Fanagrams! Get it? Cuz the creator is a 'fan' of 'anagrams'! AHAHA I'm too much.... You're probably thinking, what even are anagrams? If you want to play, type 'c' for continue. If not, type 'n' for nope.")
while input1 not in ['c', 'n']:
  input1 = input("If you want to play, type 'c' for continue. If not, type 'n' for nope.")
if input1 == 'c':
  print("Anagrams are the rearrangements of letters from a word to create another word. It's simple word play at its best!")
  print("Fanagrams is designed with two levels: Easy and Hard")
  print("Easy consists of 4 letter words while Hard consists of 6 letter words. You get the option to choose either level!")
input2 = input("So what will it be, Easy or Hard?")
while input2 not in ['easy','hard']:
  input2 = input("So what will it be Easy or Hard?")
if input2 == 'easy':
  print("To play, you must think of an anagram per word (of ten words) in fifteen seconds! Don't worry if you're stumped, I'll hint you once to put you in the right direction!")
  print("P.S. Some of the words may have several anagrams and each hint will be specific to one option. ARE YOU READY?")
  chosen_word = random_word(easy_words)
elif input2 == 'hard':
  print("To play, you must think of an anagram per word (of ten words) in ten seconds! Don't worry if you're stumped, I'll hint you once to put you in the right direction!")
  print("P.S. Some of the words may have several anagrams and each hint will be specific to one option. ARE YOU READY?")
  chosen_word = random_word(hard_words)
if input1 == 'n':
  sys.exit()
