#!/usr/bin/python
# -*- coding : iso-8859-15
def f(x):
    y = 2 * x ** 2 + 1
    return y

# Programa que usa la funcion f(x)
for i in range(5):
    y = f(i)
    print (i,y)