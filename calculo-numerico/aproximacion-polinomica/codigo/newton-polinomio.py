import sympy as sp  # Biblioteca para cálculo simbólico (maneja la 'x' como variable)
import numpy as np  # Para crear arreglos numéricos y rangos
import matplotlib.pyplot as plt  # Para generar la gráfica final
from interpolacion_util import (
    evaluar_polinomio,           # Evalúa un polinomio simbólico en un valor
    tabla_diferencias_divididas, # Construye la tabla completa de Newton
    graficar_polinomio,          # Dibuja el polinomio y los puntos conocidos
)

def obtener_polinomio_newton(x_points, y_points):
    """
    Construye el polinomio P(x) usando el método de Newton de diferencias divididas.
    Recibe dos listas: x_points (valores de x) y y_points (valores de y correspondientes).
    Retorna el polinomio simbólico y la variable 'x' para evaluaciones posteriores.
    """
    # 1. Definimos 'x' como un símbolo matemático, no como un número
    x = sp.Symbol('x')

    # 2. Calculamos la tabla completa de diferencias divididas
    tabla = tabla_diferencias_divididas(x_points, y_points)
    coeficientes = [tabla[0][j] for j in range(len(x_points))]

    # 3. Construimos el polinomio de Newton
    polinomio = coeficientes[0]
    terminos = [f"{coeficientes[0]}"]

    print("Construcción del polinomio de Newton:")
    print("-" * 50)

    for i in range(1, len(coeficientes)):
        termino = coeficientes[i]
        termino_str = f"{coeficientes[i]}"

        # Multiplicamos por (x - x_j) para cada j < i
        for j in range(i):
            termino *= (x - x_points[j])
            termino_str += f"(x - {x_points[j]})"

        polinomio += termino
        terminos.append(termino_str)

    print("Tabla de diferencias divididas:")
    for i in range(len(x_points)):
        fila = f"x_{i} = {x_points[i]:2.0f} | "
        for j in range(len(x_points) - i):
            fila += f"{tabla[i][j]:6.1f} | "
        print(fila)
    
    print("\nTérminos del polinomio:")
    for i, termino in enumerate(terminos):
        print(f"Término {i}: {termino}")
    
    print("-" * 50)
    print(f"P(x) = {' + '.join(terminos)}")
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
polinomio, x_var = obtener_polinomio_newton(x_puntos, y_puntos)

# Probamos el polinomio evaluando puntos que NO estaban en la lista original
print("\nEvaluaciones:")
for punto in [-1, -2, 4, 7]:
    valor = evaluar_polinomio(polinomio, punto)
    print(f"P({punto}) = {valor}")

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

graficar_polinomio(polinomio, x_puntos, y_puntos, 'Polinomio de Interpolación de Newton')