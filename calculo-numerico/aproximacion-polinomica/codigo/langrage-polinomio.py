import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def obtener_polinomio_lagrange(x_points, y_points):
    """
    Obtiene el polinomio de interpolación de Lagrange en forma simbólica
    
    Parámetros:
    x_points: lista de puntos x conocidos
    y_points: lista de valores y correspondientes
    
    Retorna:
    polinomio: expresión simbólica del polinomio
    x: variable simbólica
    """
    x = sp.Symbol('x')
    n = len(x_points)
    polinomio = 0
    
    print("Construcción del polinomio de Lagrange:")
    print("-" * 50)
    
    for i in range(n):
        # Construir L_i(x)
        L_i = 1
        terminos_l = []
        for j in range(n):
            if j != i:
                termino = (x - x_points[j]) / (x_points[i] - x_points[j])
                L_i *= termino
                terminos_l.append(f"(x-{x_points[j]})/({x_points[i]}-{x_points[j]})")
        
        # Mostrar L_i(x)
        print(f"L_{i}(x) = {' * '.join(terminos_l)}")
        print(f"L_{i}(x) simplificado = {sp.simplify(L_i)}")
        print()
        
        # Agregar término al polinomio
        polinomio += y_points[i] * L_i
    
    print("-" * 50)
    print(f"P(x) = {polinomio}")
    print(f"P(x) simplificado = {sp.simplify(polinomio)}")
    
    return sp.simplify(polinomio), x

def evaluar_polinomio(polinomio, x_valor):
    """Evalúa el polinomio en un punto específico"""
    x = sp.Symbol('x')
    return polinomio.subs(x, x_valor)

# Ejemplo de uso
x_puntos = [0, 1, 2 , 3]
y_puntos = [-1,6,31, 18]

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}")
print()

polinomio, x_var = obtener_polinomio_lagrange(x_puntos, y_puntos)

# Evaluar en algunos puntos
print("\nEvaluaciones:")
for punto in [1, 2, 4, 7, 3.5]:
    valor = evaluar_polinomio(polinomio, punto)
    print(f"P({punto}) = {valor}")

# Visualización
x_vals = np.linspace(0, 8, 200)
y_vals = [float(evaluar_polinomio(polinomio, x)) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', label=f'P(x) = {polinomio}', linewidth=2)
plt.plot(x_puntos, y_puntos, 'ro', label='Puntos conocidos', markersize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio de Interpolación de Lagrange')
plt.legend()
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.show()
