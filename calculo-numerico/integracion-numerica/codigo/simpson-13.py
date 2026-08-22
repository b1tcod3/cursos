"""
MÓDULO DE INTEGRACIÓN NUMÉRICA: REGLA DE SIMPSON 1/3

Este script implementa la regla de Simpson 1/3 en sus versiones simple
y compuesta. En lugar de una recta, interpola una PARÁBOLA por cada
trío de puntos consecutivos, capturando parte de la curvatura de f.

ALGORITMO (compuesto):
1. Dividir [a, b] en n subintervalos iguales (n debe ser PAR) de ancho h.
2. Evaluar la función en los n+1 nodos resultantes.
3. Acumular: S = h/3 · [f0 + 4·(suma de impares) + 2·(suma de pares) + fn].
   - Peso 4: nodos impares = punto medio de cada parábola.
   - Peso 2: nodos pares interiores = extremo compartido entre dos parábolas.

PROPIEDADES:
- Grado de precisión 3 (¡no 2!): el término cúbico se cancela por simetría.
- Error local: E = -(b-a)⁵/180 · f⁽⁴⁾(ξ).
- Orden global O(h⁴): duplicar los subintervalos reduce el error ×16.
"""

import numpy as np

from integracion_util import (
    funcion_prueba,
    graficar_area,
    reportar_error,
    valor_exacto,
)


def simpson_13_simple(f, a, b):
    """Una sola parábola por los extremos y el punto medio de [a, b]."""
    h = (b - a) / 2
    return h / 3 * (f(a) + 4 * f((a + b) / 2) + f(b))


def simpson_13_compuesto(f, a, b, n):
    """
    Aplica Simpson 1/3 a n/2 parábolas encadenadas sobre [a, b].
    Lanza un error si n no es par: sin esa condición los tramos no cierran.
    """
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 compuesta exige un número PAR de subintervalos.")

    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)

    print(f"Subintervalos: {n} | paso h = {h:.4f} | parábolas: {n // 2}")
    print("-" * 50)

    # Recorremos los pesos alternantes 1,4,2,4,...,2,4,1
    suma = f(xs[0]) + f(xs[-1])
    for i in range(1, n):
        fi = f(xs[i])
        peso = 4 if i % 2 == 1 else 2
        suma += peso * fi
        print(f"f(x_{i}) = f({xs[i]:.4f}) = {fi:.10f}  (peso {peso})")

    return h / 3 * suma


# --- EJECUCIÓN DEL EJEMPLO ---

# Integral de prueba del curso: I = ∫₀¹ e^(-x²) dx (sin primitiva elemental)
f = funcion_prueba()
a, b = 0, 1
exacto = valor_exacto()

print("Integral de prueba: ∫₀¹ e^(-x²) dx")
print(f"Valor exacto:       {exacto:.10f}\n")

print("--- Simpson 1/3 simple ---\n")
s1 = simpson_13_simple(f, a, b)
reportar_error("Simpson 1/3 simple", s1, exacto)

print("\n--- Simpson 1/3 compuesta (n = 4) ---\n")
s4 = simpson_13_compuesto(f, a, b, 4)
print()
reportar_error("Simpson 1/3 compuesta n=4", s4, exacto)

# Con las mismas evaluaciones que el trapecio compuesto n=4,
# el error cae más de dos órdenes de magnitud: ese es el orden extra.
print("\nConvergencia del error (debe multiplicarse por ~16):")
for n in [2, 4, 8]:
    reportar_error(f"Simpson 1/3 compuesta n={n}", simpson_13_compuesto(f, a, b, n), exacto)

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

h = (b - a) / 4
xs4 = np.linspace(a, b, 5)
graficar_area(xs4, f(xs4), f, 'Regla de Simpson 1/3 Compuesta (n=4) para $e^{-x^2}$')
