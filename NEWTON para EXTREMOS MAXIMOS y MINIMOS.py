# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
18/10/2023

METODO DE NEWTON PARA EXTREMOS MAXIMOS Y MINIMOS

"""
import random as rnd

def minimo(f, a, b, c, d, n):
    """Esta función encuentra el mínimo de f en el
    intervalo a <= x <= b; c <= y <= d usando n iteraciones"""

    zMin = 0  # Inicializamos zMin con un valor grande positivo

    for i in range(n):
        r = rnd.random()  # genera un aleatorio entre 0 y 1
        x = a + (b - a) * r

        r = rnd.random()
        y = c + (d - c) * r

        z = eval(f)

        if z < zMin:  # Comparamos con zMin para encontrar el mínimo
            zMin = z
            xMin = x
            yMin = y

    return xMin, yMin, zMin

def maximo(f, a, b, c, d, n):
    """Esta función encuentra el máximo de f en el
    intervalo a <= x <= b; c <= y <= d usando n iteraciones"""

    zMax = 0

    for i in range(n):
        r = rnd.random()  # genera un aleatorio entre 0 y 1
        x = a + (b - a) * r

        r = rnd.random()
        y = c + (d - c) * r

        z = eval(f)

        if z > zMax:  # Comparamos con zMax para encontrar el máximo
            zMax = z
            xMax = x
            yMax = y

    return xMax, yMax, zMax

# Calcular mínimo
resultado_min = minimo("6.4*x + 2*y + x**2 - 2*x**4 + 2*x*y - 3*y**2", -2, 2, -2, 2, 10000)
xMin, yMin, zMin = resultado_min

# Calcular máximo
resultado_max = maximo("6.4*x + 2*y + x**2 - 2*x**4 + 2*x*y - 3*y**2", -2, 2, -2, 2, 10000)
xMax, yMax, zMax = resultado_max

# Imprimir resultados
print("Resultado del cálculo del mínimo:")
print(f"x mínimo: {xMin}")
print(f"y mínimo: {yMin}")
print(f"Valor mínimo: {zMin}")

print("\nResultado del cálculo del máximo:")
print(f"x máximo: {xMax}")
print(f"y máximo: {yMax}")
print(f"Valor máximo: {zMax}")

# EJEMPLO EN CLASE
"z=y-x-2*x**2-2*x*y-y**2"
#resultado_min = minimo("y - x - 2 * x**2 - 2 * x * y - y**2", -2, 2, 1, 3, 10000)
#resultado_max = maximo("y - x - 2 * x**2 - 2 * x * y - y**2", -2, 2, 1, 3, 10000)