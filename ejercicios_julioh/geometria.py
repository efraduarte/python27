#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from math import*
def cuadrado(l):
    area = l **2
    return area
def triangulo(b, h):
    area = (b * h) / 2
    return area
def rectangulo(a, b):
    area = a * b
    return area
def circulo(r):
    area = pi * r**2
    return area
pi=3,14
r = int(input("Introduzca Radio: "))
print ("El Area va hacer: ",r)