# Ejemplo 2 de interpolación
============================

Obtener el polinomio de interpolación de Newton para los siguientes puntos:

| x | y |
|---|---|
| 1 | 2|
| 0 | 4 | 
| -3 | -2|

Para obtener el polinomio de interpolación de Newton, utilizamos la fórmula:

$$ P(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) $$

Donde $f[x_0]$ es el valor de la función en el punto $x_0$, $f[x_0, x_1]$ es la diferencia dividida entre los puntos $x_0$ y $x_1$, y $f[x_0, x_1, x_2]$ es la diferencia dividida entre los puntos $x_0$, $x_1$ y $x_2$.

Calculamos las diferencias divididas mediante el uso de la tabla:

| x_i | f[x_i] | f[x_i, x_{i+1}] | f[x_i, x_{i+1}, x_{i+2}] |
| x_0 | f[x_0] | f[x_0, x_1] | f[x_0, x_1, x_2] |
| x_1 | f[x_1] | f[x_1, x_2] | |
| x_2 | f[x_2] | | |

Calculamos los valores de f[x_i]:
- f[x_0] = f[1] = 2
- f[x_1] = f[0] = 4
- f[x_2] = f[-3] = -2

Calculamos las diferencias divididas:
- f[x_0, x_1] = (f[x_1] - f[x_0])/(x_1 - x_0) = (4 - 2)/(0 - 1) = -2
- f[x_1, x_2] = (f[x_2] - f[x_1])/(x_2 - x_1) = (-2 - 4)/(-3 - 0) = 2
- f[x_0, x_1, x_2] = (f[x_1, x_2] - f[x_0, x_1])/(x_2 - x_0) = (2 - (-2))/(-3 - 1) = 4/(-4) = -1

Sustituyendo los valores en la tabla:

| x_i | f[x_i] | f[x_i, x_{i+1}] | f[x_i, x_{i+1}, x_{i+2}] |
| 1 | 2 | -2 | -1 |
| 0 | 4 | 2 | |
| -3 | -2 | | |
Finalmente, el polinomio de interpolación de Newton es:
$$ P(x) = 2 - 2(x - 1) - 1(x - 1)(x - 0) $$
Simplificando:
$$ P(x) = 2 - 2(x - 1) - (x - 1)x $$
$$ P(x) = 2 - 2x + 2 - x^2 + x $$
$$ P(x) = -x^2 - x + 4 $$
