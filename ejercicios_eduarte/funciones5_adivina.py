#!/usr/bin/python
# -*- coding : iso-8859-15
from random import *
def adivina(numero):
    n = randint(1,6)
    return True
 
while True:
    try:
        ad = int(raw_input("Adivina el numero:  "))
        if ad==0:
            break
        if adivina(numero)==ad:
            print "acertaste",numero
        else:
            print "fallaste",numero
    except:
        print "\nEl numero tiene que ser entero"