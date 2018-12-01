#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
def dif(num1, num2):
    if (num1 > num2):
 
        aux = num1
        num1 = num2
        num2 = aux
    for i in range(num1+1, num2):
        print(i)
dif(15,10)