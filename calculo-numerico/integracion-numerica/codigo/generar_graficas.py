"""
GENERADOR DE FIGURAS PARA LA INTEGRACIÓN NUMÉRICA

Produce las imágenes estáticas incrustadas en integracion-numerica.md.
Ejecutar desde cualquier ubicación:

    python3 generar_graficas.py

Las figuras se guardan en ../imagenes/ (relativo a este script).
Implementación autocontenida: solo requiere numpy y matplotlib.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

CARPETA_SALIDA = Path(__file__).resolve().parent.parent / "imagenes"

COLOR_FUNCION = "#222222"
COLOR_TRAPECIO = "#d62728"
COLOR_SIMPSON = "#2ca02c"
COLOR_GAUSS = "#9467bd"
COLOR_ROMBERG = "#ff7f0e"

DPI = 150


def f(x):
    """La gaussiana e^(-x²): banco de pruebas común del tema."""
    return np.exp(-(x**2))


def valor_exacto():
    """I = ∫₀¹ e^(-x²) dx vía la función error (librería estándar de Python)."""
    from math import erf, pi, sqrt

    return sqrt(pi) / 2 * erf(1)


def trapecio_compuesto(n):
    xs = np.linspace(0.0, 1.0, n + 1)
    h = 1.0 / n
    return h / 2 * (f(xs[0]) + 2 * np.sum(f(xs[1:-1])) + f(xs[-1]))


def simpson_13_compuesto(n):
    if n % 2:
        raise ValueError("n debe ser par")
    xs = np.linspace(0.0, 1.0, n + 1)
    h = 1.0 / n
    y = f(xs)
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])


def romberg_diagonal(k):
    R = np.zeros((k + 1, k + 1))
    for i in range(k + 1):
        R[i, 0] = trapecio_compuesto(2**i)
    for j in range(1, k + 1):
        for i in range(j, k + 1):
            R[i, j] = (4**j * R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)
    return R[k, k]


def nodos_y_pesos_legendre(n):
    """Raíces de P_n por Newton (recurrencia de tres términos) y sus pesos."""
    def p_y_dp(x):
        p_ant, p_act = 1.0, x
        for k in range(1, n):
            p_ant, p_act = p_act, ((2 * k + 1) * x * p_act - k * p_ant) / (k + 1)
        dp = n * (x * p_act - p_ant) / (x**2 - 1)
        return p_act, dp

    xs = np.cos(np.pi * (np.arange(1, n + 1) - 0.25) / (n + 0.5))
    ws = np.zeros(n)
    for i in range(n):
        r = xs[i]
        for _ in range(100):
            p, dp = p_y_dp(r)
            delta = -p / dp
            r += delta
            if abs(delta) < 1e-14:
                break
        _, dp = p_y_dp(r)
        xs[i], ws[i] = r, 2.0 / ((1.0 - r**2) * dp**2)
    return xs, ws


def gauss_legendre(n):
    t, w = nodos_y_pesos_legendre(n)
    x = 0.5 + 0.5 * t  # mapeo [-1,1] -> [0,1]
    return float(0.5 * np.sum(w * f(x)))


def figura_trapecio_vs_simpson():
    """La misma integral: cuerda vs parábola sobre tres puntos comunes."""
    xs = np.array([0.0, 0.5, 1.0])
    ys = f(xs)

    # Parábola de Simpson 1/3: Lagrange grado 2 por los tres puntos
    coef = np.polyfit(xs, ys, 2)
    x_fino = np.linspace(0, 1, 400)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_fino, f(x_fino), color=COLOR_FUNCION, lw=2.5,
            label="$f(x)=e^{-x^2}$")

    ax.fill_between([0, 1], [ys[0], ys[2]], color=COLOR_TRAPECIO, alpha=0.25)
    ax.plot([0, 1], [ys[0], ys[2]], color=COLOR_TRAPECIO, lw=2,
            label=f"Trapecio = {trapecio_compuesto(1):.6f}")
    for xi, yi in zip([0, 1], [ys[0], ys[2]]):
        ax.plot([xi, xi], [0, yi], color=COLOR_TRAPECIO, ls=":", lw=1.2)

    ax.fill_between(x_fino, np.polyval(coef, x_fino), color=COLOR_SIMPSON, alpha=0.20)
    ax.plot(x_fino, np.polyval(coef, x_fino), color=COLOR_SIMPSON, lw=2,
            label=f"Simpson 1/3 = {simpson_13_compuesto(2):.6f}")

    ax.plot(xs, ys, "ko", ms=7, zorder=5, label="Nodos comunes")
    ax.set_title("Trapecio vs Simpson 1/3 con los mismos puntos extremos")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="lower left")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="k", alpha=0.3)

    fig.tight_layout()
    fig.savefig(CARPETA_SALIDA / "trapecio-vs-simpson.png", dpi=DPI)
    plt.close(fig)


def figura_error_convergencia():
    """Error absoluto vs número de evaluaciones (escala log-log)."""
    exacto = valor_exacto()

    eval_trap, err_trap = [], []
    eval_simp, err_simp = [], []
    for k in range(1, 8):  # 2^k subintervalos
        n = 2**k
        eval_trap.append(n + 1)
        err_trap.append(abs(trapecio_compuesto(n) - exacto))
        eval_simp.append(n + 1)
        err_simp.append(abs(simpson_13_compuesto(n) - exacto))

    eval_romb, err_romb = [], []
    for i in range(1, 7):
        eval_romb.append(2**i + 1)
        err_romb.append(abs(romberg_diagonal(i) - exacto))

    eval_gauss, err_gauss = [], []
    for n in range(1, 9):
        eval_gauss.append(n)
        err_gauss.append(abs(gauss_legendre(n) - exacto))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(eval_trap, err_trap, "o-", color=COLOR_TRAPECIO, label="Trapecio compuesto ($O(h^2)$)")
    ax.loglog(eval_simp, err_simp, "s-", color=COLOR_SIMPSON, label="Simpson 1/3 ($O(h^4)$)")
    ax.loglog(eval_romb, err_romb, "^-", color=COLOR_ROMBERG, label="Romberg (diagonal)")
    ax.loglog(eval_gauss, err_gauss, "d-", color=COLOR_GAUSS, label="Gauss-Legendre ($n$ nodos)")

    ax.set_xlabel("Evaluaciones de $f$")
    ax.set_ylabel("Error absoluto")
    ax.set_title("Convergencia del error: $\\int_0^1 e^{-x^2}\\,dx$")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(loc="lower left")

    fig.tight_layout()
    fig.savefig(CARPETA_SALIDA / "error-convergencia.png", dpi=DPI)
    plt.close(fig)


def figura_gauss_nodos_pesos():
    """Nodos y pesos para n = 2, 3, 4, 5 sobre el intervalo canónico."""
    fig, ejes = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

    for ax, n in zip(ejes, [2, 3, 4, 5]):
        t, w = nodos_y_pesos_legendre(n)
        ax.vlines(t, 0, w, color="gray", lw=1.2, ls=":")
        ax.bar(t, w, width=0.08, color="#1f77b4", alpha=0.85)
        ax.scatter(t, w, color="#d62728", zorder=5, s=40)
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(0, 1.25)
        ax.set_title(f"$n={n}$ (precisión {2*n-1})")
        ax.set_xticks([-1, 0, 1])
        ax.grid(True, axis="y", alpha=0.3)

    ejes[0].set_ylabel("Peso $w_i$")
    fig.suptitle("Nodos $x_i$ (rojo) y pesos $w_i$ de Gauss-Legendre en $[-1, 1]$ "
                 "(todos los pesos suman 2)")
    fig.tight_layout()
    fig.savefig(CARPETA_SALIDA / "gauss-nodos-pesos.png", dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    CARPETA_SALIDA.mkdir(exist_ok=True)
    print(f"Valor exacto de referencia: I = {valor_exacto():.16f}")
    figura_trapecio_vs_simpson()
    print("OK  trapecio-vs-simpson.png")
    figura_error_convergencia()
    print("OK  error-convergencia.png")
    figura_gauss_nodos_pesos()
    print("OK  gauss-nodos-pesos.png")
