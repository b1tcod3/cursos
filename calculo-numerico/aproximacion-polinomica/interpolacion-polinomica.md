# Interpolación Polinómica 📐

La interpolación polinómica es una herramienta fundamental en el análisis numérico, ya que permite aproximar funciones complejas o datos discretos mediante una expresión algebraica manejable: el polinomio.

> **Definición:**: Es una técnica que consiste en encontrar un polinomio que pase exactamente por un conjunto de puntos dados. Dado un conjunto de $n+1$ puntos, existe un único polinomio de grado *n* que satisface todas las condiciones de interpolación, resultado garantizado por el determinante de Vandermonde.

## Principales métodos de interpolación polinómica

1. **Lagrange**: [Ejemplo 1](./ejemplos/ejemplo-1.md) | [Código Python](./codigo/langrage-polinomio.py)
2. **Newton**: [Ejemplo 2](./ejemplos/ejemplo-2.md) | [Código Python](./codigo/newton-polinomio.py)
3. **Hermite**: [Ejemplo 3](./ejemplos/ejemplo-3.md) | [Código Python](./codigo/hermite-polinomio.py)
4. **Spline**:
5. **Chebyshev**:
6. **Runge-Kutta**:

## Método de Interpolación de Lagrange

Este método en lugar de esolver un sistema de ecuaciones complicado, Lagrange propone armar el polinomio como una "combinación" de piezas más simples llamadas polinomios base($L_i$).

> **Formulación:** Dado un conjunto de puntos $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, el polinomio de interpolación de Lagrange se define como:

$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

donde los polinomios de base $L_i(x)$ se calculan como:

$$L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}$$

Cada $L_i(x)$ es un polinomio de grado $n$ con las siguientes propiedades:
- Cada bloque $L_i$ vale 1 cuando evaluamos en su propio punto $x_i$.
- Ese mismo bloque vale 0 en todos los demás puntos de la lista.

En resumen, cada polinomio de base $L_i(x)$ es igual a 1 en $x_i$ y 0 en los demás puntos para $i \neq j$, lo que garantiza que el polinomio de interpolación pase por todos los puntos dados.

**Ejemplo práctico**: Consulta el [Ejemplo 1](./ejemplos/ejemplo-1.md) para ver una aplicación paso a paso del método de Lagrange.

**Implementación**: Revisa el [código en Python](./codigo/langrage-polinomio.py) que implementa el algoritmo de interpolación de Lagrange.

## Método de Interpolación de Newton

El método de Diferencias Divididas de Newton es una forma algorítmica y eficiente de obtener el mismo polinomio único que Lagrange, pero construido de manera incremental.

> **Formulación:** Expresa el polinomio interpolador en una base diferente, asociadas a los nodos de interpolación:

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

**Implementación**: Revisa el [código en Python](./codigo/newton-polinomio.py) que implementa el algoritmo de interpolación de Newton.

## Interpolación de Hermite

> **Definición:** La interpolación de Hermite es un método de aproximación polinómica que generaliza la interpolación clásica al incorporar información no solo de los valores de la función, sino también de sus derivadas en los nodos de interpolación.

Dados $n+1$ puntos distintos $x_0, x_1, \ldots, x_n$, se conocen los valores de la función $f(x_i)$ y de su derivada $f'(x_i)$ en cada nodo. El objetivo es encontrar un polinomio $H(x)$ de grado mínimo que satisfaga:

$$H(x_i) = f(x_i), \quad H'(x_i) = f'(x_i), \quad i = 0, 1, \ldots, n$$

Este polinomio existe, es único, y tiene grado $2n+1$, ya que se dispone de $2n+2$ datos para construirlo ($n+1$ valores de la función y $n+1$ valores de la derivada).

### Nodos repetidos

Para construir el polinomio de Hermite usando el método de Newton con diferencias divididas, se define un conjunto de puntos $z_0, z_1, \ldots, z_{2n+1}$ donde cada nodo $x_i$ aparece repetido dos veces:

$$z_{2i} = z_{2i+1} = x_i, \quad i = 0, 1, \ldots, n$$

### Fórmula de diferencias divididas con nodos repetidos

La tabla de diferencias divididas se construye siguiendo estas reglas:

Para nodos ordenados $x_0 \leq x_1 \leq \cdots \leq x_k$:

$$f[x_0, x_1, \ldots, x_k] = \frac{f^{(k)}(x_0)}{k!} \text{ si } x_0 = x_k$$

$$f[x_0, x_1, \ldots, x_k] = \frac{f[x_1, \ldots, x_k] - f[x_0, \ldots, x_{k-1}]}{x_k - x_0} \text{ si } x_0 \neq x_k$$

**Reglas clave:**
- Cuando los nodos son idénticos: $f[x_i, x_i] = f'(x_i)$
- Para tres nodos repetidos: $f[x_i, x_i, x_i] = \frac{f''(x_i)}{2!}$
- En general: $f[x_i, x_i, \ldots, x_i] = \frac{f^{(j)}(x_i)}{j!}$ donde $j$ es el número de repeticiones menos 1

### Tabla de diferencias divididas para Hermite

La tabla se construye repitiendo cada nodo y colocando las derivadas según corresponda. Para el caso de dos nodos $(x_0, x_1)$ con sus respectivas derivadas $(d_0, d_1)$:

| $x_i$ | D.D. Orden 0 | D.D. Orden 1 | D.D. Orden 2 | D.D. Orden 3 |
|-------|---------------|---------------|---------------|---------------|
| $x_0$ | $y_0$ | | | |
| $x_0$ | $y_0$ | $d_0$ | | |
| $x_1$ | $y_1$ | $P_1$ | $(P_1 - d_0)/h$ | |
| $x_1$ | $y_1$ | $d_1$ | $(d_1 - P_1)/h$ | $(d_0 + d_1 - 2P_1)/h^2$ |

Donde $P_1 = \frac{y_1 - y_0}{h}$ y $h = x_1 - x_0$.

### Fórmula del polinomio de Hermite

El polinomio se expresa mediante la fórmula de Newton:

$$H(x) = \sum_{k=0}^{2n+1} f[z_0, z_1, \ldots, z_k] \prod_{j=0}^{k-1}(x - z_j)$$

Los coeficientes son las diferencias divididas que aparecen en la primera celda de cada columna de la tabla (diagonal superior).

Para dos nodos, el polinomio cúbico de Hermite es:

$$H(x) = y_0 + d_0(x-x_0) + \frac{P_1 - d_0}{h}(x-x_0)^2 + \frac{d_0 + d_1 - 2P_1}{h^2}(x-x_0)^2(x-x_1)$$

**Ejemplo práctico**: Consulta el [Ejemplo 3](./ejemplos/ejemplo-3.md) para ver una aplicación paso a paso del método de Hermite.


