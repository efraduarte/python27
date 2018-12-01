#! /usr/bin/python
# -*- coding: iso-8859-15

#Promedio
n = int(input("Ingrese la cantidad de datos: "))
suma = 0
for i in range(n):
    x = (float(input("Ingrese el dato: ")))
    suma = suma + x
prom = suma / n
print("El promedio es: ", prom)