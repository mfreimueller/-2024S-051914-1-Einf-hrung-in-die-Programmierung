number_from_user = input("Zahl erbeten: ")

if not number_from_user.isdecimal():
    print("Kein Zahl wurde eingegeben!")
    exit()

n = int(number_from_user)
sum_even = 0

# Alternativ: for idx in range(0, n, 2):
# Dann kann man, offensichtlich, die If-Abfrage
# auslassen.
for idx in range(1, n):
    if idx % 2 == 0:
        sum_even = sum_even + idx

print("Die Summe der geraden Zahlen von 1 bis", n, "beträgt", sum_even)