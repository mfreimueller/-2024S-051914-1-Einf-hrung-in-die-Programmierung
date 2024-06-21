import matplotlib.pyplot as plt
import random

input_path = input("input file: ")
char_stats = dict()

with open(input_path, "r") as file:
    line = file.readline()

    while line != "":
        for char in line:
            if char in char_stats:
                char_stats[char] += 1
            else:
                char_stats[char] = 1
        
        line = file.readline()

colors = []

for key in char_stats.keys():
    colors.append((random.randint(0, 100) / 100, random.randint(0, 100) / 100, random.randint(0, 100) / 100))

plt.bar(char_stats.keys(), char_stats.values(), color=colors)
plt.show()