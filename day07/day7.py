import random
# global variables

asciiLength = 7


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# generate a random word
def genWord():
    """Generate a random word from the list of words."""
    random.shuffle(words)
    #print(words)
    randomWord = random.choice(words)
    return randomWord

# generate dash according to the length of the word
def genDash(word):
    """Generate a string of dashes with the same length as the word."""
    dash = '-'*len(word)
    return dash

# check if the life is 0
def life(lifes):
    """life checking"""
    if lifes == 0:
        print("You lose")
        return False
    else:
        print("You have", lifes, "lives left")
        return True

# split the word & dash into a list
def splits(word,dash):
    """Split the word and dash into a list."""
    return list(word), list(dash)


# check if the guess is in the word
def check(wordList,dashList,guess):
    if(guess in wordList):
        for i in range(len(wordList)):
            if wordList[i] == guess:
                dashList[i] = guess
                return True
        print("Good guess")
        return True
    else:
        print("Wrong guess")
        return False

# adding or subtracting life
def lifeCheck(isTrue,lifes):
    if not isTrue:
        lifes -= 1
    return lifes


def play():
    global lifes
    lifes = 5
    curAscii = 1
    word = genWord()
    dash = genDash(word)
    wordList, dashList = splits(word, dash)

    
    print(r"""
                        .___                               
__  _  _____________  __| _/    _________    _____   ____  
\ \/ \/ /  _ \_  __ \/ __ |    / ___\__  \  /     \_/ __ \ 
 \     (  <_> )  | \/ /_/ |   / /_/  > __ \|  Y Y  \  ___/ 
  \/\_/ \____/|__|  \____ |   \___  (____  /__|_|  /\___  >
                         \/  /_____/     \/      \/     \/ 
""")
    print("Welcome to the game")
    print(HANGMANPICS[0])
    print("The word is", ''.join(dashList))

    while ''.join(dashList) != word and lifes > 0:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            guess = guess.lower()
            isTrue = check(wordList, dashList, guess)
            if isTrue:
                print(HANGMANPICS[curAscii])
            else:
                print("Wrong guess")
                curAscii += 1
                print(HANGMANPICS[curAscii])
            lifes = lifeCheck(isTrue, lifes)
            if not life(lifes):
                print("The word was", word)
                print("You lose")
                break
            else:
                print("The word is", ''.join(dashList))
        else:
            print("Please enter a single letter")

    if ''.join(dashList) == word:
        print("Congratulations! You've guessed the word:", word)

def Again():
    play = input("Do you want to play again? (y/n): ")
    if play.lower() == 'y':
        return True
    else:
        print("Thanks for playing")
        return False

# Main game loop
while True:
    play()
    if not Again():
        break


