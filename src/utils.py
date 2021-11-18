#Ejercicio 1
def replacespace (string):

      return string.replace(" ","_")

#Ejercico 2
def changeMayus (word):
    return word.swapcase()

#Ejercico 3
def modificateString (word1,ind,letra):
    wordList = list(word1)
    wordList[ind-1] = letra
    return "".join(wordList)

#Ejercico 4
def primeraMayus (string1):
    return string1.title()

#Ejercico 5
def subcampeon (n):
    lista = []
    for x in range(n):
        nota=int(input("Ingrese la nota "+str(x+1)+": "))
        lista.append(nota)
        lista.sort()
    print(lista)
    print("La segunda nota mas alta es: ", lista[-2])
    return