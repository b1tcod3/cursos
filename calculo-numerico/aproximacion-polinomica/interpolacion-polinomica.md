# Interpolación Polinómica

> **Definición:**: Es una técnica que consiste en encontrar un polinomio que pase exactamente por un conjunto de puntos dados. Dado un conjunto de $n+1$ puntos, existe un único polinomio de grado *n* que satisface todas las condiciones de interpolación, resultado garantizado por el determinante de Vandermonde.

## Principales métodos de interpolación polinómica

1. **Lagrange**: [Ejemplo 1](./ejemplos/ejemplo-1.md) | [Código Python](./codigo/langrage-polinomio.py)
2. **Newton**:
3. **Hermite**:
4. **Spline**:
5. **Chebyshev**:
6. **Runge-Kutta**:

## Método de Interpolación de Lagrange

> **Formulación:**: Dado un conjunto de puntos $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, el polinomio de interpolación de Lagrange se define como:

$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

donde los polinomios de base $L_i(x)$ se calculan como:

$$L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}$$

Cada polinomio de base $L_i(x)$ es igual a 1 en $x_i$ y 0 en los demás puntos para $i \neq j$, lo que garantiza que el polinomio de interpolación pase por todos los puntos dados.

**Ejemplo práctico**: Consulta el [Ejemplo 1](./ejemplos/ejemplo-1.md) para ver una aplicación paso a paso del método de Lagrange.

**Implementación**: Revisa el [código en Python](./codigo/langrage-polinomio.py) que implementa el algoritmo de interpolación de Lagrange.

## Método de Interpolación de Newton

> **Formulación:**: Expresa el polinomio interpolador en una base diferente, asociadas a los nodos de interpolación:

$$P(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + ... + f[x_0, x_1, ..., x_n](x - x_0)(x - x_1)...(x - x_{n-1})$$

Los coeficientes $f[x_0, x_1, ..., x_k]$ se denominan diferencias divididas y se calculan de manera recursiva a partir de los valores de la función en los puntos dados:

$$f[x_0, ..., x_n] = \frac{f[x_1, ..., x_n] - f[x_0, ..., x_{n-1}]}{x_n - x_0}$$

con la condición inicial $f[x_k] = f(x_k)$.

Este método es especialmente útil cuando se agregan nuevos puntos de interpolación, ya que permite actualizar el polinomio sin necesidad de recalcular todo desde cero.

### Tabla de Diferencias Divididas
El cálculo de las diferencia divididas se puede organizar en una tabla triangular donde cada columna se obtiene recurvisamente a partir de la anterior. Los coeficientes del polinomio interpolador son las diferencias divididas de la diagonal principal de la tabla.

| $x_i$ | $f[x_i]$ | $f[x_i, x_{i+1}]$ | $f[x_i, x_{i+1}, x_{i+2}]$ | ... |
|------|---------|-------------------|-----------------------------|-----|
| $x_0$ | $f[x_0]$ | $f[x_0, x_1]$ | $f[x_0, x_1, x_2]$ | ... |
| $x_1$ | $f[x_1]$ | $f[x_1, x_2]$ | $f[x_1, x_2, x_3]$ | ... |
| $x_2$ | $f[x_2]$ | $f[x_2, x_3]$ | $f[x_2, x_3, x_4]$ | ... |
| ...  |

**Ejemplo práctico**: Consulta el [Ejemplo 2](./ejemplos/ejemplo-2.md) para ver una aplicación paso a paso del método de Newton.

**Implementación**: Revisa el [código en Python](./codigo/langrage-polinomio.py) que implementa el algoritmo de interpolación de Lagrange.


