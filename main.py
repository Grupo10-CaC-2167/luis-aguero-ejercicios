from src.utils import *

#Ejercicio 1
palabra1 = "hola como estas"
replacespace(palabra1)
print(palabra1)
print (replacespace(palabra1))

#Ejercicio 2
palabra2 = "hOLA mUNDO"
changeMayus(palabra2)
print(palabra2)
print(changeMayus(palabra2))

#Ejercicio 3
word1 = input("Ingrese una palabra: ")
ind = int(input("¿Que indice quiere cambiar?: "))
while ind > len(word1):
    ind = int(input("Ingrese otro indice:"))
letra = input("¿Por cual letra quiere cambiarla?: ")
modificateString (word1,ind,letra)
print(word1)
print(modificateString (word1,ind,letra))

#Ejercicio 4
palabra4 = input("Ingrese una palabra: ")
primeraMayus(palabra4)
print(palabra4)
print(primeraMayus(palabra4))

#Ejercicio 5
numeroNotas = int(input("Ingrese cuantas notas va a cargar: "))
subcampeon(numeroNotas)

