import random

word_list = []

with open("words.txt", "r") as file:
    line = file.readline()

    while line != "":
        word_list.append(line.strip())
        line = file.readline()

secret_word = random.choice(word_list)
attempts = 1

while attempts < 6:
    guess = ""

    while len(guess) != 5:
        guess = input("5-stelliger Guess: ").strip()
    
    guess = guess.lower()

    matches = []
    partly_fitting_matches = []
    for idx, char in enumerate(guess):
        # die beiden Funktionen darunter in eigene
        # Funktionen auszulagern ist möglich, aber mMn
        # ist es hier nicht notwendig.
        if char == secret_word[idx]:
            matches.append(idx)
        elif char in secret_word:
            partly_fitting_matches.append(char)
    
    if guess == secret_word:
        break

    print(attempts, ". Versuch: ", guess)
    print("Korrekte Position: ", matches)
    print("Richtiger Buchstabe, aber falsche Position: ", partly_fitting_matches)

    attempts += 1

if attempts < 6:
    print("Hurra! Du hast das Wort nach", attempts, "Versuchen erraten!")
else:
    print("Das gesuchte Wort war ", secret_word)