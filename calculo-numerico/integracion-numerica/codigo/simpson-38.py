"""
MÓDULO DE INTEGRACIÓN NUMÉRICA: REGLA DE SIMPSON 3/8

Este script implementa la regla de Simpson 3/8 en sus versiones simple
y compuesta. Interpola un CUBO por cada cuatro puntos consecutivos.
Su nombre proviene del factor 3h/8 que multiplica la suma.

Es menos precisa que Simpson 1/3 para el mismo ancho (error 8 veces
mayor), pero es la pieza de empalme cuando el número de subintervalos
no es par: 5 subintervalos = un tramo de 3 (regla 3/8) + dos de a uno...

ALGORITMO (compuesto):
1. Dividir [a, b] en n subintervalos iguales (n múltiplo de 3).
2. Evaluar la función en los n+1 nodos resultantes.
3. Acumular: S = 3h/8 · [f0 + 3·(no múltiplos de 3) + 2·(múltiplos de 3) + fn].

PROPIEDADES:
- Grado de precisión 3: igual que Simpson 1/3, pese a usar más puntos.
- Error local: E = -(b-a)⁵/80 · f⁽⁴⁾(ξ).
- Orden global O(h⁴).
"""

import numpy as np

from integracion_util import (
    funcion_prueba,
    graficar_area,
    reportar_error,
    valor_exacto,
)


def simpson_38_simple(f, a, b):
    """Un solo cubo por los cuatro puntos equiespaciados de [a, b]."""
    h = (b - a) / 3
    return 3 * h / 8 * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))


def simpson_38_compuesto(f, a, b, n):
    """
    Aplica Simpson 3/8 encadenado sobre n subintervalos (n múltiplo de 3).
    Los nodos cuyo índice es múltiplo de 3 cierran un cubo y abren otro:
    por eso pesan 2; el resto de interiores pesa 3.
    """
    if n % 3 != 0:
        raise ValueError("Simpson 3/8 compuesta exige subintervalos múltiplos de 3.")

    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)

    print(f"Subintervalos: {n} | paso h = {h:.4f} | cubos: {n // 3}")
    print("-" * 50)

    # Extremos: peso 1 | múltiplos de 3 interiores: peso 2 | resto: peso 3
    suma = f(xs[0]) + f(xs[-1])
    for i in range(1, n):
        fi = f(xs[i])
        peso = 2 if i % 3 == 0 else 3
        suma += peso * fi
        print(f"f(x_{i}) = f({xs[i]:.4f}) = {fi:.10f}  (peso {peso})")

    return 3 * h / 8 * suma


# --- EJECUCIÓN DEL EJEMPLO ---

# Integral de prueba del curso: I = ∫₀¹ e^(-x²) dx (sin primitiva elemental)
f = funcion_prueba()
a, b = 0, 1
exacto = valor_exacto()

print("Integral de prueba: ∫₀¹ e^(-x²) dx")
print(f"Valor exacto:       {exacto:.10f}\n")

print("--- Simpson 3/8 simple ---\n")
s3 = simpson_38_simple(f, a, b)
reportar_error("Simpson 3/8 simple", s3, exacto)

print("\n--- Simpson 3/8 compuesta (n = 6) ---\n")
s6 = simpson_38_compuesto(f, a, b, 6)
print()
reportar_error("Simpson 3/8 compuesta n=6", s6, exacto)

# Comparación directa con Simpson 1/3 usando el mismo número de evaluaciones:
# ambos tienen grado de precisión 3, pero 1/3 gana por el ancho efectivo menor.
print("\nConvergencia del error:")
for n in [3, 6]:
    reportar_error(f"Simpson 3/8 compuesta n={n}", simpson_38_compuesto(f, a, b, n), exacto)

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

h = (b - a) / 3
xs3 = np.linspace(a, b, 4)
graficar_area(xs3, f(xs3), f, 'Regla de Simpson 3/8 Simple para $e^{-x^2}$')
