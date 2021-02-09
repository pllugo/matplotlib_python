#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar los valores de X e Y en un gráfico de línea

    # Función que se desea graficar:
    # y1 = x**2

    x = list(range(-10, 11, 1))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y = [i**2 for i in x]
    fig = plt.figure()
    fig.suptitle('Y=f(x**2)', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(x, y, c='blue', marker='^', ms=10, label='y=x**2')
    ax.legend()
    ax.grid()
    custom_ticks = np.linspace(-10, 10, 11, dtype=int)
    ax.set_xticks(custom_ticks)
    ax.set_facecolor('whitesmoke')
    plt.show()

    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "Y" en función de "X"
    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección


def ej2():
    # Line Plot
    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, color = "red", marker = ".", label = "y1=x**2")
    ax.plot(x, y2, color = "blue", marker = "+", label = "y2=x**3")
    ax.set_facecolor("whitesmoke")
    ax.set_title("Graficas y1=x**2 y y2=x**3")
    ax.set_ylabel("Y")
    ax.set_xlabel("x")
    ax.legend()
    plt.show()
    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección


def ej3():
    # Scatter Plot
    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función a implementar
    # y = tanh(x) --> tangente hiperbólica

    # Implementacion
    y = np.tanh(x)
    fig = plt.figure()
    fig.suptitle('Scatter', fontsize=16)
    ax1 = fig.add_subplot()
    ax1.scatter(x, y, c='m', marker='^', label = "tanh(x)")
    ax1.set_facecolor('whitesmoke')
    ax1.grid()
    ax1.set_ylabel("Y")
    ax1.set_xlabel("x")
    ax1.legend()
    plt.show()
    # Graficar la función utilizando "scatter"

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Elegir un marker a elección


def ej4():
    # Figura con múltiples gráficos
    # Line Plot
    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)
    fig = plt.figure(figsize=(5,5))
    fig.tight_layout()
    fig1 = fig.add_subplot(4,1,1)
    fig2 = fig.add_subplot(4,1,2)
    fig3 = fig.add_subplot(4,1,3)
    fig4 = fig.add_subplot(4,1,4)
    fig1.plot(x, y1, color ="r", marker = '+',label = "y1=x**2")
    fig2.plot(x, y2, color ="b", marker = '.',label = "y2=x**3")
    fig3.plot(x, y3, color ="g", marker = '^',label = "y3=x**4")
    fig4.plot(x, y4, color ="r", marker = '*',label = "y4=sqrt(x)")

    #Figura 1
    fig1.set_title("Grafico 1",fontsize=6)
    fig1.set_xlabel("X",fontsize=6)
    fig1.set_ylabel("Y",fontsize=6)
    fig1.set_facecolor("Whitesmoke")
    fig1.legend()
    fig1.grid()

    #Figura 2
    fig2.set_title("Grafico 2",fontsize=6)
    fig2.set_xlabel("X",fontsize=6)
    fig2.set_ylabel("Y",fontsize=6)
    fig2.set_facecolor("Whitesmoke")
    fig2.legend()
    fig2.grid()

    #Figura 3
    fig3.set_title("Grafico 3",fontsize=6)
    fig3.set_xlabel("X",fontsize=6)
    fig3.set_ylabel("Y",fontsize=6)
    fig3.set_facecolor("Whitesmoke")
    fig3.legend()
    fig3.grid()

    #Figura 4

    fig4.set_title("Grafico 4",fontsize=6)
    fig4.set_xlabel("X",fontsize=6)
    fig4.set_ylabel("Y",fontsize=6)
    fig4.set_facecolor("Whitesmoke")
    fig4.legend()
    fig4.grid()

    plt.show()

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    # ej4()
