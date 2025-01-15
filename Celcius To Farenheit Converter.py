import os
Retry = "0"
def Fahrenheit_To_Celcius(Fahrenheit):
    feh = (Fahrenheit - 32) * 5/9
    return  feh

def Celcius_To_Farenheit (Celcius):
    cel = (Celcius * 9/5) + 32
    return cel

while (Retry == "Y") or (Retry == "0"):
    Option_Pick = input("pick (1) for : Fahrenheit To Celcius\npick (2) for : Celcius To Farenheit\n")
    if Option_Pick == "1":
        os.system('cls')
        print ("You have selected Fahrenheit To Celcius")
        Temp = float(input("Enter the temperature (°F): "))
        print("--------------------------")
        print("°C :",Fahrenheit_To_Celcius(Temp))
        print("--------------------------")
        Retry = input("Enter (Y) to retry : ").upper()
        os.system('cls')

    elif Option_Pick == "2":
        os.system('cls')
        print ("You have selected Celcius To Farenheit")
        Temp = float(input("Enter the temperature (°C): "))
        print("--------------------------")
        print("°F :", Celcius_To_Farenheit(Temp))
        print("--------------------------")
        Retry = input("Enter (Y) to retry : ").upper()
        os.system('cls')

    else:
        os.system('cls')
        print("You have not Selected an option")
        Retry = input("Enter (Y) to retry : ").upper()
        os.system('cls')
