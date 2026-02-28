import sympy as sp  # Biblioteca para cálculo simbólico (maneja la 'x' como variable)
import numpy as np  # Para crear arreglos numéricos y rangos
import matplotlib.pyplot as plt  # Para generar la gráfica final

def obtener_polinomio_lagrange(x_points, y_points):
    """
    Construye el polinomio P(x) que pasa por todos los puntos (X, Y). Polinomio de interpolación de Lagrange.
    Recibe dos listas: x_points (valores de x) y y_points (valores de y correspondientes). Retorna el polinomio simbólico y la variable 'x' para evaluaciones posteriores.
    """
    # 1. Definimos 'x' como un símbolo matemático, no como un número
    x = sp.Symbol('x')
    
    # 2. 'n' es la cantidad de puntos; definirá el grado del polinomio (n-1)
    n = len(x_points)
    
    # 3. Aquí iremos sumando cada término: P(x) = L0*y0 + L1*y1 + ...
    polinomio = 0
    
    print("Construcción del polinomio de Lagrange:")
    print("-" * 50)
    
    # Bucle externo: recorre cada punto 'i' para calcular su base L_i(x)
    for i in range(n):
        L_i = 1  # Inicializamos el producto en 1
        terminos_l = [] # Lista auxiliar solo para mostrar el proceso en consola
        
        # Bucle interno: construye el producto (x - xj) / (xi - xj) para j != i
        for j in range(n):
            if j != i:
                # Aplicamos la fórmula: Termino = (x - x_j) / (x_i - x_j)
                termino = (x - x_points[j]) / (x_points[i] - x_points[j])
                
                # Vamos multiplicando para obtener el polinomio base L_i
                L_i *= termino
                
                # Guardamos la representación en texto para el print
                terminos_l.append(f"(x-{x_points[j]})/({x_points[i]}-{x_points[j]})")
        
        # Mostramos en consola cómo se va viendo cada L_i
        print(f"L_{i}(x) = {' * '.join(terminos_l)}")
        print(f"L_{i}(x) simplificado = {sp.simplify(L_i)}")
        print()
        
        # El polinomio final suma: y_i * L_i(x)
        polinomio += y_points[i] * L_i
    
    print("-" * 50)
    # Mostramos el polinomio total sin simplificar y luego simplificado (agrupado)
    print(f"P(x) = {polinomio}")
    print(f"P(x) simplificado = {sp.simplify(polinomio)}")
    
    # Retornamos el polinomio limpio y la variable simbólica para usarla después
    return sp.simplify(polinomio), x

def evaluar_polinomio(polinomio, x_valor):
    """
    Toma el polinomio simbólico y reemplaza la 'x' por un valor real.
    """
    x = sp.Symbol('x')
    # .subs() es 'substitute': cambia x por el valor deseado
    return polinomio.subs(x, x_valor)

# --- EJECUCIÓN DEL EJEMPLO ---

# Definimos los puntos conocidos (nodos)
x_puntos = [0, 1, 2, 3]
y_puntos = [-1, 6, 31, 18]

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}\n")

# Llamada principal para obtener la fórmula del polinomio
polinomio, x_var = obtener_polinomio_lagrange(x_puntos, y_puntos)

# Probamos el polinomio evaluando puntos que NO estaban en la lista original
print("\nEvaluaciones:")
for punto in [-1,-2, 4, 7]:
    valor = evaluar_polinomio(polinomio, punto)
    print(f"P({punto}) = {valor}")

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

# Creamos 200 puntos entre 0 y 8 para dibujar una curva suave
x_vals = np.linspace(0, 8, 200)

# Evaluamos cada uno de esos 200 puntos en nuestro polinomio
# Convertimos a float() porque matplotlib no entiende símbolos de SymPy
y_vals = [float(evaluar_polinomio(polinomio, x)) for x in x_vals]

plt.figure(figsize=(10, 6))
# Dibujamos la línea azul del polinomio interpolado
plt.plot(x_vals, y_vals, 'b-', label=f'P(x) = {polinomio}', linewidth=2)
# Dibujamos los puntos originales como puntos rojos
plt.plot(x_puntos, y_puntos, 'ro', label='Puntos conocidos', markersize=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio de Interpolación de Lagrange')
plt.legend()
plt.grid(True)
# Dibujamos los ejes X e Y para referencia
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.show()
