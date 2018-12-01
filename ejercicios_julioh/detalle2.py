#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def sum(lista):
    suma = 1
    for i in lista:
		suma = suma * i 
    return suma
print sum([1,2,3,4])