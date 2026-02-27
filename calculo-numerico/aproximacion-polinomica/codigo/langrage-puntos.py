import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    """Interpolación de Lagrange"""
    n = len(x_points)
    resultado = 0
    
    for i in range(n):
        termino = y_points[i]
        for j in range(n):
            if j != i:
                termino *= (x - x_points[j]) / (x_points[i] - x_points[j])
        resultado += termino
    
    return resultado

# Datos de ejemplo
x_datos = np.array([1, 2, 4, 7])
y_datos = np.array([3, 5, 9, 15])

# Puntos para graficar la función interpolante
x_grafica = np.linspace(min(x_datos), max(x_datos), 100)
y_grafica = [lagrange_interpolation(x_datos, y_datos, x) for x in x_grafica]

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(x_grafica, y_grafica, 'b-', label='Polinomio de Lagrange')
plt.plot(x_datos, y_datos, 'ro', label='Puntos conocidos', markersize=10)

# Interpolar un punto específico
x_interpolar = 3.5
y_interpolar = lagrange_interpolation(x_datos, y_datos, x_interpolar)
plt.plot(x_interpolar, y_interpolar, 'gs', label=f'Punto interpolado (x={x_interpolar})', markersize=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Polinomial de Lagrange')
plt.legend()
plt.grid(True)
plt.show()

print(f"El valor interpolado en x={x_interpolar} es: {y_interpolar}")
