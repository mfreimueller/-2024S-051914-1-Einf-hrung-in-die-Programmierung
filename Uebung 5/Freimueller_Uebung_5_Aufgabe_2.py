word_list = ["Hallo", "Welt", "Hallo", "Python", "Welt"]
word_freq = dict()

for word in word_list:
    if word in word_freq:
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1

print("word_freq =", word_freq)