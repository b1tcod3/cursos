import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from interpolacion_util import evaluar_por_tramos  # Utilidades compartidas


def interpolacion_segmentaria_lineal(x_points, y_points):
    """
    Construye la interpolación segmentaria lineal (grado 1).
    Retorna lista de polinomios por tramo y la variable simbólica x.
    """
    x = sp.Symbol('x')
    n = len(x_points) - 1
    tramos = []

    print("Construcción de la Interpolación Segmentaria Lineal:")
    print("-" * 50)

    for i in range(n):
        pendiente = (y_points[i + 1] - y_points[i]) / (x_points[i + 1] - x_points[i])
        P_i = y_points[i] + pendiente * (x - x_points[i])
        P_i_simpl = sp.simplify(P_i)
        tramos.append((x_points[i], x_points[i + 1], P_i_simpl))
        print(f"P_{i}(x) en [{x_points[i]}, {x_points[i+1]}]: {P_i_simpl}")

    print("-" * 50)
    return tramos, x


# --- EJECUCIÓN DEL EJEMPLO ---

x_puntos = [0, 2, 4]
y_puntos = [1, 5, 3]

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}\n")

tramos, x_var = interpolacion_segmentaria_lineal(x_puntos, y_puntos)

print("\nVerificación en los nodos:")
for i in range(len(x_puntos)):
    val = evaluar_por_tramos(tramos, x_puntos[i])
    print(f"P({x_puntos[i]}) = {val}")

print("\nEvaluaciones intermedias:")
for punto in [1, 3]:
    val = evaluar_por_tramos(tramos, punto)
    print(f"P({punto}) = {val}")

# --- VISUALIZACIÓN ---

x_graf = np.linspace(0, 4, 300)
y_graf = [evaluar_por_tramos(tramos, x) for x in x_graf]

plt.figure(figsize=(10, 6))
plt.plot(x_graf, y_graf, 'b-', label='Interpolación Segmentaria Lineal', linewidth=2)
plt.plot(x_puntos, y_puntos, 'ro', label='Puntos conocidos', markersize=10)

# Marcar los nodos interiores con líneas verticales punteadas
for i in range(1, len(x_puntos) - 1):
    plt.axvline(x=x_puntos[i], color='gray', linestyle='--', alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Segmentaria Lineal (A Trozos)')
plt.legend()
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.show()
