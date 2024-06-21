def encrypt(txt, offset = 1):
    lowercase_txt = txt.lower()
    encrypted_text = ""

    for char in lowercase_txt:
        if char.isalpha():
            new_ord = ord(char) + offset

            if new_ord < 97:
                new_ord = 122
            elif new_ord > 122:
                new_ord = 97
            
            encrypted_text += chr(new_ord)
        else:
            encrypted_text += char
    
    return encrypted_text

input_path = input("input file:")
output_path = input("output file:")
offset = int(input("offset:"))

with open(input_path, "r") as input_file:
    with open(output_path, "w") as output_file:
        line = input_file.readline()
        while line != "":
            encrypted_line = encrypt(line, offset)
            output_file.write(encrypted_line)

            line = input_file.readline()