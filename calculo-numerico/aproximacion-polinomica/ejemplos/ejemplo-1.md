# Ejemplo 1 de interpolación
============================

Obtener el polinomio de interpolación de Lagrange para los siguientes puntos:

| x | y |
|---|---|
| 0 | -1|
| 1 | 6 | 
| 2 | 31|
| 3 | 18|

Para obtener el polinomio de interpolación de Lagrange, utilizamos la fórmula:

$$ P_n(x) = y_0 L_0(x) + y_1 L_1(x) + y2 L_2(x) + y_3 L_3(x) $$

Calculamos cada uno de los términos $L_i(x)$:

## $L_0(x)$
$$ L_0(x) = \frac{(x - x_1)(x - x_2)(x - x_3)}{(x_0 - x_1)(x_0 - x_2)(x_0 - x_3)} = \frac{(x - 1)(x - 2)(x - 3)}{(0 - 1)(0 - 2)(0 - 3)} = \frac{(x - 1)(x - 2)(x - 3)}{-6}  $$

$$ L_0(x) = \frac{ x^3 - 6x^2 + 11x - 6}{-6} = -\frac{1}{6}x^3 + x^2 - \frac{11}{6}x + 1 $$

## $ L_1(x) $
$$ L_1(x) = \frac{(x - x_0)(x - x_2)(x - x_3)}{(x_1 - x_0)(x_1 - x_2)(x_1 - x_3)} = \frac{(x - 0)(x - 2)(x - 3)}{(1 - 0)(1 - 2)(1 - 3)} = \frac{(x)(x - 2)(x - 3)}{2} $$

$$ L_1(x) = \frac{ x^3 - 5x^2 + 6x}{2} = \frac{1}{2}x^3 - \frac{5}{2}x^2 + 3x $$

## $ L_2(x) $
$$ L_2(x) = \frac{(x - x_0)(x - x_1)(x - x_3)}{(x_2 - x_0)(x_2 - x_1)(x_2 - x_3)} = \frac{(x - 0)(x - 1)(x - 3)}{(2 - 0)(2 - 1)(2 - 3)} = \frac{(x)(x - 1)(x - 3)}{-2} $$
$$ L_2(x) = \frac{ x^3 - 4x^2 + 3x}{-2} = -\frac{1}{2}x^3 + 2x^2 - \frac{3}{2}x $$

## $ L_3(x) $
$$ L_3(x) = \frac{(x - x_0)(x - x_1)(x - x_2)}{(x_3 - x_0)(x_3 - x_1)(x_3 - x_2)} = \frac{(x - 0)(x - 1)(x - 2)}{(3 - 0)(3 - 1)(3 - 2)} = \frac{(x)(x - 1)(x - 2)}{6} $$
$$ L_3(x) = \frac{ x^3 - 3x^2 + 2x}{6} = \frac{1}{6}x^3 - \frac{1}{2}x^2 + \frac{1}{3}x $$

Finalmente, sustituimos los valores de $y_i$ y $L_i(x)$ en la fórmula del polinomio de interpolación:

$$ P_3(x) = -1 \cdot L_0(x) + 6 \cdot L_1(x) + 31 \cdot L_2(x) + 18 \cdot L_3(x) $$

$$ P_3(x) = -1 \cdot \left(-\frac{1}{6}x^3 + x^2 - \frac{11}{6}x + 1\right) + 6 \cdot \left(\frac{1}{2}x^3 - \frac{5}{2}x^2 + 3x\right) + 31 \cdot \left(-\frac{1}{2}x^3 + 2x^2 - \frac{3}{2}x\right) + 18 \cdot \left(\frac{1}{6}x^3 - \frac{1}{2}x^2 + \frac{1}{3}x\right) $$

$$ P_3(x) = \frac{1}{6}x^3 - x^2 + \frac{11}{6}x - 1 + 3x^3 - 15x^2 + 18x - \frac{31}{2}x^3 + 62x^2 - \frac{93}{2}x + 3x^3 - 9x^2 + 6x $$

$$ P_3(x) = \left(\frac{1}{6} + 3 - \frac{31}{2} + 3\right)x^3 + \left(-1 - 15 + 62 - 9\right)x^2 + \left(\frac{11}{6} + 18 - \frac{93}{2} + 6\right)x - 1 $$

Por lo tanto, el polinomio de interpolación de Lagrange para los puntos dados es:
$ P_3(x) = -\frac{25}{3}x^3 + 37x^2 - \frac{133}{6}x - 1 $


