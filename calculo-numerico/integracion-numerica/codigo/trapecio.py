"""
MÓDULO DE INTEGRACIÓN NUMÉRICA: REGLA DEL TRAPECIO

Este módulo implementa la regla del trapecio en sus versiones simple y
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

ESTRUCTURA DE MÓDULO PROFESIONAL:
Las funciones genéricas se definen arriba y la demostración vive bajo el
bloque `if __name__ == '__main__':`. Así puedes importar las funciones
sin efectos secundarios (`from trapecio import trapecio_compuesto`) o
ejecutar el archivo para ver los ejemplos funcionando.
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


def trapecio_compuesto(f, a, b, n, verbose=False):
    """
    Aplica el trapecio a n subintervalos iguales de [a, b].
    Recibe la función f, los extremos y el número de subdivisiones.
    Como buena herramienta de biblioteca es silenciosa por defecto;
    pasa verbose=True para ver el cálculo paso a paso.
    Retorna el valor aproximado de la integral.
    """
    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)

    if verbose:
        print(f"Subintervalos: {n} | paso h = {h:.4f}")
        print(f"Nodos: {np.round(xs, 4)}")
        print("-" * 50)

    # Extremos: peso 1 | Interiores: peso 2 (comparten dos trapecios)
    suma = f(xs[0]) + f(xs[-1])
    for i in range(1, n):
        fi = f(xs[i])
        suma += 2 * fi
        if verbose:
            print(f"f(x_{i}) = f({xs[i]:.4f}) = {fi:.10f}  (peso 2)")

    return h / 2 * suma


def application():
    """Demostración del módulo: dos problemas distintos, una misma herramienta."""
    # --- Problema 1: la gaussiana del curso (sin primitiva elemental) ---
    f = funcion_prueba()
    a, b = 0, 1
    exacto = valor_exacto()

    print("Problema 1: ∫₀¹ e^(-x²) dx")
    print(f"Valor exacto:       {exacto:.10f}\n")

    print("--- Trapecio simple ---\n")
    t1 = trapecio_simple(f, a, b)
    reportar_error("Trapecio simple", t1, exacto)

    print("\n--- Trapecio compuesto (n = 4) ---\n")
    t4 = trapecio_compuesto(f, a, b, 4, verbose=True)
    print()
    reportar_error("Trapecio compuesto n=4", t4, exacto)

    # El orden O(h²) se aprecia al refinar la malla: el error cae ×4 cada vez
    print("\nConvergencia del error (debe multiplicarse por ~4):")
    for n in [1, 2, 4, 8]:
        reportar_error(f"Trapecio compuesto n={n}", trapecio_compuesto(f, a, b, n), exacto)

    # --- Problema 2: física con la MISMA herramienta genérica ---
    from math import exp

    print("\nProblema 2: desplazamiento s = ∫₀¹ 3t²·e^(t³) dt (velocidad v(t))")
    v = lambda t: 3 * t**2 * exp(t**3)      # la función específica entra como argumento
    V = lambda t: exp(t**3)                 # antiderivada: valor exacto e - 1

    exacto_fisica = V(1) - V(0)
    for n in [4, 400]:
        numerical = trapecio_compuesto(v, 0, 1, n, verbose=(n == 4))
        reportar_error(f"Velocidad v(t), n={n}", numerical, exacto_fisica)    # --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---
    xs4 = np.linspace(a, b, 5)
    graficar_area(xs4, f(xs4), f, 'Regla del Trapecio Compuesta (n=4) para $e^{-x^2}$')


# EL BLOQUE MÁGICO: ejecuta la demo solo si corres este archivo directamente;
# si lo importas desde otro script, las funciones quedan disponibles en silencio.
if __name__ == '__main__':
    application()
