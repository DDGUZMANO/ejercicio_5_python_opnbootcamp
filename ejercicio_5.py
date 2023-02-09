print("Hello, here you could check if any year it's a leap year.")
anio = int(input("Please, add the number of year you want to check: "))

def bisiesto(anio):
    if (anio % 4) == 0:
        print("this a leap year.")
        
    else:
        print("This is not a leap year.")
        
bisiesto(anio)