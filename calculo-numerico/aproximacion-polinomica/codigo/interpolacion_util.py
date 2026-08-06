"""
UTILIDADES COMPARTIDAS DE INTERPOLACIÓN POLINÓMICA

Funciones comunes a los distintos métodos (Lagrange, Newton, Hermite,
Chebyshev, Splines, Segmentaria y Taylor) para evitar repetir código.
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def evaluar_polinomio(polinomio, x_valor):
    """Evalúa un polinomio simbólico reemplazando la 'x' por un valor."""
    x = sp.Symbol('x')
    return polinomio.subs(x, x_valor)


def tabla_diferencias_divididas(x_points, y_points):
    """
    Calcula la tabla completa de diferencias divididas de Newton.
    Retorna una matriz triangular: la columna j contiene las diferencias
    divididas de orden j.
    """
    n = len(x_points)
    tabla = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tabla[i][0] = y_points[i]
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x_points[i + j] - x_points[i])
    return tabla


def coeficientes_diferencias_divididas(x_points, y_points):
    """Retorna los coeficientes del polinomio de Newton (diagonal superior)."""
    tabla = tabla_diferencias_divididas(x_points, y_points)
    return [tabla[0][j] for j in range(len(x_points))]


def construir_polinomio_newton(x_points, y_points):
    """
    Construye el polinomio de Newton con diferencias divididas.
    Retorna el polinomio simplificado y la variable simbólica x.
    """
    x = sp.Symbol('x')
    coef = coeficientes_diferencias_divididas(x_points, y_points)
    pol = coef[0]
    for i in range(1, len(coef)):
        termino = coef[i]
        for j in range(i):
            termino *= (x - x_points[j])
        pol += termino
    return sp.simplify(pol), x


def evaluar_por_tramos(tramos, x_valor):
    """
    Evalúa una función definida a trozos en un valor dado.
    tramos: lista de tuplas (x_inicio, x_fin, expresión_simbólica).
    """
    x = sp.Symbol('x')
    for xi, xf, expr in tramos:
        if xi <= x_valor <= xf:
            return float(expr.subs(x, x_valor))
    return None


def graficar_polinomio(polinomio, x_puntos, y_puntos, titulo, etiqueta='P',
                       x_min=-4, x_max=2, n_puntos=200):
    """Grafica un polinomio interpolador junto con los puntos conocidos."""
    x_vals = np.linspace(x_min, x_max, n_puntos)
    y_vals = [float(evaluar_polinomio(polinomio, xv)) for xv in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'b-', label=f'{etiqueta}(x) = {polinomio}', linewidth=2)
    plt.plot(x_puntos, y_puntos, 'ro', label='Puntos conocidos', markersize=10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.show()
