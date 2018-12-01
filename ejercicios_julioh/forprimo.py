#! /usr/bin/python
# -*- coding: iso-8859-15 -*
a = 0
n = int(input("Ingrese el número: "))
for i in range(1, n+1):
    if (n%i == 0):
     a = a + 1
if (a != 2):
    print ("No es primo")
else:
    print ("Si es primo")