#!/usr/bin/python
# -*- coding : iso-8859-15
def primo(q):
    c = 0
    for i in range(1, q+1):
        if q%i == 0:
            c = c + 1
    if c > 2:
        return False
    else:
        return True
# Programa que lista los numeros primos ene el rango
a = int(input("Desde: "))
b = int(input("Hasta: "))
for q in range(a, b+1):
    if primo(q):
        
        print ("Numero primo: ",q)