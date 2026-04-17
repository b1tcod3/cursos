import sympy as sp  # Biblioteca para cálculo simbólico (maneja la 'x' como variable)
import numpy as np  # Para crear arreglos numéricos y rangos
import matplotlib.pyplot as plt  # Para generar la gráfica final

def calcular_diferencias_divididas(x_points, y_points):
    """
    Calcula las diferencias divididas para el polinomio de Newton.
    Retorna una lista con los coeficientes del polinomio.
    """
    n = len(x_points)
    # Creamos una matriz para almacenar las diferencias divididas
    tabla = [[0 for _ in range(n)] for _ in range(n)]
    
    # Inicializamos la primera columna con los valores de y
    for i in range(n):
        tabla[i][0] = y_points[i]
    
    # Calculamos las diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x_points[i + j] - x_points[i])
    
    # Los coeficientes del polinomio son los valores de la diagonal superior
    coeficientes = [tabla[0][j] for j in range(n)]
    
    return coeficientes

def obtener_polinomio_newton(x_points, y_points):
    """
    Construye el polinomio P(x) usando el método de Newton de diferencias divididas.
    Recibe dos listas: x_points (valores de x) y y_points (valores de y correspondientes).
    Retorna el polinomio simbólico y la variable 'x' para evaluaciones posteriores.
    """
    # 1. Definimos 'x' como un símbolo matemático, no como un número
    x = sp.Symbol('x')
    
    # 2. Calculamos las diferencias divididas
    coeficientes = calcular_diferencias_divididas(x_points, y_points)
    
    # 3. Construimos el polinomio de Newton
    polinomio = coeficientes[0]
    terminos = [f"{coeficientes[0]}"]
    
    print("Construcción del polinomio de Newton:")
    print("-" * 50)
    
    for i in range(1, len(coeficientes)):
        termino = coeficientes[i]
        termino_str = f"{coeficientes[i]}"
        
        # Multiplicamos por (x - x_j) para cada j < i
        for j in range(i):
            termino *= (x - x_points[j])
            termino_str += f"(x - {x_points[j]})"
        
        polinomio += termino
        terminos.append(termino_str)
    
    print("Tabla de diferencias divididas:")
    tabla = [[0 for _ in range(len(x_points))] for _ in range(len(x_points))]
    for i in range(len(x_points)):
        tabla[i][0] = y_points[i]
    
    for j in range(1, len(x_points)):
        for i in range(len(x_points) - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (x_points[i + j] - x_points[i])
    
    for i in range(len(x_points)):
        fila = f"x_{i} = {x_points[i]:2.0f} | "
        for j in range(len(x_points) - i):
            if j == 0:
                fila += f"{tabla[i][j]:6.1f} | "
            else:
                fila += f"{tabla[i][j]:6.1f} | "
        print(fila)
    
    print("\nTérminos del polinomio:")
    for i, termino in enumerate(terminos):
        print(f"Término {i}: {termino}")
    
    print("-" * 50)
    print(f"P(x) = {' + '.join(terminos)}")
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
x_puntos = [1, 0, -3]
y_puntos = [2, 4, -2]

print("Datos de entrada:")
print(f"x: {x_puntos}")
print(f"y: {y_puntos}\n")

# Llamada principal para obtener la fórmula del polinomio
polinomio, x_var = obtener_polinomio_newton(x_puntos, y_puntos)

# Probamos el polinomio evaluando puntos que NO estaban en la lista original
print("\nEvaluaciones:")
for punto in [-1, -2, 4, 7]:
    valor = evaluar_polinomio(polinomio, punto)
    print(f"P({punto}) = {valor}")

# --- BLOQUE DE VISUALIZACIÓN GRÁFICA ---

# Creamos 200 puntos entre -4 y 2 para dibujar una curva suave
x_vals = np.linspace(-4, 2, 200)

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
plt.title('Polinomio de Interpolación de Newton')
plt.legend()
plt.grid(True)
# Dibujamos los ejes X e Y para referencia
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.show()