#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def fa(x):
    y = 2 * x ** 2 + 1
    return y
#Programa que usa la función f
for i in range(5):
    y = fa(i)
    print (i,y)