import numpy as np

#Ejercicio 1
class numComplejo:
    def __init__(self, numi1, numi2):
        self.numi1 = numi1
        self.numi2 = numi2
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    
    def sumar (self):
        sumai=self.numi1 + self.numi2
        print("El resultado de la suma es: ",sumai)
        return sumai
    def restar (self):
        restai=self.numi1 - self.numi2
        print("El resultado de la resta es: ",restai)
        return restai
    def multiplicar (self):
        multiplicacioni=self.numi1 * self.numi2
        print("El resultado de la multiplicacion es: ",multiplicacioni)
        return multiplicacioni
    def dividir (self):
        dividiri = self.numi1/self.numi2
        print("El resultado de la division es: ",dividiri)
    def __str__(self):
        return f"{self.numi1}{self.numi2}{self.sumar}{self.restar}{self.multiplicar}{self.dividir}"

#Ejercicio 2
class Vectores:
    def __init__(self, vec1, vec2):
        self.vec1 = vec1
        self.vec2 = vec2
        self.sumarV()
        self.restarV()
        self.multiplicarV()
        self.dividirV()
    
    def sumarV (self):
        sumavec=self.vec1 + self.vec2
        print("El resultado de la suma es: ",sumavec)
        return sumavec
    
    def restarV (self):
        restavec=self.vec1 - self.vec2
        print("El resultado de la resta es: ",restavec)
        return restavec

    def multiplicarV (self):
        multiplicacionvec=self.vec1 * self.vec2
        print("El resultado de la multiplicacion es: ",multiplicacionvec)
        return multiplicacionvec

    def dividirV (self):
        dividirvec = self.vec1/self.vec2
        print("El resultado de la division es: ",dividirvec)
        return dividirvec

    

#Ejercicio 3
class Matrices:
    def __init__(self, mat1, mat2):
        self.mat1 = mat1
        self.mat2 = mat2
        self.sumarM()
        self.restarM()
        self.multiplicarM()
    
    def sumarM (self):
        sumamat=self.mat1 + self.mat2
        print("El resultado de la suma es: ",sumamat)
        return sumamat
    
    def restarM (self):
        restamat=self.mat1 - self.mat2
        print("El resultado de la resta es: ",restamat)
        return restamat

    def multiplicarM (self):
        multiplicacionmat=self.mat1 * self.mat2
        print("El resultado de la multiplicacion es: ",multiplicacionmat)
        return multiplicacionmat
#Ejercicio 4

#Ejercicio 5