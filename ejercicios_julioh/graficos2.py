#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt 
from matplotlib import * 
import numpy as np
# Definimos el periodo de la grÃ¡fica senoidal
periodo = 2
# Definimos el array dimensional
x = np.linspace(0, 10, 1000)
# Definimos la funciÃ³n senoidal
y = np.sin(2*np.pi*x/periodo)  
# Creamos la figura
plt.figure()
# Primera grÃ¡fica
title('Grafico')
plt.subplot(2,2,1,title="Grafica 1")
plt.plot(x, y,'r')
# Segunda grÃ¡fica
plt.subplot(2,2,2, title="Grafica 2")
plt.plot(x, y,marker='o', linestyle='--', color='r',)
# Tercera grÃ¡fica 
plt.subplot(2,2,3,title="Grafica 3")
plt.plot(x, y,marker='*', linestyle='-', color='g')
# Cuarta grÃ¡fica	
plt.subplot(2,2,4,title="Grafica 4")
plt.plot(x, y, marker='x', linestyle=':', color='b',)
# Mostramos en pantalla
plt.show()