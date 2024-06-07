in_file = open("input_data.txt", "r")
input_number_list = []

line = in_file.readline()

while line != "":
    if line.strip().isdecimal():
        input_number_list.append(int(line))

    line = in_file.readline()

in_file.close()

def process_number_list(number_list):
    product = 1

    for number in number_list:
        # Wenn man das Produkt der ungeraden Zahlen berechnen wollte,
        # müsste man aus der unteren Zeile ein number % 2 == 1 machen.
        if number % 2 == 0:
            product *= number
    
    return product

product = process_number_list(input_number_list)

out_file = open("out_data.txt", "w")
out_file.write(str(product))
out_file.close()