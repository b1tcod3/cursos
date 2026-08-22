"""
MÓDULO DE INTEGRACIÓN NUMÉRICA: EXTRAPOLACIÓN DE ROMBERG

Este script implementa la tabla de Romberg. La idea es explotar la
estructura del error del trapecio compuesto, que se desarrolla en
potencias PARES de h:  T(h) = I + c1·h² + c2·h⁴ + c3·h⁶ + ...

Combinando dos trapecios con pasos h y h/2 se cancela el término c1·h²;
repetiendo el truco sobre los resultados ya extrapolados se cancelan
los términos siguientes, ganando DOS órdenes de precisión por columna.

ALGORITMO:
1. Columna 0: trapecios compuestos con 2^i subintervalos (reciclando puntos).
2. Cada nueva columna aplica la fórmula de Richardson:
       R(i, j) = [4^j · R(i, j-1) - R(i-1, j-1)] / (4^j - 1)
3. La diagonal R(k, k) converge al valor exacto a velocidad espectacular.

PROPIEDADES:
- Orden O(h^(2j)) en la columna j.
- La diferencia entre diagonales consecutivas sirve de estimador de error.
"""

import numpy as np

from integracion_util import (
    funcion_prueba,
    reportar_error,
    valor_exacto,
)


def romberg(f, a, b, k):
    """
    Construye la tabla de Romberg hasta la fila k (2^k subintervalos).
    Retorna la matriz triangular inferior R y la mejor estimación R[k][k].
    """
    R = np.zeros((k + 1, k + 1))

    # --- Columna 0: trapecios cada vez más finos ---
    for i in range(k + 1):
        n = 2**i
        h = (b - a) / n
        xs = np.linspace(a, b, n + 1)
        if i == 0:
            # Primer trapecio: no hay nada que reciclar
            R[i, 0] = h / 2 * (f(xs[0]) + f(xs[-1]))
        else:
            # Truco clave: solo los nodos IMPARES son nuevos;
            # el resto ya fue evaluado por la fila anterior.
            nuevos = sum(f(xs[j]) for j in range(1, n, 2))
            R[i, 0] = R[i - 1, 0] / 2 + h * nuevos
            print(f"R({i},0): trapecio con {n} subintervalos = {R[i, 0]:.10f}")

    print("\nExtrapolaciones de Richardson:")
    # --- Columnas j ≥ 1: cancelamos la potencia 4^j del error ---
    for j in range(1, k + 1):
        factor = 4**j
        for i in range(j, k + 1):
            R[i, j] = (factor * R[i, j - 1] - R[i - 1, j - 1]) / (factor - 1)
        print(f"Columna {j} completa (orden O(h^{2*j}))")

    return R, R[k, k]


def imprimir_tabla(R):
    """Muestra la tabla triangular con formato legible."""
    print("\nTabla de Romberg:")
    print("-" * (14 * len(R)))
    for i in range(len(R)):
        fila = "  ".join(f"{R[i, j]:.10f}" if j <= i else " " * 12 for j in range(len(R)))
        print(f"fila {i}: {fila}")


# --- EJECUCIÓN DEL EJEMPLO ---

# Integral de prueba del curso: I = ∫₀¹ e^(-x²) dx (sin primitiva elemental)
f = funcion_prueba()
a, b = 0, 1
exacto = valor_exacto()

print("Integral de prueba: ∫₀¹ e^(-x²) dx")
print(f"Valor exacto:       {exacto:.10f}")

R, mejor = romberg(f, a, b, 4)
imprimir_tabla(R)

print()
reportar_error("Romberg R(4,4)", mejor, exacto)

# El estimador de error gratuito: distancia entre diagonales consecutivas
print("\nEstimación de error |R(i,i) - R(i-1,i-1)|:")
for i in range(1, len(R)):
    print(f"|R({i},{i}) - R({i-1},{i-1})| = {abs(R[i, i] - R[i-1, i-1]):.3e}")
