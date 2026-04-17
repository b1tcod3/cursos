# Ejemplo de Interpolación de Hermite

Usamos los mismos puntos que en los ejemplos de Lagrange y Newton para mantener consistencia.

## Datos

- Puntos: (1, 2), (0, 4), (-3, -2)
- Derivadas: Calculadas a partir del polinomio resultado P(x) = -x² - x + 4
  - f'(x) = -2x - 1
  - f'(1) = -3, f'(0) = -1, f'(-3) = 5

| x_i | f(x_i) | f'(x_i) |
|-----|--------|---------|
| 1   | 2      | -3      |
| 0   | 4      | -1      |
| -3  | -2     | 5       |

## Tabla de diferencias divididas (nodos repetidos)

| x_i | D.D. 0 | D.D. 1 | D.D. 2 | D.D. 3 | D.D. 4 | D.D. 5 |
|-----|--------|--------|--------|--------|--------|--------|
| 1   | 2      |        |        |        |        |        |
| 1   | 2      | -3     |        |        |        |        |
| 0   | 4      | 2      | 5      |        |        |        |
| 0   | 4      | -1     | -3     | -2     |        |        |
| -3  | -2     | -1     | 0      | 1      | 0.2    |        |
| -3  | -2     | 5      | -3     | 0      | -0.5   | -0.1   |

## Polinomio resultante

El polinomio de Hermite con 3 nodos tiene grado 5:

$$H(x) = 2 - 3(x-1) + 5(x-1)^2 - 2(x-1)^2x + (x-1)^2x^2 + \cdots$$

Simplificado: $H(x) = -x^2 - x + 4$

**Nota**: En este caso particular, el polinomio de Hermite coincide con el de Newton porque los datos provienen de un polinomio cuadrático. El método de Hermite es más útil cuando se conoce la derivada de la función original o cuando se quiere una interpolación más suave.