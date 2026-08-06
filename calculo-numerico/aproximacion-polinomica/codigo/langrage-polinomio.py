"""
MÓDULO DE INTERPOLACIÓN POLINÓMICA DE LAGRANGE

Este script implementa el método de Lagrange para hallar el único polinomio 
de grado n que pasa exactamente por un conjunto de n+1 puntos dados.

ALGORITMO:
1. Definir la variable simbólica 'x' mediante SymPy.
2. Iterar sobre cada punto (xi, yi) del conjunto de datos.
3. Para cada punto 'i', calcular el Polinomio Base Li(x):
   Li(x) = Π [ (x - xj) / (xi - xj) ] para todo j != i.
4. Construir el Polinomio Interpolador P(x) como la sumatoria:
   P(x) = Σ [ yi * Li(x) ].
5. Simplificar la expresión algebraica resultante.

PROPIEDADES:
- El determinante de Vandermonde garantiza la unicidad del polinomio.
- Complejidad computacional: O(n^2).
"""

import sympy as sp  # Biblioteca para cálculo simbólico (maneja la 'x' como variable)
import numpy as np  # Para crear arreglos numéricos y rangos
import matplotlib.pyplot as plt  # Para generar la gráfica final
from interpolacion_util import evaluar_polinomio, graficar_polinomio  # Utilidades compartidas

def obtener_polinomio_lagrange(x_points, y_points):
    """
    Construye el polinomio P(x) que pasa por todos los puntos (X, Y). Polinomio de interpolación de Lagrange.
    Recibe dos listas: x_points (valores de x) y y_points (valores de y correspondientes). Retorna el polinomio simbólico y la variable 'x' para evaluaciones posteriores.
    """
    # 1. Definimos 'x' como un símbolo matemático, no como un número
    x = sp.Symbol('x')
    
    # 2. 'n' es la cantidad de puntos; definirá el grado del polinomio (n-1)
    n = len(x_points)
    
    # 3. Aquí iremos sumando cada término: P(x) = L0*y0 + L1*y1 + ...
    polinomio = 0
    
    print("Construcción del polinomio de Lagrange:")
    print("-" * 50)
    
    # Bucle externo: recorre cada punto 'i' para calcular su base L_i(x)
    for i in range(n):
        L_i = 1  # Inicializamos el producto en 1
        terminos_l = [] # Lista auxiliar solo para mostrar el proceso en consola
        
        # Bucle interno: construye el producto (x - xj) / (xi - xj) para j != i
        for j in range(n):
            if j != i:
                # Aplicamos la fórmula: Termino = (x - x_j) / (x_i - x_j)
                termino = (x - x_points[j]) / (x_points[i] - x_points[j])
                
                # Vamos multiplicando para obtener el polinomio base L_i
                L_i *= termino
                
                # Guardamos la representación en texto para el print
                terminos_l.append(f"(x-{x_points[j]})/({x_points[i]}-{x_points[j]})")
        
        # Mostramos en consola cómo se va viendo cada L_i
        print(f"L_{i}(x) = {' * '.join(terminos_l)}")
        print(f"L_{i}(x) simplificado = {sp.simplify(L_i)}")
        print()
        
        # El polinomio final suma: y_i * L_i(x)
        polinomio += y_points[i] * L_i
    
    print("-" * 50)
    # Mostramos el polinomio total sin simplificar y luego simplificado (agrupado)
    print(f"P(x) = {polinomio}")
    print(f"P(x) simplificado = {sp.simplify(polinomio)}")
    
    # Retornamos el polinomio limpio y la variable simbólica para usarla después
    return sp.simplify(polinomio), x

# --- EJECUCIÓN DEL EJEMPLO ---

# Definimos los puntos conocidos (nodos)
x_puntos = [1, 0, -3]
y_puntos = [2, 4, -2]

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}\n")

# Llamada principal para obtener la fórmula del polinomio
polinomio, x_var = obtener_polinomio_lagrange(x_puntos, y_puntos)

# Probamos el polinomio evaluando puntos que NO estaban en la lista original
print("\nEvaluaciones:")
for punto in [-1,-2, 4, 7]:
    valor = evaluar_polinomio(polinomio, punto)
    print(f"P({punto}) = {valor}")

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

graficar_polinomio(polinomio, x_puntos, y_puntos, 'Polinomio de Interpolación de Lagrange')
