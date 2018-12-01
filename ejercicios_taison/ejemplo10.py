#! /usr/bin/python
# -*- coding: iso-8859-15

#Simular el lanzamiento de un dado. Muestre el resultado en cada intento y finalice cuando aparezca el número 3.
# Random de dados


from random import *
n = int(input("Ingrese la cantidad de intentos: "))

for i in range(n):
    x = randint(1,6)
    print x
    if x == 3:
        break
    