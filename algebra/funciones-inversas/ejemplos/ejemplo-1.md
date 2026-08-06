# Ejemplo 1: Restringir el dominio para hallar la inversa de una función polinomial

Encuentra la función inversa de:

$$f(x) = (x - 4)^2, \quad x \geq 4 \qquad \text{y} \qquad f(x) = (x - 4)^2, \quad x \leq 4$$

## Solución

La función $f(x) = (x-4)^2$ no es uno-a-uno, pero restringida a $x \geq 4$ o $x \leq 4$ sí lo es.

Comenzamos reemplazando $f(x)$ por $y$ e intercambiando $x$ y $y$:

$$y = (x - 4)^2$$
$$x = (y - 4)^2$$

Sacamos raíz cuadrada:

$$\pm\sqrt{x} = y - 4$$
$$4 \pm \sqrt{x} = y$$

Esto no es una función tal como está. Examinamos la restricción del dominio original para elegir el caso.

### a) Dominio restringido a $x \geq 4$

Las salidas de la inversa deben ser $\geq 4$, así que usamos el caso $+$:

$$\boxed{f^{-1}(x) = 4 + \sqrt{x}}$$

### b) Dominio restringido a $x \leq 4$

Las salidas de la inversa deben ser $\leq 4$, así que usamos el caso $-$:

$$\boxed{f^{-1}(x) = 4 - \sqrt{x}}$$

## Análisis

Las gráficas de $f$ y $f^{-1}$ son simétricas respecto a la recta $y = x$. Si $(a, b)$ está en la gráfica de $f$, entonces $(b, a)$ está en la gráfica de $f^{-1}$. Los puntos de intersección entre $f$ y $f^{-1}$ siempre están sobre $y = x$. Por ejemplo, $(4, 0)$ está en $f$ y $(0, 4)$ está en $f^{-1}$.
