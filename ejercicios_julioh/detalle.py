#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def factorial(num):
    resultado = num
    for i in range(num-1,1,-1):
        resultado = resultado * i
	return resultado
print (factorial(10))
