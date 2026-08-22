"""
MÓDULO DE INTEGRACIÓN NUMÉRICA: REGLA DEL TRAPECIO

Este script implementa la regla del trapecio en sus versiones simple y
compuesta. La idea es reemplazar la función por la recta que une los
puntos extremos de cada subintervalo y sumar las áreas de los trapecios.

ALGORITMO (compuesto):
1. Dividir [a, b] en n subintervalos iguales de ancho h = (b - a) / n.
2. Evaluar la función en los n+1 nodos resultantes.
3. Acumular: T = h/2 · [f(x0) + 2·f(x1) + ... + 2·f(x_{n-1}) + f(xn)].
   Los nodos interiores pesan doble porque comparten dos trapecios.

PROPIEDADES:
- Grado de precisión 1: integra exactamente rectas.
- Error local: E = -(b-a)³/12 · f''(ξ).
- Orden global O(h²): duplicar los subintervalos reduce el error ×4.
"""

import numpy as np

from integracion_util import (
    funcion_prueba,
    graficar_area,
    reportar_error,
    valor_exacto,
)


def trapecio_simple(f, a, b):
    """Un único trapecio sobre [a, b]: el método en su forma más básica."""
    return (b - a) / 2 * (f(a) + f(b))


def trapecio_compuesto(f, a, b, n):
    """
    Aplica el trapecio a n subintervalos iguales de [a, b].
    Recibe la función f, los extremos y el número de subdivisiones.
    Retorna el valor aproximado de la integral.
    """
    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)

    print(f"Subintervalos: {n} | paso h = {h:.4f}")
    print(f"Nodos: {np.round(xs, 4)}")
    print("-" * 50)

    # Extremos: peso 1 | Interiores: peso 2 (comparten dos trapecios)
    suma = f(xs[0]) + f(xs[-1])
    for i in range(1, n):
        fi = f(xs[i])
        suma += 2 * fi
        print(f"f(x_{i}) = f({xs[i]:.4f}) = {fi:.10f}  (peso 2)")

    return h / 2 * suma


# --- EJECUCIÓN DEL EJEMPLO ---

# Integral de prueba del curso: I = ∫₀¹ e^(-x²) dx (sin primitiva elemental)
f = funcion_prueba()
a, b = 0, 1
exacto = valor_exacto()

print("Integral de prueba: ∫₀¹ e^(-x²) dx")
print(f"Valor exacto:       {exacto:.10f}\n")

print("--- Trapecio simple ---\n")
t1 = trapecio_simple(f, a, b)
reportar_error("Trapecio simple", t1, exacto)

print("\n--- Trapecio compuesto (n = 4) ---\n")
t4 = trapecio_compuesto(f, a, b, 4)
print()
reportar_error("Trapecio compuesto n=4", t4, exacto)

# El orden O(h²) se aprecia al refinar la malla: el error cae ×4 cada vez
print("\nConvergencia del error (debe multiplicarse por ~4):")
for n in [1, 2, 4, 8]:
    reportar_error(f"Trapecio compuesto n={n}", trapecio_compuesto(f, a, b, n), exacto)

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

h = (b - a) / 4
xs4 = np.linspace(a, b, 5)
graficar_area(xs4, f(xs4), f, 'Regla del Trapecio Compuesta (n=4) para $e^{-x^2}$')
