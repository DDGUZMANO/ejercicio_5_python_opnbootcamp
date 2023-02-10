print("Hello, here you could check if any year it's a leap year.")
anio = int(input("Please, add the number of year you want to check: "))

def bisiesto(anio):
    if (anio % 4) == 0:
        return "this a leap year."
        
    else:
        return "This is not a leap year."
        
print(bisiesto(anio))