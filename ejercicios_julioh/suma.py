#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def primo(n):
    c = 0
    for i in range(1, n+1):
        if n%i == 0:
            c = c + 1
        if c > 2:
            return False
        else:
            return True
#Programa que lista los números primos en el rango
a = int(input("Desde: "))
b = int(input("Hasta: "))
for i in range(a, b+1):
      if primo(i):
        print ("Numero primo: ",i)