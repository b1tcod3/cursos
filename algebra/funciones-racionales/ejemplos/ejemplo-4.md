# Ejemplo 4: Escribir una función racional desde interceptos y asíntotas

La gráfica tiene interceptos $x$ en $x = -2$ y $x = 3$ (en ambos la gráfica atraviesa, sugiriendo factores lineales) y dos asíntotas verticales: en $x = -1$ con comportamiento de $\frac{1}{x}$ (lados opuestos) y en $x = 2$ con comportamiento de $\frac{1}{x^2}$ (ambos lados hacia $-\infty$). Escribe la función.

## Solución

### Paso 1: Factores del numerador

Interceptos $x$ en $-2$ y $3$, con factores lineales:

$$(x + 2)(x - 3)$$

### Paso 2: Factores del denominador

Asíntota en $x = -1$ (comportamiento de $\frac{1}{x}$) → factor lineal $(x + 1)$. Asíntota en $x = 2$ (comportamiento de $\frac{1}{x^2}$) → factor al cuadrado $(x - 2)^2$.

### Paso 3: Factor de estiramiento

Usamos el intercepto $y$ $(0, -2)$:

$$-2 = a\frac{(0 + 2)(0 - 3)}{(0 + 1)(0 - 2)^2} = a\frac{(2)(-3)}{(1)(4)} = a\frac{-6}{4}$$
$$a = \frac{4}{3}$$

### Respuesta

$$f(x) = \frac{4(x + 2)(x - 3)}{3(x + 1)(x - 2)^2}$$
