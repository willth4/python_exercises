# geg. Temperatur in Celsius
# ges. Temperatur in Kelvin
# K=C+273.15

def get_temperature():
    while True:
        C=input("Gib die Temperatur in Celsius ein: ")
        try:
            C=float(C)
            return C
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur.")

def convert_to_kelvin(C):
    K=C+273.15
    return K

def convert_to_fahrenheit(C):
    # (0 °C x 9 / 5) + 32 = 32 °F
    F=(C * 9 / 5) + 32
    return F

if __name__ == '__main__':
    C= get_temperature()
    print("Das sind "+ str(convert_to_kelvin(C)) + " K (Kelvin).")
    print("Das sind " + str(convert_to_fahrenheit(C)) + " °F (Fahrenheit).")