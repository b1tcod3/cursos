# Demostración del Teorema de Existencia y Unicidad

## Enunciado

Dados $n+1$ puntos distintos $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, con $x_i \neq x_j$ para todo $i \neq j$, existe un único polinomio $P(x)$ de grado menor o igual a $n$ tal que:

$$P(x_i) = y_i \quad \text{para todo } i = 0, 1, \dots, n$$

---

## Demostración 1: Por el Teorema Fundamental del Álgebra (Reducción al absurdo)

Supongamos, por contradicción, que existen **dos polinomios distintos** $P(x)$ y $Q(x)$, ambos de grado menor o igual a $n$, que interpolan exactamente los mismos $n+1$ puntos.

Definimos un nuevo polinomio $D(x)$ como la diferencia entre ambos:

$$D(x) = P(x) - Q(x)$$

Al restar dos polinomios de grado $\le n$, el polinomio resultante $D(x)$ también tiene grado $\le n$.

Evaluando $D(x)$ en cualquiera de los nodos de interpolación $x_i$:

$$D(x_i) = P(x_i) - Q(x_i) = y_i - y_i = 0$$

Esto significa que $D(x)$ se anula en los $n+1$ nodos, es decir, $D(x)$ tiene al menos $n+1$ raíces distintas.

Por el Teorema Fundamental del Álgebra, un polinomio no nulo de grado $n$ puede tener como máximo $n$ raíces reales. La única forma de que un polinomio de grado $\le n$ tenga $n+1$ raíces es que sea el **polinomio nulo** ($D(x) = 0$ para todo $x$).

Por lo tanto:

$$P(x) - Q(x) = 0 \quad \implies \quad P(x) = Q(x)$$

Queda demostrado que no pueden existir dos polinomios distintos; el polinomio es único. $\blacksquare$


## Demostración 2: Por Álgebra Lineal (Matriz de Vandermonde)

Asumiendo que el polinomio tiene la forma canónica $P(x) = a_0 + a_1x + a_2x^2 + \dots + a_nx^n$, evaluar los $n+1$ puntos genera un sistema de ecuaciones lineales $Ax = b$:

$$
\begin{pmatrix}
1 & x_0 & x_0^2 & \cdots & x_0^n \\
1 & x_1 & x_1^2 & \cdots & x_1^n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^n
\end{pmatrix}
\begin{pmatrix}
a_0 \\ a_1 \\ \vdots \\ a_n
\end{pmatrix} =
\begin{pmatrix}
y_0 \\ y_1 \\ \vdots \\ y_n
\end{pmatrix}
$$

La matriz de coeficientes es la **Matriz de Vandermonde**. Su determinante es:

$$\det(V) = \prod_{0 \le i < j \le n} (x_j - x_i)$$

Como por definición todos los puntos $x$ son distintos ($x_i \neq x_j$), ningún término del producto es cero. Por lo tanto:

$$\det(V) \neq 0$$

Al ser el determinante no nulo, la matriz es invertible, lo que garantiza que el sistema de ecuaciones tiene **una única solución exacta** para los coeficientes $a_0, a_1, \dots, a_n$. $\blacksquare$


## Consecuencias prácticas

Ambas demostraciones confirman que:

- El polinomio de interpolación es **único** para un conjunto dado de puntos.
- Los métodos de **Lagrange** y **Newton** producen exactamente el mismo polinomio, solo expresado en bases diferentes.
- La elección del método depende de criterios de eficiencia computacional, no de precisión teórica.
- Newton permite agregar nuevos puntos sin recalcular todo; Lagrange requiere rehacer el cálculo completo.
