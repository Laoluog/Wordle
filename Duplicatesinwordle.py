from wordle_secret_words import get_secret_words

secretwords = get_secret_words()
dupes = 0
for word in secretwords:
    if len(set(word)) != len(list(word)):
        dupes += 1

print(dupes)