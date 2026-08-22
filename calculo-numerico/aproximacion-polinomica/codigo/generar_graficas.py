"""
GENERADOR DE FIGURAS PARA LA INTERPOLACIÓN POLINÓMICA

Produce las imágenes estáticas incrustadas en interpolacion-polinomica.md.
Ejecutar desde cualquier ubicación:

    python3 generar_graficas.py

Las figuras se guardan en ../imagenes/ (relativo a este script).
Implementación autocontenida: solo requiere numpy y matplotlib.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

CARPETA_SALIDA = Path(__file__).resolve().parent.parent / "imagenes"

COLOR_FUNCION = "#222222"
COLOR_EQUISPACIADO = "#d62728"
COLOR_CHEBYSHEV = "#2ca02c"
COLOR_POLINOMIO_GLOBAL = "#9467bd"
COLOR_SPLINE = "#1f77b4"
COLOR_SEGMENTARIA = "#ff7f0e"

DPI = 150


def runge(x):
    """La campana de Runge clásica."""
    return 1.0 / (1.0 + 25.0 * x**2)


def nodos_equispaciados(n, a=-1.0, b=1.0):
    return np.linspace(a, b, n + 1)


def nodos_chebyshev(n, a=-1.0, b=1.0):
    """Raíces de T_{n+1} mapeadas al intervalo [a, b]."""
    k = np.arange(n + 1)
    x = np.cos((2 * k + 1) * np.pi / (2 * (n + 1)))
    return (a + b) / 2 + (b - a) / 2 * x


def coeficientes_newton(x_nodos, y_nodos):
    """Coeficientes de las diferencias divididas (diagonal superior)."""
    n = len(x_nodos)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y_nodos
    for j in range(1, n):
        tabla[: n - j, j] = (
            tabla[1 : n - j + 1, j - 1] - tabla[: n - j, j - 1]
        ) / (x_nodos[j:] - x_nodos[: n - j])
    return tabla[0]


def evaluar_newton(coeficientes, x_nodos, x_eval):
    """Forma anidada de Newton (esquema de Horner hacia atrás)."""
    x_nodos = np.asarray(x_nodos, dtype=float)
    resultado = np.full_like(np.asarray(x_eval, dtype=float), coeficientes[-1])
    for k in range(len(coeficientes) - 2, -1, -1):
        resultado = resultado * (x_eval - x_nodos[k]) + coeficientes[k]
    return resultado


def interpolar_newton(x_nodos, y_nodos, x_eval):
    return evaluar_newton(coeficientes_newton(x_nodos, y_nodos), x_nodos, x_eval)


def spline_cubico_natural(x_nodos, y_nodos):
    """
    Retorna una función que evalúa el spline cúbico natural definido en los
    nodos dados (segundas derivadas continuas, S''(extremos) = 0).
    """
    x_nodos = np.asarray(x_nodos, dtype=float)
    y_nodos = np.asarray(y_nodos, dtype=float)
    h = np.diff(x_nodos)

    sistema = np.zeros((len(h) - 1, len(h) - 1))
    rhs = np.zeros(len(h) - 1)
    for i in range(1, len(h)):
        rhs[i - 1] = 6 * ((y_nodos[i + 1] - y_nodos[i]) / h[i] - (y_nodos[i] - y_nodos[i - 1]) / h[i - 1])
        if i > 1:
            sistema[i - 1, i - 2] = h[i - 1]
        sistema[i - 1, i - 1] = 2 * (h[i - 1] + h[i])
        if i < len(h) - 1:
            sistema[i - 1, i] = h[i]

    m = np.concatenate(([0.0], np.linalg.solve(sistema, rhs), [0.0]))

    def evaluar(x_eval):
        x_eval = np.asarray(x_eval, dtype=float)
        indice = np.clip(np.searchsorted(x_nodos, x_eval, side="right") - 1, 0, len(h) - 1)
        hi = h[indice]
        xl, xr = x_nodos[indice], x_nodos[indice + 1]
        yl, yr = y_nodos[indice], y_nodos[indice + 1]
        ml, mr = m[indice], m[indice + 1]
        a_izq = (xr - x_eval) / hi
        a_der = (x_eval - xl) / hi
        return (
            a_izq * yl
            + a_der * yr
            + ((a_izq**3 - a_izq) * ml + (a_der**3 - a_der) * mr) * hi**2 / 6
        )

    return evaluar


def polinomio_lineal_a_trozos(x_nodos, y_nodos):
    """Interpolación lineal segmentaria (clase C0)."""
    return lambda x_eval: np.interp(x_eval, x_nodos, y_nodos)


def polinomio_taylor_sin(grado, x_eval):
    """Polinomio de Taylor de sin(x) centrado en 0 (solo términos impares)."""
    resultado = np.zeros_like(np.asarray(x_eval, dtype=float))
    for k in range(1, grado + 1, 2):
        signo = (-1) ** ((k - 1) // 2)
        resultado += signo * x_eval**k / math.factorial(k)
    return resultado


def nueva_figura(titulo):
    figura, eje = plt.subplots(figsize=(8.5, 5))
    eje.grid(True, alpha=0.3)
    eje.axhline(0, color="k", alpha=0.3)
    eje.set_xlabel("$x$")
    eje.set_ylabel("$y$")
    eje.set_title(titulo)
    return figura, eje


def guardar(figura, nombre):
    CARPETA_SALIDA.mkdir(exist_ok=True)
    destino = CARPETA_SALIDA / nombre
    figura.savefig(destino, dpi=DPI, bbox_inches="tight")
    plt.close(figura)
    print(f"Generada: {destino}")


def graficar_runge_equispaciados():
    """Fenómeno de Runge: grados crecientes con nodos equiespaciados."""
    x_fino = np.linspace(-1, 1, 1000)

    figura, eje = nueva_figura(
        "Fenómeno de Runge — Polinomios globales con nodos equiespaciados"
    )
    eje.plot(x_fino, runge(x_fino), COLOR_FUNCION, "--", linewidth=2,
             label=r"$f(x)=\frac{1}{1+25x^2}$")

    for grado, color in zip((4, 10, 16), ("#f4a261", "#e76f51", "#9b2226")):
        nodos = nodos_equispaciados(grado)
        eje.plot(x_fino, interpolar_newton(nodos, runge(nodos), x_fino), color,
                 linewidth=1.8, label=f"$P_{{{grado}}}(x)$ equiespaciado")

    eje.plot([], [], " ", label=" ")  # separador visual
    nodos_mayores = nodos_equispaciados(16)
    eje.plot(nodos_mayores, runge(nodos_mayores), "o", color="#555555",
             markersize=4.5, label="Nodos ($n=16$)")

    eje.set_ylim(-0.6, 1.8)
    eje.legend(loc="upper center", fontsize=9, ncol=2)
    guardar(figura, "runge-equispaciados.png")


def graficar_chebyshev_vs_equispaciados():
    """Mismo grado alto: equiespaciado oscila, Chebyshev se ajusta."""
    grado = 16
    x_fino = np.linspace(-1, 1, 1000)

    figura, eje = nueva_figura(
        f"Nodos equiespaciados vs. nodos de Chebyshev (grado {grado})"
    )
    eje.plot(x_fino, runge(x_fino), COLOR_FUNCION, "--", linewidth=2,
             label=r"$f(x)=\frac{1}{1+25x^2}$")

    nodos_eq = nodos_equispaciados(grado)
    eje.plot(x_fino, interpolar_newton(nodos_eq, runge(nodos_eq), x_fino),
             COLOR_EQUISPACIADO, linewidth=1.8,
             label=f"Equispaciados ($P_{{{grado}}}$)")
    eje.plot(nodos_eq, runge(nodos_eq), "o", color=COLOR_EQUISPACIADO,
             markersize=4.5)

    nodos_ch = nodos_chebyshev(grado)
    eje.plot(x_fino, interpolar_newton(nodos_ch, runge(nodos_ch), x_fino),
             COLOR_CHEBYSHEV, linewidth=2.2,
             label=f"Chebyshev ($P_{{{grado}}}$)")
    eje.plot(nodos_ch, runge(nodos_ch), "o", color=COLOR_CHEBYSHEV,
             markersize=4.5)

    eje.set_ylim(-0.5, 1.5)
    eje.legend(loc="upper center", fontsize=10)
    guardar(figura, "chebyshev-vs-equispaciados.png")


def graficar_spline_vs_global():
    """Polinomio global oscilando frente al spline cúbico suave."""
    grado = 12
    nodos = nodos_equispaciados(grado)
    x_fino = np.linspace(-1, 1, 1000)

    figura, eje = nueva_figura(
        "Polinomio global vs. Spline cúbico natural (12 nodos)"
    )
    eje.plot(x_fino, runge(x_fino), COLOR_FUNCION, "--", linewidth=2,
             label=r"$f(x)=\frac{1}{1+25x^2}$")
    eje.plot(x_fino, interpolar_newton(nodos, runge(nodos), x_fino),
             COLOR_POLINOMIO_GLOBAL, linewidth=1.8,
             label=f"Polinomio global $P_{{{grado}}}$")
    eje.plot(x_fino, spline_cubico_natural(nodos, runge(nodos))(x_fino),
             COLOR_SPLINE, linewidth=2.4, label="Spline cúbico natural")
    eje.plot(nodos, runge(nodos), "o", color="#555555", markersize=5,
             label="Nodos")

    eje.set_ylim(-0.5, 1.5)
    eje.legend(loc="upper center", fontsize=10)
    guardar(figura, "spline-vs-global.png")


def graficar_segmentaria_vs_spline():
    """Picos C0 de la lineal segmentaria frente a la suavidad del spline."""
    x_nodos = np.linspace(0, 10, 9)
    y_nodos = np.sin(x_nodos)
    x_fino = np.linspace(0, 10, 1000)

    figura, eje = nueva_figura("Segmentaria lineal (C⁰) vs. Spline cúbico (C²)")
    eje.plot(x_fino, np.sin(x_fino), COLOR_FUNCION, "--", linewidth=2,
             label=r"$f(x)=\sin(x)$")
    eje.plot(x_fino, polinomio_lineal_a_trozos(x_nodos, y_nodos)(x_fino),
             COLOR_SEGMENTARIA, "-.", linewidth=2,
             label="Lineal a trozos (con picos)")
    eje.plot(x_fino, spline_cubico_natural(x_nodos, y_nodos)(x_fino),
             COLOR_SPLINE, linewidth=2.4, label="Spline cúbico natural")
    eje.plot(x_nodos, y_nodos, "o", color="#555555", markersize=6,
             label="Nodos")

    eje.legend(loc="upper right", fontsize=10)
    guardar(figura, "segmentaria-vs-spline.png")


def graficar_taylor_local():
    """Taylor: imbatible cerca del punto base, diverge al alejarse."""
    x_fino = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    colores = plt.cm.viridis(np.linspace(0.15, 0.85, 5))

    figura, eje = nueva_figura(
        r"Aproximación local: Taylor de $f(x)=\sin(x)$ centrado en $x_0=0$"
    )
    eje.plot(x_fino, np.sin(x_fino), COLOR_FUNCION, "--", linewidth=2.2,
             label=r"$\sin(x)$")

    for grado, color in zip((1, 3, 5, 7, 9), colores):
        eje.plot(x_fino, polinomio_taylor_sin(grado, x_fino), color=color,
                 linewidth=1.8, label=f"$T_{{{grado}}}(x)$")

    eje.set_ylim(-2.5, 2.5)
    eje.legend(loc="upper left", fontsize=9, ncol=2)
    guardar(figura, "taylor-local.png")


if __name__ == "__main__":
    graficar_runge_equispaciados()
    graficar_chebyshev_vs_equispaciados()
    graficar_spline_vs_global()
    graficar_segmentaria_vs_spline()
    graficar_taylor_local()
    print("Listo.")
