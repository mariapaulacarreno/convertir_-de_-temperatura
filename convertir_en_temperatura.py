# Programa para convertir °C en °F y °K

# Libreria
import math 

#-----
#input 
#-----

print("---------------------")
print("convertir temperatura")
print("---------------------")


Celcius = input("ingrese la temperatura en grados celcius: ")
Celcius = int(Celcius)

#---------
#Processing
#---------

Fahrenheit = Celcius*9/5 + 32
Kelvin = Celcius + 273.15

#output 
print ("-------------------------------------")
print ("-------------resultado---------------")
print ("-------------------------------------")
print ("grados fahrenheit: " + str(Fahrenheit))
print ("grados Kelvin : " +str(Kelvin))
print ("-------------------------------------")