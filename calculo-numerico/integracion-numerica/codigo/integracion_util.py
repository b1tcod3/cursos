"""
UTILIDADES COMPARTIDAS DE INTEGRACIÓN NUMÉRICA

Funciones comunes a los distintos métodos (Trapecio, Simpson 1/3,
Simpson 3/8, Romberg y Gauss-Legendre) para evitar repetir código.
Todos los ejemplos del curso usan la misma integral de prueba:

    I = ∫₀¹ e^(-x²) dx = √π/2 · erf(1) ≈ 0.7468241328124271

elegida porque NO tiene primitiva elemental: la única vía es la cuadratura.
"""

from math import erf, pi, sqrt

import matplotlib.pyplot as plt
import numpy as np


def funcion_prueba():
    """La gaussiana e^(-x²): banco de pruebas común de todos los métodos."""
    return lambda x: np.exp(-x**2)


def valor_exacto():
    """Valor exacto de la integral de prueba, calculado vía la función error."""
    return sqrt(pi) / 2.0 * erf(1)


def reportar_error(nombre, aproximacion, exacto):
    """Imprime una línea comparando el resultado del método con el valor exacto."""
    error = abs(aproximacion - exacto)
    print(f"{nombre:<30} = {aproximacion:.10f} | error absoluto = {error:.3e}")


def graficar_area(xs, ys, funcion, titulo):
    """
    Dibuja la curva real de la función junto con el polígono formado por
    los nodos (xs, ys) del método: se aprecia dónde la aproximación
    recorta o sobrepasa el área verdadera bajo la curva.
    """
    a, b = min(xs), max(xs)
    x_curva = np.linspace(a, b, 400)

    plt.figure(figsize=(10, 6))
    plt.plot(x_curva, funcion(x_curva), 'b-', linewidth=2, label='$f(x)$')
    plt.fill_between(xs, ys, alpha=0.35, color='darkorange', label='Área aproximada')

    # Trazos verticales punteados en cada nodo y su valor evaluado
    for xi, yi in zip(xs, ys):
        plt.plot([xi, xi], [0, yi], color='gray', linestyle=':', linewidth=1)
        plt.plot(xi, yi, 'ro', markersize=6)

    plt.title(titulo)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', alpha=0.3)
    plt.show()
