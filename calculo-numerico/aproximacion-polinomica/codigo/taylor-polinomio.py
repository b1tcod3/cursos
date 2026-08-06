import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from interpolacion_util import evaluar_polinomio  # Utilidades compartidas


def polinomio_taylor(funcion, x0, n):
    """
    Construye el polinomio de Taylor de grado n para una función dada,
    centrado en x0.
    funcion: expresión simbólica de f(x)
    x0: punto base
    n: grado del polinomio
    """
    x = sp.Symbol('x')
    P = 0
    f_k = funcion

    print(f"Construcción del Polinomio de Taylor (grado {n}, centrado en x₀={x0}):")
    print("-" * 60)

    for k in range(n + 1):
        if k == 0:
            derivada_en_x0 = float(funcion.subs(x, x0))
        else:
            f_k = sp.diff(f_k, x)
            derivada_en_x0 = float(f_k.subs(x, x0))

        termino = derivada_en_x0 / sp.factorial(k) * (x - x0)**k
        P += termino
        print(f"k={k}: f^({k})({x0}) = {derivada_en_x0:8.5f}  →  término = {termino}")

    print("-" * 60)
    return sp.simplify(P), x


def error_taylor(funcion, x0, n):
    """
    Calcula el error de truncamiento (resto de Lagrange) simbólicamente.
    """
    x = sp.Symbol('x')
    xi = sp.Symbol('xi')

    derivada_n1 = funcion
    for _ in range(n + 1):
        derivada_n1 = sp.diff(derivada_n1, x)

    resto = derivada_n1.subs(x, xi) / sp.factorial(n + 1) * (x - x0)**(n + 1)
    return resto


# --- EJECUCIÓN DEL EJEMPLO ---

x = sp.Symbol('x')
f = sp.exp(x)
x0 = 0
n = 3

print("Función: f(x) = eˣ")
print(f"Punto base: x₀ = {x0}")
print(f"Grado del polinomio: n = {n}\n")

P, _ = polinomio_taylor(f, x0, n)

print(f"\nP_{n}(x) = {P}")
print()

# Evaluación y comparación
x_eval = 0.5
aprox = float(evaluar_polinomio(P, x_eval))
real = float(evaluar_polinomio(f, x_eval))
error_abs = abs(real - aprox)
error_pct = error_abs / real * 100

print(f"Evaluación en x = {x_eval}:")
print(f"  Aproximación P_{n}({x_eval}) = {aprox:.6f}")
print(f"  Valor real      e^{x_eval}  = {real:.6f}")
print(f"  Error absoluto              = {error_abs:.6f}")
print(f"  Error relativo              = {error_pct:.4f}%")

# Resto de Lagrange
resto = error_taylor(f, x0, n)
print(f"\nResto de Lagrange: R_{n}(x) = {resto}")

# --- VISUALIZACIÓN ---

x_graf = np.linspace(-1, 2, 400)
f_real = [float(evaluar_polinomio(f, xv)) for xv in x_graf]
f_aprox = [float(evaluar_polinomio(P, xv)) for xv in x_graf]
f_error = [abs(real_i - aprox_i) for real_i, aprox_i in zip(f_real, f_aprox)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica 1: Comparación función vs polinomio
ax1.plot(x_graf, f_real, 'k-', label=r'$f(x) = e^x$', linewidth=2)
ax1.plot(x_graf, f_aprox, 'r--', label=f'$P_{n}(x)$ (Taylor)', linewidth=1.5)
ax1.axvline(x=x0, color='gray', linestyle=':', alpha=0.7, label=f'$x_0={x0}$')
ax1.plot(x_eval, aprox, 'bo', label=f'$P({x_eval})={aprox:.4f}$', markersize=8)
ax1.plot(x_eval, real, 'go', label=f'$e^{{{x_eval}}}={real:.4f}$', markersize=8)
ax1.set_title('Polinomio de Taylor vs Función Real')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfica 2: Error absoluto
ax2.plot(x_graf, f_error, 'm-', linewidth=2)
ax2.axvline(x=x0, color='gray', linestyle=':', alpha=0.7)
ax2.set_title(f'Error Absoluto |f(x) - P_{n}(x)|')
ax2.set_xlabel('x')
ax2.set_ylabel('Error')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
