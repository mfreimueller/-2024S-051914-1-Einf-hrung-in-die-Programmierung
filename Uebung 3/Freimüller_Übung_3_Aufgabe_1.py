# AUTHOR: Michael Freimüller, 11845745

# Sidenote: Ich finde den Gebrauch von Funktionen zur
# Abstraktion redundanten Codes schlichtweg elegant.
# Und es ist eleganter, eine Exception zu werfen, als
# schlichtweg FALSE zurückzugeben und dadurch eine Funktion
# zu erzeugen, die zwei unterschiedliche Werte zurückgeben
# kann (eine Unart, meiner Meinung nach - Hallo an PHP, Javascript etc.)
# Außerdem hätte ich gerne negative Zahlen als möglichen
# Input :-)

def read_input_as_number():
    input_number = input("Gib eine ganze Zahl an: ").strip()

    # Kleine Fleißaufgabe: .isdecimal wirft einen Fehler,
    # wenn ein String ein führendes Minus hat. Ergo wäre es
    # nicht möglich, eine negative Zahl zu parsen.
    # Daher erstelle ich hier einen validierbaren String,
    # der ggfs. kein führendes Minus besitzt.
    # (Man könnte das natürlich noch eleganter über einen Regex-
    # Ausdruck lösen...)
    unsigned_number = input_number[1:] if input_number.startswith("-") else input_number
    
    if unsigned_number.isdecimal():
        return int(input_number)
    else:
        raise ValueError("input must be a valid number.")

# Der eigentliche Programmablauf beginnt hier:

try:
    num1 = read_input_as_number()
    num2 = read_input_as_number()
except ValueError:
    print("Ungültige Eingabe. Es muss sich um eine ganze Zahl handeln!")
    exit()

print("Die Summe von " + str(num1) + " + " + str(num2) + " ist " + str(num1 + num2))