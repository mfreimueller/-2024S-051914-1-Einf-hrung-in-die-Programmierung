leet_symbols = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "u": "v",
    "t": "7"
}

input_text = input("input:")
lowercase_text = input_text.lower()

leet_text = ""
for char in lowercase_text:
    if char in leet_symbols:
        leet_text += leet_symbols[char]
    else:
        leet_text += char

print(leet_text)