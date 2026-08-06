import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from interpolacion_util import evaluar_polinomio, graficar_polinomio  # Utilidades compartidas

def diferencias_divididas_hermite(x_vals, y_vals, dy_vals):
    """
    Calcula las diferencias divididas para la interpolación de Hermite.
    x_vals: lista de nodos (repetidos dos veces cada uno)
    y_vals: lista de valores de la función
    dy_vals: lista de valores de las derivadas
    """
    n = len(x_vals)
    tabla = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        tabla[i][0] = y_vals[i]
    
    for j in range(1, n):
        for i in range(n - j):
            if x_vals[i + j] == x_vals[i]:
                tabla[i][j] = dy_vals[i]
            else:
                tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    
    return tabla

def obtener_polinomio_hermite(x_puntos, y_puntos, dy_puntos):
    """
    Construye el polinomio de Hermite usando el método de Newton.
    """
    x = sp.Symbol('x')
    
    n = len(x_puntos)
    x_vals = []
    y_vals = []
    dy_vals = []
    
    for i in range(n):
        x_vals.append(x_puntos[i])
        x_vals.append(x_puntos[i])
        y_vals.append(y_puntos[i])
        y_vals.append(y_puntos[i])
        dy_vals.append(dy_puntos[i])
        dy_vals.append(dy_puntos[i])
    
    tabla = diferencias_divididas_hermite(x_vals, y_vals, dy_vals)
    
    coeficientes = [tabla[0][j] for j in range(2*n)]
    
    polinomio = coeficientes[0]
    terminos = [f"{coeficientes[0]}"]
    
    print("Construcción del polinomio de Hermite:")
    print("-" * 50)
    
    for i in range(1, len(coeficientes)):
        termino = coeficientes[i]
        termino_str = f"{coeficientes[i]}"
        
        for j in range(i):
            termino *= (x - x_vals[j])
            termino_str += f"(x - {x_vals[j]})"
        
        polinomio += termino
        terminos.append(termino_str)
    
    print("Tabla de diferencias divididas (Hermite):")
    for i in range(len(x_vals)):
        fila = f"x_{i} = {x_vals[i]:6.3f} | "
        for j in range(len(x_vals) - i):
            fila += f"{float(tabla[i][j]):10.5f} | "
        print(fila)
    
    print("\nTérminos del polinomio:")
    for i, termino in enumerate(terminos):
        print(f"Término {i}: {termino}")
    
    print("-" * 50)
    print(f"H(x) = {' + '.join(terminos)}")
    print(f"H(x) simplificado = {sp.simplify(polinomio)}")
    
    return sp.simplify(polinomio), x

# --- EJECUCIÓN DEL EJEMPLO ---

# Mismos datos que Lagrange y Newton: (1,2), (0,4), (-3,-2)
# Las derivadas se calculan del polinomio P(x) = -x^2 - x + 4
# f'(x) = -2x - 1
x_puntos = [1, 0, -3]
y_puntos = [2, 4, -2]
dy_puntos = [-3, -1, 5]  # f'(1) = -3, f'(0) = -1, f'(-3) = 5

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}")
print(f"y': {dy_puntos}\n")

polinomio, x_var = obtener_polinomio_hermite(x_puntos, y_puntos, dy_puntos)

print("\nVerificación en los nodos:")
for i in range(len(x_puntos)):
    val = evaluar_polinomio(polinomio, x_puntos[i])
    print(f"H({x_puntos[i]}) = {val}")

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

graficar_polinomio(polinomio, x_puntos, y_puntos, 'Interpolación de Hermite', etiqueta='H')