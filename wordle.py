import random
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

LETTER_FREQUENCIES = {'a': 909, 'e': 1055, 'r': 836, 'o': 675, 'i': 647, 's': 618, 't': 667, 'l': 645, 'n': 548, 'u': 457, 'y': 417, 'c': 446, 'd': 371, 'h': 377, 'm': 299, 'p': 345, 
'b': 266, 'g': 299, 'k': 203, 'w': 193, 'f': 206, 'v': 148, 'z': 36, 'x': 37, 'j': 27, 'q': 29}

def generate_secret_word():
    secret_word = random.choice(list(get_valid_wordle_guesses()))
    return secret_word

def score_word(word: str) -> int:
    return sum(LETTER_FREQUENCIES.get(letter.lower(),0) for letter in word)

def wordvalid(guess: str) -> bool:
    validlist = list(get_valid_wordle_guesses())
    guess = guess.upper()

    if guess not in validlist or len(guess) != 5:
        return False
    return True

def get_feedback(guess: str, secret_word: str) -> str:

    returnList = ["-"]*5

    #green
    guesslist = list(guess)
    secretwordlist = list(secret_word)

    if wordvalid(guess) == False:
        return "Please input a valid guess"
    else:
        for i in range (len(guess)):
            for j in range (len(secret_word)):
                if i == j and guess[i] == secret_word[j]:
                    returnList[i] = guess[i].upper()
                    guesslist[i] = "-"
                    secretwordlist[j] = "_"

    #yellow
    if wordvalid(guess) == False:
        pass
    else:
        for y in range(len(guesslist)):
            for z in range(len(secretwordlist)):
                if guesslist[y] == secretwordlist[z]:
                    returnList[y] = guesslist[y].lower() #must fix indice problem
                    guesslist[y] = "-"
                    secretwordlist[z] = "_"
    strret = "".join(c for c in returnList)
    return str(strret)


def colors(guess: str, secret_word: str) -> str:
    guess = guess.upper()
    secret_word = secret_word.upper()
    ourword = get_feedback(guess, secret_word)
    colorword = ""

    if wordvalid(guess) == False:
        return "Please input a valid guess"
    else:
        for i in range(len(ourword)):
            if ourword[i].isupper():
                colorword += Back.GREEN + guess[i]
            elif ourword[i].islower():
                colorword += Back.YELLOW + guess[i]
            elif ourword[i] == "-":
                colorword += Back.WHITE + guess[i]

    return str(colorword)


def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
    '''
    global wordlist 
            
    temp = set()
        
    if len(guesses) == 0:
            wordlist = valid_guesses.copy()
            return 'CLINT'

    for i in range(5):
        if feedback[-1][i] == '-':
            for item in wordlist:
                if guesses[-1][i] in item and len(temp) < (len(wordlist) - 1):
                    temp.add(item)
                    
        elif feedback[-1][i].isupper():
            for item in wordlist:
                if guesses[-1][i] != item[i] and len(temp) < (len(wordlist) - 1):
                    temp.add(item)
                     
        elif feedback[-1][i].islower():
            for item in wordlist:
                if guesses[-1][i] not in item or guesses[-1][i] == item[i] and len(temp) < (len(wordlist) - 1):
                    temp.add(item)
                            
    wordlist = wordlist.difference(temp)

            
    if len(guesses) == 1:
            return 'SOARE'

    for item in wordlist:
        if sorted(set(item)) == sorted(item):
            return item
    return list(wordlist)[0]




storage = []
regstorage = []
guesses = []
def game2():
    valid_guesses = get_valid_wordle_guesses()
    for i in range(6):
         print("Enter a guess")
         n = input()
         if n.upper() == "H":
             aiguess = get_AI_guess(guesses, regstorage, get_secret_words(), valid_guesses)
             storage.append(colors(aiguess, secret_word))
             for word in range(len(storage)):
                print(str(storage[word]))
             guesses.append(aiguess)
             regstorage.append(get_feedback(aiguess, secret_word))
             if aiguess == secret_word:
                 print(f"Congratulations! You won the wordle in" + {i+1} + "guesses")
                 break
         else:
            while not wordvalid(n):
                print("Please input a valid guess")
                n = input()
            guesses.append(n)
            game(n, storage)
            if n == secret_word:
                print(f"Congratulations! You won the wordle in" + {i+1} + "guesses")
                break

    else:
        print(f"You lost! The word was " + secret_word)

def game(input: str, storage: list):
    storage.append(colors(input, secret_word))
    regstorage.append(get_feedback(input, secret_word))
    for word in range(len(storage)):
        print(str(storage[word]))

if __name__ == "__main__":
    print("Start game")
    secret_word = generate_secret_word()
    game2()
    print("Game end")

