# Ejemplo de Polinomio de Taylor

Construcción de un polinomio de Maclaurin (Taylor con $x_0 = 0$) de grado $n = 3$ para aproximar $f(x) = e^x$ y estimar $e^{0.5}$.

## Datos e iteraciones

Para $f(x) = e^x$, todas sus derivadas son iguales a sí misma: $f^{(k)}(x) = e^x$.

Evaluando en $x_0 = 0$:

| Derivada | $f^{(k)}(x)$ | $f^{(k)}(0)$ |
|----------|-------------|--------------|
| $f(x)$   | $e^x$       | $1$          |
| $f'(x)$  | $e^x$       | $1$          |
| $f''(x)$ | $e^x$       | $1$          |
| $f'''(x)$| $e^x$       | $1$          |

## Construcción del polinomio

Aplicando la fórmula de Taylor para $n = 3$ centrado en $x_0 = 0$:

$$P_3(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3$$

Sustituyendo los valores:

$$P_3(x) = 1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3$$

## Evaluación numérica

Estimamos $e^{0.5}$ evaluando el polinomio en $x = 0.5$:

$$P_3(0.5) = 1 + (0.5) + \frac{1}{2}(0.5)^2 + \frac{1}{6}(0.5)^3$$

$$P_3(0.5) = 1 + 0.5 + 0.125 + 0.020833$$

$$P_3(0.5) = 1.645833$$

Valor real de $e^{0.5} \approx 1.648721$. El error es de apenas $0.002888$ (0.18%), demostrando la alta precisión del polinomio de Taylor cerca del punto base.
