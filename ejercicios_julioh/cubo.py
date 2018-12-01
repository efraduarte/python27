#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def sc(n):
    if n > 1:
        r = sc(n - 1) + n ** 3
    else:
        r = 1
    return r
a = int(input("Desde: "))
b = int(input("Hasta: "))
for i in range(a, b+1):
    if sc(i):
        print ("Numero primo: ",i)