from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

secretwords = get_secret_words()
guesses = get_valid_wordle_guesses()

letterdict = {'a': 0, 'e': 0, 'r': 0, 'o': 0, 'i': 0, 's': 0, 't': 0, 
    'l': 0, 'n': 0, 'u': 0, 'y': 0, 'c': 0, 'd': 0, 'h': 0, 
    'm': 0, 'p': 0, 'b': 0, 'g': 0, 'k': 0, 'w': 0, 'f': 0, 
    'v': 0, 'z': 0, 'x': 0, 'j': 0, 'q': 0}
for word in secretwords:
    l = set(word)
    for i in l:
        letterdict[i.lower()] += 1
print(letterdict)
tempscore = 0
bestwords = []
for wrd in guesses:
    score = 0
    l = set(wrd)
    for i in l:
        score += letterdict[i.lower()]
    if score >= tempscore:
        tempscore = score
for wrd2 in guesses:
    score = 0
    l = set(wrd2)
    for i in l:
        score += letterdict[i.lower()]
    if score == tempscore:
        bestwords.append(wrd2)
print(bestwords)