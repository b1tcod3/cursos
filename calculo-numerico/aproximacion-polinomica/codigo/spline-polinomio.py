import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from interpolacion_util import evaluar_por_tramos  # Utilidades compartidas

def resolver_sistema_tridiagonal(h, a, tipo="natural", dy_extremos=None):
    """
    Resuelve el sistema tridiagonal para encontrar los valores de c (segunda derivada).
    h: lista de distancias entre nodos (h_j = x_{j+1} - x_j)
    a: lista de valores de la función en cada nodo
    tipo: "natural" (c0=cn=0) o "clamped" (se especifica derivada en extremos)
    dy_extremos: [f'(x0), f'(xn)] para el caso clamped
    """
    n = len(a) - 1
    sistema = np.zeros((n - 1, n - 1))
    rhs = np.zeros(n - 1)

    for i in range(1, n):
        rhs[i - 1] = 3 * ((a[i + 1] - a[i]) / h[i] - (a[i] - a[i - 1]) / h[i - 1])
        if i > 1:
            sistema[i - 1, i - 2] = h[i - 1]
        sistema[i - 1, i - 1] = 2 * (h[i - 1] + h[i])
        if i < n - 1:
            sistema[i - 1, i] = h[i]

    # Condiciones de frontera
    if tipo == "natural":
        c0, cn = 0, 0
    elif tipo == "clamped" and dy_extremos is not None:
        rhs[0] -= h[0] * dy_extremos[0]
        rhs[-1] -= h[-1] * dy_extremos[1]
        c0 = dy_extremos[0]
        cn = dy_extremos[1]
    else:
        c0, cn = 0, 0

    c_int = np.linalg.solve(sistema, rhs)
    c = np.zeros(n + 1)

    if tipo == "natural":
        c[0], c[-1] = c0, cn
        c[1:-1] = c_int
    elif tipo == "clamped":
        c[0], c[-1] = c0, cn
        c[1:-1] = c_int

    return c


def obtener_spline(x_points, y_points, tipo="natural", dy_extremos=None):
    """
    Construye los polinomios de Spline Cúbico para cada subintervalo.
    Retorna la lista de polinomios simbólicos y la variable x.
    """
    x = sp.Symbol('x')
    n = len(x_points) - 1

    h = [x_points[i + 1] - x_points[i] for i in range(n)]
    a = y_points.copy()

    c = resolver_sistema_tridiagonal(h, a, tipo, dy_extremos)

    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    splines = []
    print("Construcción de los Splines Cúbicos:")
    print("-" * 50)

    print("\nCoeficientes calculados:")
    print(f"{'Tramo':<8} {'a_j':<10} {'b_j':<10} {'c_j':<10} {'d_j':<10}")
    print("-" * 50)

    for i in range(n):
        S_j = a[i] + b[i] * (x - x_points[i]) + c[i] * (x - x_points[i])**2 + d[i] * (x - x_points[i])**3
        splines.append((x_points[i], x_points[i + 1], S_j))
        print(f"S_{i}     {a[i]:<10.5f} {b[i]:<10.5f} {c[i]:<10.5f} {d[i]:<10.5f}")

    print("-" * 50)
    print("\nPolinomios resultantes:")
    for i, (xi, xf, S_j) in enumerate(splines):
        S_simplificado = sp.simplify(S_j)
        print(f"S_{i}(x) en [{xi}, {xf}]: {S_simplificado}")

    return splines, x


# --- EJECUCIÓN DEL EJEMPLO ---

x_puntos = [0, 1, 2]
y_puntos = [1, 2, 0]

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}\n")

splines, x_var = obtener_spline(x_puntos, y_puntos, tipo="natural")

print("\nVerificación en los nodos:")
for i in range(len(x_puntos)):
    val = evaluar_por_tramos(splines, x_puntos[i])
    print(f"S({x_puntos[i]}) = {val}")

print("\nEvaluaciones intermedias:")
for punto in [0.5, 1.5]:
    val = evaluar_por_tramos(splines, punto)
    print(f"S({punto}) = {val}")

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

x_vals_graf = np.linspace(0, 2, 300)
y_vals_graf = [evaluar_por_tramos(splines, x) for x in x_vals_graf]

plt.figure(figsize=(10, 6))
plt.plot(x_vals_graf, y_vals_graf, 'b-', label='Spline Cúbico Natural', linewidth=2)
plt.plot(x_puntos, y_puntos, 'ro', label='Puntos conocidos', markersize=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación por Splines Cúbicos (Spline Natural)')
plt.legend()
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.show()
