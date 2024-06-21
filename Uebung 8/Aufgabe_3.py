input_text = input("text:")
separator = input("separator:")
formatted_text = separator + " "

for char in input_text:
    formatted_text += char + " " + separator + " "

print(formatted_text)