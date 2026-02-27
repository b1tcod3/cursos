# Interpolación Polinómica

> **Definición:**: Es una técnica que consiste en encontrar un polinomio que pase exactamente por un conjunto de puntos dados. Dado un conjunto de $n+1$ puntos, existe un único polinomio de grado *n* que satisface todas las condiciones de interpolación, resultado garantizado por el determinante de Vandermonde.

## Principales métodos de interpolación polinómica

1. **Lagrange**:
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


