import random

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
def life():
    """life checking"""
    if life == 0:
        print("You lose")
        return False
    else:
        print("You have", life, "lives left")
        return True

# split the word & dash into a list
def splits(word,dash):
    """Split the word and dash into a list."""
    wordList = list(word)
    dashList = list(dash)
    return wordList, dashList

# check if the guess is in the word
def check(wordList,dashList,guess):
    if(guess in wordList):
        for i in range(len(wordList)):
            if wordList[i] == guess:
                dashList[i] = guess
        print("Good guess")
        return True
    else:
        print("Wrong guess")
        return False

# adding or subtracting life
def lifeCheck(isTrue):
    if isTrue != True:
        life -= 1


word = genWord()
dash = genDash(word)
wordList, dashList = splits(word, dash)

