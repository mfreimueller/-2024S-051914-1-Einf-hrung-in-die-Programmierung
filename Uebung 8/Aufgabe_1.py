text = input("text:")

symbols = set()

for char in text:
    if char in symbols:
        print(char, " is doppelt!")

    symbols.add(char)

if len(text) == len(symbols):
    print("Die Zeichenkette enthält kein doppeltes Zeichen")
else:
    print("Die Zeichenkette enthält mindestens eines seiner Zeichen doppelt")