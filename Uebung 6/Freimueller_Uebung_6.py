# Nachdem ich nicht zu 100% sicher bin, welche Anweisung
# am Aufgabenblatt korrekt ist, habe ich hier eine Kompromisslösung:
# Wenn der fettgedruckte Text, dass nur die geraden Zahlen multipliziert
# werden sollen, wahr ist, so setzt man multiply_even_numbers auf True.
# Wenn aber die Anweisung unter Schritt 2 gültig ist, so setzt man 
# multiply_even_numbers auf False.
multiply_even_numbers = True

input_number_list = []

try: # safety first.
    in_file = open("input_data.txt", "r")
    
    line = in_file.readline()

    while line != "":
        if line.strip().isdecimal():
            input_number_list.append(int(line))

        line = in_file.readline()

    in_file.close()
except FileNotFoundError:
    print("Die Datei 'input_data.txt' wurde nicht gefunden!")
    exit()

def process_number_list(number_list):
    product = 1

    for number in number_list:
        # Wenn man das Produkt der ungeraden Zahlen berechnen wollte,
        # müsste man aus der unteren Zeile ein number % 2 == 1 machen.
        if number % 2 == (0 if multiply_even_numbers else 1):
            product *= number
    
    return product

product = process_number_list(input_number_list)

out_file = open("out_data.txt", "w")
out_file.write(str(product))
out_file.close()