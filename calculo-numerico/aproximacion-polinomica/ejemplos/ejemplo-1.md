# Ejemplo 1 de interpolación
============================

Obtener el polinomio de interpolación de Lagrange para los siguientes puntos:

| x | y |
|---|---|
| 1 | 2 |
| 0 | 4 |
| -3 | -2 |

Para obtener el polinomio de interpolación de Lagrange, utilizamos la fórmula:

$$ P_2(x) = y_0 L_0(x) + y_1 L_1(x) + y_2 L_2(x) $$

Calculamos cada uno de los términos $L_i(x)$:

## $L_0(x)$
$$ L_0(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} = \frac{(x - 0)(x + 3)}{(1 - 0)(1 + 3)} = \frac{x(x + 3)}{4} $$

## $L_1(x)$
$$ L_1(x) = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} = \frac{(x - 1)(x + 3)}{(0 - 1)(0 + 3)} = \frac{(x - 1)(x + 3)}{-3} $$

## $L_2(x)$
$$ L_2(x) = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} = \frac{(x - 1)(x - 0)}{(-3 - 1)(-3 - 0)} = \frac{x(x - 1)}{12} $$

Finalmente, sustituimos los valores de $y_i$ y $L_i(x)$ en la fórmula del polinomio de interpolación:

$$ P_2(x) = 2 \cdot L_0(x) + 4 \cdot L_1(x) - 2 \cdot L_2(x) $$

$$ P_2(x) = 2 \cdot \frac{x(x + 3)}{4} + 4 \cdot \frac{(x - 1)(x + 3)}{-3} - 2 \cdot \frac{x(x - 1)}{12} $$

$$ P_2(x) = \frac{x^2 + 3x}{2} - \frac{4}{3}(x^2 + 2x - 3) - \frac{x^2 - x}{6} $$

Eliminamos los denominadores bajo un denominador común:

$$ P_2(x) = \frac{3(x^2 + 3x) - 8(x^2 + 2x - 3) - (x^2 - x)}{6} $$

$$ P_2(x) = \frac{3x^2 + 9x - 8x^2 - 16x + 24 - x^2 + x}{6} $$

Agrupamos los términos semejantes:

$$ P_2(x) = \frac{-6x^2 - 6x + 24}{6} $$

Por lo tanto, el polinomio de interpolación de Lagrange para los puntos dados es:

$$ P_2(x) = -x^2 - x + 4 $$
