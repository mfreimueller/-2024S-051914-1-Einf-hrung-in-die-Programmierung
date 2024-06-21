# a: 97
# z: 122

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

print(encrypt("Mein Essen ist gut. 123!", 0))
print(encrypt("Mein Essen ist gut. 123!", 4))
print(encrypt("Mein Essen ist gut. 123!", -4))