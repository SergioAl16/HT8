# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
18/10/2023

METODO DE NEWTON PARA EXTREMOS MAXIMOS Y MINIMOS
CON NUMEROS ALEATORIOS EN ORDEN

"""
import random as rnd

def minimo_en_orden(f, a, b, c, d, n, h):
    """Esta función encuentra el mínimo de f en el
    intervalo a <= x <= b; c <= y <= d usando n iteraciones"""

    zMin = float('inf')  # Inicializamos zMin con un valor grande positivo

    for i in range(n):
        x = a + (i * h) % (b - a)
        y = c + (i * h) % (d - c)

        z = eval(f)

        if z < zMin:  # Comparamos con zMin para encontrar el mínimo
            zMin = z
            xMin = x
            yMin = y

    return xMin, yMin, zMin

def maximo_en_orden(f, a, b, c, d, n, h):
    """Esta función encuentra el máximo de f en el
    intervalo a <= x <= b; c <= y <= d usando n iteraciones"""

    zMax = float('-inf')

    for i in range(n):
        x = a + (i * h) % (b - a)
        y = c + (i * h) % (d - c)

        z = eval(f)

        if z > zMax:  # Comparamos con zMax para encontrar el máximo
            zMax = z
            xMax = x
            yMax = y

    return xMax, yMax, zMax

# Calcular mínimo en orden
resultado_min_orden = minimo_en_orden("6.4*x + 2*y + x**2 - 2*x**4 + 2*x*y - 3*y**2", -2, 2, -2, 2, 10000, 0.01)
xMin_orden, yMin_orden, zMin_orden = resultado_min_orden

# Calcular máximo en orden
resultado_max_orden = maximo_en_orden("6.4*x + 2*y + x**2 - 2*x**4 + 2*x*y - 3*y**2", -2, 2, -2, 2, 10000, 0.01)
xMax_orden, yMax_orden, zMax_orden = resultado_max_orden

# Imprimir resultados
print("Resultado del cálculo del mínimo en orden:")
print(f"x mínimo en orden: {xMin_orden}")
print(f"y mínimo en orden: {yMin_orden}")
print(f"Valor mínimo en orden: {zMin_orden}")

print("\nResultado del cálculo del máximo en orden:")
print(f"x máximo en orden: {xMax_orden}")
print(f"y máximo en orden: {yMax_orden}")
print(f"Valor máximo en orden: {zMax_orden}")


# EJEMPLO EN CLASE
"z=y-x-2*x**2-2*x*y-y**2"
#resultado_min = minimo("y - x - 2 * x**2 - 2 * x * y - y**2", -2, 2, 1, 3, 10000)
#resultado_max = maximo("y - x - 2 * x**2 - 2 * x * y - y**2", -2, 2, 1, 3, 10000)