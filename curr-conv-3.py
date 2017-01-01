print("Which country would you like to convert currencies with?")
print("C - Canada")
print("M - Mexico")
print("B - Brazil")
print("D - Germany")
print("E - Any other European country")
print("N - China")
print("I - India")
print("G - Nigeria")
print("T - Ethiopia")
country = str(input("> "))
print(" ")


def conv():
    if country == "C":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 1.34
        print(str(value) + " USD = " + str(nu) + " CAD.")
    elif country == "M":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 20.73
        print(str(value) + " USD = " + str(nu) + " MXN.")
    elif country == "B":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 3.26
        print(str(value) + " USD = " + str(nu) + " BRL.")
    elif country == "D":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 1.72
        print(str(value) + " USD = " + str(nu) + " DEM.")
    elif country == "E":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * .95
        print(str(value) + " USD = " + str(nu) + " EUR.")
    elif country == "N":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 6.94
        print(str(value) + " USD = " + str(nu) + " CNY.")
    elif country == "I":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 67.95
        print(str(value) + " USD = " + str(nu) + " INR.")
    elif country == "G":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 314.98
        print(str(value) + " USD = " + str(nu) + " NGN.")
    elif country == "T":
        print("How much money do you want to convert? Add .0 to the end if whole number.")
        value = float(input("> "))
        print(" ")
        nu = value * 22.52
        print(str(value) + " USD = " + str(nu) + " ETB.")
conv()
input(" ")
