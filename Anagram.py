import random
import sys

anagram_choice = ""
rounds = 1
points = 0
s = 1

class Game_Basics:
    """Generic game basics"""
    def __init__(self,difficulty):
        #self.rounds = 10
        #self.guesses = ""
        #self.points = 0
        self.difficulty = difficulty

        if difficulty == 'easy':
            self.words = {'deaf':['fade'],'dice':['iced'],'disk':['kids','skid'],'sole':['lose'],'golf':['flog'],'fuel':['flue'],'grab':['brag','garb'],
        'gulp':['plug'],'fowl':['wolf','flow'],'dear':['read','dare'],'snag':['nags'],'mean':['amen','mane','name'],'note':['tone'],'pace':['cape'],
        'pale':['peal','plea','leap'],'race':['care','acre'],'reef':['free'],'ring':['grin'],'silo':['soil','oils'],'step':['pets','pest']}

        elif difficulty == 'hard':
            self.words = {'cinema':['iceman','anemic'],'except':['expect'],'recede':['decree'],'friend':['finder'],'grease':['agrees'],'incept':['pectin'],
        'leader':['dealer'],'marine':['airmen','remain'],'meteor':['remote'],'oceans':['canoes'],'sniper':['ripens'],'hustle':['sleuth'],'fringe':['finger'],
        'impart':['armpit'],'listen':['silent','enlist','tinsel','inlets'],'manors':['ransom'],'plates':['palest','pastel','petals','pleats','staple'],
        'potion':['option'],'resins':['rinses','sirens'],'rustic':['citrus','curist']}

        self.word = ""

    def intro(self):
        print("To play, you must think of an anagram per word (of ten words). You will have 3 guesses per round! ARE YOU READY?")
        input("Press ENTER to continue......")

    def random_word(self):
        """Choose random word from specified level list"""
        self.word = random.choice(list(self.words.keys()))
        return self.word

    def anagram_guess(self):
        """Determines if your guesses were correct"""
        guess_count = 2
        global s
        correct_choice = self.words[self.word]
        print("---------")
        print(f"Round {rounds}")
        print(f"Word: {self.word}\n")
        anagram_choice = input("Anagram: ").lower()
        print(" ")
        print(" ")
        while anagram_choice not in correct_choice and guess_count > 0:
            print(f"That's Not a Word! Keep Guessing, Guesses Left = {guess_count}!")
            print(f"Word: {self.word}\n")
            anagram_choice = input("Anagram: ").lower()
            guess_count -= 1
        if anagram_choice in correct_choice:
            correct = ["Nice choice!", "You're on FIRE!", "You're on a roll, no time to waste!"]
            print(f"{random.choice(correct)} {anagram_choice} is CORRECT!")
            s = 1
        if anagram_choice not in correct_choice:
            s = 0
            print("Sorry, you exceeded your 3 guesses. Next Round...")
            print(" ")
        return s

input1 = input("Welcome to Fanagrams! Get it? Cuz the creator is a 'fan' of 'anagrams'! AHAHA I'm too much.... You're probably thinking, what even are anagrams? If you want to play, type 'c' for continue. If not, type 'n' for nope. ").lower()
while input1 not in ['c', 'n']:
  input1 = input("If you want to play, type 'c' for continue. If not, type 'n' for nope. ").lower()
if input1 == 'n':
  sys.exit()
if input1 == 'c':
  print(" ")
  print("Anagrams are the rearrangements of letters from a word to create another word. It's simple word play at its best!")
  print("Fanagrams is designed with two levels: Easy and Hard")
  print("Easy consists of 4 letter words while Hard consists of 6 letter words. You get the option to choose either level!")
input2 = input("So what will it be, Easy or Hard? ").lower()
while input2 not in ['easy','hard']:
  input2 = input("So what will it be Easy or Hard? ").lower()
print(" ")

game = Game_Basics(input2)
game.intro()
while rounds != 11:
    game.random_word()
    game.anagram_guess()
    rounds += 1
    if s == 1:
        if input2 == "easy":
            points += 5
        if input2 == "hard":
            points += 10
    elif s == 0:
        print(f"You have {points} Total Points, so far!")
    del game.words[game.word]

if rounds == 11:
    print("You've reached the end!")
    if input2 == "easy":
        print(f"You got {points} out of 50 points!")
    if input2 == "hard":
        print(f"You got {points} out of 100 points!")
    print(" ")
    print("Shoutout to those who helped in the making of this game: Omay, Nikki, and Mrs. Gerstein! :)")
