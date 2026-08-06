# Ejemplo 2: Inversa de una función cuadrática cuando no se especifica la restricción

Restringe el dominio y luego encuentra la inversa de:

$$f(x) = (x - 2)^2 - 3$$

## Solución

Es una parábola con vértice en $(2, -3)$ que abre hacia arriba. Es decreciente en un lado del vértice y creciente en el otro, así que restringimos el dominio a:

$$x \geq 2$$

Usamos la forma de vértice. Reemplazamos $f(x)$ por $y$ e intercambiamos $x$ y $y$:

$$y = (x - 2)^2 - 3$$
$$x = (y - 2)^2 - 3$$

Sumamos 3:

$$x + 3 = (y - 2)^2$$

Sacamos raíz cuadrada:

$$\pm\sqrt{x + 3} = y - 2$$
$$2 \pm \sqrt{x + 3} = y$$

Como la función original se restringió a $x \geq 2$, las salidas de la inversa deben ser $\geq 2$, así que usamos el caso $+$:

$$\boxed{f^{-1}(x) = 2 + \sqrt{x + 3}}$$

## Análisis

También podríamos haber restringido el dominio a $x \leq 2$, en cuyo caso:

$$f^{-1}(x) = 2 - \sqrt{x + 3}$$

Se cumple que:

- dominio de $f$ = rango de $f^{-1}$ = $[2, \infty)$
- dominio de $f^{-1}$ = rango de $f$ = $[-3, \infty)$

Las gráficas son simétricas respecto a $y = x$; por ejemplo, $(2, -3)$ está en $f$ y $(-3, 2)$ está en $f^{-1}$.

**Consejo:** si la cuadrática no está en forma de vértice, reescribirla primero permite leer las coordenadas del vértice y restringir el dominio fácilmente.
