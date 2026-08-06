# Ejemplo 5: Dominio de una función radical compuesta con una función racional

Encuentra el dominio de:

$$f(x) = \sqrt{\frac{(x + 2)(x - 3)}{x - 1}}$$

## Solución

Una raíz cuadrada solo está definida cuando la cantidad bajo el radical es no negativa. Debemos hallar dónde:

$$\frac{(x + 2)(x - 3)}{x - 1} \geq 0$$

El signo de una función racional puede cambiar en los interceptos $x$ y en las asíntotas verticales. Aquí los puntos de cambio son $x = -2$, $x = 1$ y $x = 3$.

### Probar los intervalos

- $(-\infty, -2)$: probando $x = -3$ → $\frac{(-1)(-6)}{-4} = \frac{6}{-4} < 0$ → **negativo**
- $(-2, 1)$: probando $x = 0$ → $\frac{(2)(-3)}{-1} = 6 > 0$ → **positivo**
- $(1, 3)$: probando $x = 2$ → $\frac{(4)(-1)}{1} = -4 < 0$ → **negativo**
- $(3, \infty)$: probando $x = 4$ → $\frac{(6)(1)}{3} = 2 > 0$ → **positivo**

Incluimos los puntos donde el valor es cero ($x = -2$ y $x = 3$) y excluimos la asíntota ($x = 1$):

$$\boxed{-2 \leq x < 1 \quad \text{o} \quad x \geq 3}$$

En notación de intervalos:

$$\boxed{[-2, 1) \cup [3, \infty)}$$
