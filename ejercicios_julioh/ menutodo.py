#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
while True:
    print ("Selecciona una opción")
    print ("1. Primera opción")
    print ("2. Segunda opción")
    print ("3. Tercera opción")
    print ("4. Salir")
    opcionMenu = input("Inserta una opción: ")
    if opcionMenu == "1":
        print (" ")
        input("Has pulsado la opción 1. Pulsa una tecla continuar")
    elif opcionMenu == "2":
        print (" ")
        input("Has pulsado la opción 2. Pulsa una tecla continuar")
    elif opcionMenu == "3":
        print (" ")
        input("Has pulsado la opción 3. Pulsa una tecla continuar")
    elif opcionMenu == "4": 
        break
    else:
        print (" ")
        input("No has pulsado ninguna opción correcta. Pulsa tecla para continuar")