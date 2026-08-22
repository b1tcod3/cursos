"""
MÓDULO DE INTEGRACIÓN NUMÉRICA: CUADRATURA DE GAUSS-LEGENDRE

Este script implementa la cuadratura gaussiana con los nodos óptimos:
en lugar de fijarlos por conveniencia (equiespaciados), se eligen NODOS
Y PESOS para maximizar la exactitud. Con n evaluaciones alcanza el
grado de precisión 2n-1: el doble que cualquier fórmula de Newton-Cotes.

ALGORITMO:
1. Calcular las raíces x_i del polinomio de Legendre P_n (vía método de
   Newton, evaluando P_n y P'_n con la recurrencia de tres términos).
2. Calcular los pesos w_i = 2 / [(1 - x_i²) · (P_n'(x_i))²].
3. Mapear [-1, 1] al intervalo real [a, b]:
       x = (a+b)/2 + (b-a)/2 · t   →   ∫ₐᵇ f dx = (b-a)/2 · Σ w_i f(x_i)

PROPIEDADES:
- Exacta para todo polinomio de grado ≤ 2n-1.
- Todos los pesos son positivos: no amplifica errores de redondeo.
"""

import numpy as np

from integracion_util import (
    funcion_prueba,
    reportar_error,
    valor_exacto,
)


def legendre_y_derivada(n, x):
    """
    Evalúa simultáneamente P_n(x) y su derivada usando la recurrencia
    de tres términos: (k+1)·P_{k+1} = (2k+1)·x·P_k - k·P_{k-1}.
    La derivada sale de: P_n'(x) = n·(x·P_n(x) - P_{n-1}(x)) / (x² - 1).
    """
    p_anterior, p_actual = 1.0, x  # P_0 y P_1
    for k in range(1, n):
        p_anterior, p_actual = p_actual, ((2 * k + 1) * x * p_actual - k * p_anterior) / (k + 1)
    derivada = n * (x * p_actual - p_anterior) / (x**2 - 1)
    return p_actual, derivada


def nodos_y_pesos_legendre(n):
    """
    Raíces de P_n por Newton y sus pesos asociados.
    Semillas iniciales cos(π(i - 0.25)/(n + 0.5)): garantizan convergencia.
    """
    xs = np.cos(np.pi * (np.arange(1, n + 1) - 0.25) / (n + 0.5))
    pesos = np.zeros(n)

    for i in range(n):
        raiz = xs[i]
        # Newton itera hasta clavar la raíz de P_n
        for _ in range(100):
            p, dp = legendre_y_derivada(n, raiz)
            delta = -p / dp
            raiz += delta
            if abs(delta) < 1e-14:
                break
        _, dp = legendre_y_derivada(n, raiz)
        xs[i] = raiz
        pesos[i] = 2.0 / ((1.0 - raiz**2) * dp**2)

    return xs, pesos


def gauss_legendre(f, a, b, n):
    """
    Cuadratura gaussiana de n puntos sobre [a, b].
    Retorna la aproximación y los nodos mapeados (para inspección).
    """
    t, w = nodos_y_pesos_legendre(n)

    print(f"Gauss-Legendre n={n}: nodos en t ∈ [-1,1]: {np.round(t, 6)}")
    print(f"{'':>20}pesos: {np.round(w, 6)}")

    # Cambio de variable del intervalo canónico [-1,1] al real [a,b]
    x_mapeado = (a + b) / 2 + (b - a) / 2 * t
    return (b - a) / 2 * np.sum(w * f(x_mapeado)), x_mapeado


# --- EJECUCIÓN DEL EJEMPLO ---

# Integral de prueba del curso: I = ∫₀¹ e^(-x²) dx (sin primitiva elemental)
f = funcion_prueba()
a, b = 0, 1
exacto = valor_exacto()

print("Integral de prueba: ∫₀¹ e^(-x²) dx")
print(f"Valor exacto:       {exacto:.10f}\n")

for n in [2, 3, 4]:
    valor, _ = gauss_legendre(f, a, b, n)
    print()
    reportar_error(f"Gauss-Legendre n={n}", valor, exacto)
    print()

# El argumento decisivo: precisión POR EVALUACIÓN.
# Trapecio simple (2 evals): error ~6e-2 | Gauss n=2 (2 evals): error ~2e-4
print("Comparación con 3 evaluaciones de f:")
reportar_error("Trapecio compuesto n=2", (f(0) + 2 * f(0.5) + f(1)) / 4, exacto)
g3, _ = gauss_legendre(f, a, b, 3)
reportar_error("Gauss-Legendre n=3", g3, exacto)
