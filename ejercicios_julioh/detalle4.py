#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def larga():
    x = input("¿Cuántas palabras desea ingresar?: ")
    lista = []
    larga = ""
    for i in range(x):
		palabra = raw_input("Ingresa la palabra: ")
		lista.append(palabra)
            if len(i) > len(larga):
		        larga = i
    return larga
print larga()
