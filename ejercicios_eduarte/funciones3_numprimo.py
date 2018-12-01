#!/usr/bin/python
# -*- coding : iso-8859-15
def es_primo(x): 
    if x<2:
        return False 
    elif x==2:
        return True
    else:
        for n in range(2,x):
            if x%n == 0:
                return False
            elif(n == x-1):
                return True


while True:
    try:
        numero = int(raw_input("inserta un numero (0) salir >> "))
        if numero==0:
            break
        if es_primo(numero):
            print "\nEl numero %s es primo" % numero
        else:
            print "\nEl numero %s NO es primo" % numero
    except:
        print "\nEl numero tiene que ser entero"