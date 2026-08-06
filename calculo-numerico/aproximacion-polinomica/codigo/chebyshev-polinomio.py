import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from interpolacion_util import construir_polinomio_newton  # Utilidades compartidas


def nodos_chebyshev(n, a=-1, b=1):
    """
    Genera n+1 nodos de Chebyshev en el intervalo [a, b].
    n: grado del polinomio
    a, b: extremos del intervalo
    """
    nodos = np.array([
        np.cos((2 * k + 1) / (2 * (n + 1)) * np.pi)
        for k in range(n + 1)
    ])
    t_k = (a + b) / 2 + (b - a) / 2 * nodos
    return t_k


def funcion_runge(x):
    """Función clásica de Runge."""
    return 1 / (1 + 25 * x**2)


# --- EJECUCIÓN DEL EJEMPLO ---

# Comparación: nodos equiespaciados vs Chebyshev para f(x) = 1/(1+25x^2)
n = 7
a, b = -1, 1

# Nodos equiespaciados
x_equi = np.linspace(a, b, n + 1)
y_equi = funcion_runge(x_equi)

# Nodos de Chebyshev
x_cheb = nodos_chebyshev(n, a, b)
y_cheb = funcion_runge(x_cheb)

print("Nodos equiespaciados:")
print(f"  x: {np.round(x_equi, 4)}")
print(f"  y: {np.round(y_equi, 4)}\n")

print("Nodos de Chebyshev:")
print(f"  x: {np.round(x_cheb, 4)}")
print(f"  y: {np.round(y_cheb, 4)}\n")

# Construir polinomios con Newton
p_equi, x_var = construir_polinomio_newton(x_equi, y_equi)
p_cheb, _ = construir_polinomio_newton(x_cheb, y_cheb)

print(f"Polinomio con nodos equiespaciados (grado {n}):")
print(f"  P_equi(x) = {p_equi}\n")

print(f"Polinomio con nodos de Chebyshev (grado {n}):")
print(f"  P_cheb(x) = {p_cheb}\n")

# --- VISUALIZACIÓN ---

x_graf = np.linspace(a, b, 500)
f_real = funcion_runge(x_graf)
y_equi_graf = [float(p_equi.subs(x_var, xv)) for xv in x_graf]
y_cheb_graf = [float(p_cheb.subs(x_var, xv)) for xv in x_graf]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica 1: Nodos equiespaciados
ax1.plot(x_graf, f_real, 'k-', label=r'$f(x) = 1/(1+25x^2)$', linewidth=2)
ax1.plot(x_graf, y_equi_graf, 'r--', label=f'Interpolación (n={n})', linewidth=1.5)
ax1.plot(x_equi, y_equi, 'bo', label='Nodos equiespaciados', markersize=6)
ax1.set_title('Nodos Equiespaciados (Fenómeno de Runge)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-1, 2)

# Gráfica 2: Nodos de Chebyshev
ax2.plot(x_graf, f_real, 'k-', label=r'$f(x) = 1/(1+25x^2)$', linewidth=2)
ax2.plot(x_graf, y_cheb_graf, 'g--', label=f'Interpolación (n={n})', linewidth=1.5)
ax2.plot(x_cheb, y_cheb, 'bo', label='Nodos Chebyshev', markersize=6)
ax2.set_title('Nodos de Chebyshev (Error minimizado)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_ylim(-1, 2)

plt.tight_layout()
plt.show()
