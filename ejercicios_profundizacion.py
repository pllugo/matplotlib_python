#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
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
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]
    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos
    fig = plt.figure()
    fig.suptitle('Graficos', fontsize=10)
    fig1 = fig.add_subplot(3,1,1)
    fig2 = fig.add_subplot(3,1,2)
    fig3 = fig.add_subplot(3,1,3)
    fig1.plot(x, y1, color ="r", marker = '+',label = "y1=x**2")
    fig2.plot(x, y2, color ="b", marker = '.',label = "y2=x**3")
    fig3.plot(x, y3, color ="g", marker = '^',label = "y3=x**4")
    # Se debe colocar en la leyenda la función que representa
    # cada gráfico
    #Figura 1
    fig1.set_title("Grafico 1",fontsize=6)
    fig1.set_xlabel("X",fontsize=6)
    fig1.set_ylabel("Y",fontsize=6)
    fig1.set_facecolor("Whitesmoke")
    fig1.legend()
    fig1.grid()
    # Cada gráfico realizarlo con un color distinto
    # a su elección
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

    plt.show()


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig = plt.figure()
    fig.suptitle('Funciones Trigonométricas', fontsize=16)
    gs = gridspec.GridSpec(2, 2)
    ax = fig.add_subplot(gs[1, :])  # row 0, col 0
    ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 1
    ax2 = fig.add_subplot(gs[0, 1])
    ax.plot(x, y1, c='r', marker='^', label = "Sin(x)")
    ax.plot(x, y2, c='c', marker='.', label = "Cos(x)")
    
    ax.set_facecolor('whitesmoke')
    ax.grid()
    ax.set_ylabel("Y")
    ax.set_xlabel("x")
    ax.legend()

    ax1.plot(x, y1, c="r", label = "Sin(x)")
    ax1.set_facecolor('whitesmoke')
    ax1.grid()
    ax1.set_ylabel("Y")
    ax1.set_xlabel("x")
    ax1.legend()

    ax2.plot(x, y2, c="c", label = "Cos(x)")
    ax2.set_facecolor('whitesmoke')
    ax2.grid()
    ax2.set_ylabel("Y")
    ax2.set_xlabel("x")
    ax2.legend()
    plt.show()
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]
    
    fig = plt.figure()
    fig.suptitle('Lenguajes de Programación', fontsize=16)
    ax1 = fig.add_subplot()

    ax1.bar(lenguajes, performance, label='Lenguajes')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    ax1.set_ylabel("Performance")
    ax1.set_xlabel("Lenguajes")
    plt.show()
    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico
    fig = plt.figure()
    fig.suptitle('Uso de lenguajes de programación', fontsize=16)
    ax = fig.add_subplot()
    lista = [x for x in uso_lenguajes]#Tomo las claves del diccionario
    lista_2 = [uso_lenguajes[lista[x]] for x in range(len(lista))]#hago una lista con los valores del diccionario
    explode = (0.1, 0, 0, 0, 0, 0, 0)  # solo resaltar Python
    ax.pie(lista_2, labels = lista, explode = explode, autopct='%1.1f%%', shadow=True, startangle=90) 
    # Igualo la relacion de aspecto para que se vea como un círculo
    ax.axis('equal')
    plt.show()


def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]
    signal_x = [data['X'] for data in signal]
    signal_y = [data['Y'] for data in signal]
    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    # signal_x = [....]
    # signal_y = [....]

    # plot(signal_x, signal_y)
    fig = plt.figure()
    fig.suptitle('Graficos', fontsize=10)
    fig1 = fig.add_subplot(1, 2, 1)
    fig2 = fig.add_subplot(1, 2, 2)
    fig1.plot(signal_x, signal_y, color ="r", marker = '+',label = "Gráfica 1")
    fig1.grid()
    fig1.set_facecolor('whitesmoke')
    fig1.set_ylabel("Y")
    fig1.set_xlabel("x")
    fig1.legend()
    
    
    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    filter_signal_x = [x for x in signal_x if (abs(x) > -0.7)]
    filter_signal_y = [y for y in signal_y if (abs(y) > -0.7)]
    print(len(filter_signal_x))
    print(len(filter_signal_y))
    fig2.scatter(filter_signal_x, filter_signal_y, color ="b", marker = '.',label = "Gráfica 2")
    fig2.grid()
    fig2.set_facecolor('whitesmoke')
    fig2.set_ylabel("Y")
    fig2.set_xlabel("x")
    fig2.legend()
    plt.show()
    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
