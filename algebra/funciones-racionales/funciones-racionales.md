# Funciones Racionales 🥧

Una **función racional** es el cociente de dos funciones polinómicas, $f(x) = \frac{p(x)}{q(x)}$ con $q(x) \neq 0$.

## 1. Asíntotas Verticales y Horizontales

> **Asíntota vertical:** ocurre en los valores de $x$ donde el **denominador** es cero (y el numerador no lo es).
>
> **Asíntota horizontal:** se determina comparando los grados del numerador y del denominador:
> - Si el grado del numerador es menor que el del denominador, la asíntota horizontal es $y = 0$.
> - Si los grados son iguales, la asíntota horizontal es $y = \frac{\text{coeficiente principal del numerador}}{\text{coeficiente principal del denominador}}$.
> - Si el grado del numerador es mayor que el del denominador, no hay asíntota horizontal (puede haber una asíntota oblicua).

### Ejemplo 1: Encontrar las asíntotas verticales y horizontales

Encuentra las asíntotas verticales y horizontales de:

$$f(x) = \frac{(2x - 1)(2x + 1)}{(x - 2)(x + 3)}$$

**Solución**

**Verticales:** el denominador es cero cuando $x - 2 = 0$ o $x + 3 = 0$:

$$x = 2 \qquad \text{y} \qquad x = -3$$

**Horizontal:** expandimos numerador y denominador:

$$(2x - 1)(2x + 1) = 4x^2 - 1 \qquad (x - 2)(x + 3) = x^2 + x - 6$$

Ambos tienen grado 2. La asíntota horizontal es el cociente de los coeficientes principales:

$$y = \frac{4}{1} = 4$$

Las asíntotas verticales son $x = 2$ y $x = -3$, y la horizontal es $y = 4$.

---

## 2. Interceptos de Funciones Racionales

> Una función racional tendrá un **intercepto $y$** en $f(0)$, si la función está definida en cero. No tendrá intercepto $y$ si no está definida en cero.
>
> De igual forma, tendrá **interceptos $x$** en las entradas que hacen que la salida sea cero. Como una fracción solo es cero cuando el **numerador** es cero, los interceptos $x$ solo pueden ocurrir cuando el numerador de la función racional es igual a cero.

### Ejemplo 2: Encontrar los interceptos de una función racional

Encuentra los interceptos de $f(x) = \dfrac{(x - 2)(x + 3)}{(x - 1)(x + 2)(x - 5)}$.

**Solución**

El intercepto $y$ se obtiene evaluando en cero:

$$f(0) = \frac{(0 - 2)(0 + 3)}{(0 - 1)(0 + 2)(0 - 5)} = \frac{(-2)(3)}{(-1)(2)(-5)} = \frac{-6}{10} = -\frac{3}{5} = -0.6$$

Los interceptos $x$ ocurren cuando la función es cero, es decir, cuando el numerador es cero:

$$0 = (x - 2)(x + 3)$$
$$x = 2, -3$$

El intercepto $y$ es $(0, -0.6)$ y los interceptos $x$ son $(2, 0)$ y $(-3, 0)$.

---

## 3. Graficación de Funciones Racionales

El numerador revela los **interceptos $x$** de la gráfica, mientras que el denominador revela las **asíntotas verticales**. Los efectos sobre la forma de la gráfica son los mismos que en los polinomios:

- En un **intercepto $x$** con factor elevado al cuadrado, la gráfica **rebota**.
- En un intercepto $x$ con factor lineal, la gráfica **atraviesa** el eje.

En las asíntotas verticales:
- Si el factor del denominador tiene **grado impar**, la gráfica va hacia $+\infty$ por un lado y hacia $-\infty$ por el otro (comportamiento de $\frac{1}{x}$).
- Si el factor tiene **grado par**, la gráfica va hacia $+\infty$ en ambos lados o hacia $-\infty$ en ambos lados (comportamiento de $\frac{1}{x^2}$).

> **Ejemplo ilustrativo:** en $f(x) = \dfrac{(x + 1)^2(x - 3)}{(x + 3)^2(x - 2)}$:
>
> - En $x = -1$ (factor $(x+1)^2$ del numerador), la gráfica **rebota**.
> - En $x = 3$ (factor lineal), la gráfica **atraviesa** el eje.
> - En $x = -3$ (factor $(x+3)^2$ del denominador), va hacia $+\infty$ en **ambos lados**.
> - En $x = 2$ (factor lineal del denominador), va hacia $+\infty$ por un lado y $-\infty$ por el otro.

### Algoritmo: esbozar una función racional

1. Evaluar la función en $0$ para encontrar el **intercepto $y$**.
2. **Factorizar** el numerador y el denominador.
3. Para los factores del numerador no comunes al denominador, determinar dónde cada factor es cero para hallar los **interceptos $x$**.
4. Encontrar las **multiplicidades** de los interceptos $x$ para determinar el comportamiento de la gráfica en esos puntos.
5. Para los factores del denominador, anotar las multiplicidades de los ceros para determinar el comportamiento local. Para los factores no comunes al numerador, encontrar las **asíntotas verticales** igualando esos factores a cero.
6. Para los factores del denominador comunes a factores del numerador, encontrar las **discontinuidades removibles** (huecos) igualando esos factores a 0.
7. Comparar los grados del numerador y del denominador para determinar las asíntotas **horizontales u oblicuas**.
8. Esbozar la gráfica.

### Ejemplo 3: Graficar una función racional

Esboza la gráfica de $f(x) = \dfrac{(x + 2)(x - 3)}{(x + 1)^2(x - 2)}$.

**Solución**

La función ya está factorizada. Evaluamos en cero para el intercepto $y$:

$$f(0) = \frac{(0 + 2)(0 - 3)}{(0 + 1)^2(0 - 2)} = \frac{(2)(-3)}{(1)(-2)} = 3$$

El intercepto $y$ es $(0, 3)$.

Los interceptos $x$ ocurren cuando el numerador es cero: $x = -2$ y $x = 3$. En ambos el comportamiento es lineal (multiplicidad 1), con la gráfica atravesando el intercepto.

Las asíntotas verticales ocurren cuando el denominador es cero: $x + 1 = 0$ y $x - 2 = 0$, es decir, en $x = -1$ y $x = 2$.

No hay factores comunes entre numerador y denominador, por lo que **no hay discontinuidades removibles**.

Finalmente, el grado del denominador es mayor que el del numerador, por lo que hay una asíntota horizontal en **$y = 0$**.

Para esbozar, ubicamos los tres interceptos. Como no hay interceptos $x$ entre las asíntotas verticales y el intercepto $y$ es positivo, la función permanece positiva entre las asíntotas. El factor asociado a la asíntota en $x = -1$ está elevado al cuadrado, así que el comportamiento es el mismo en ambos lados (hacia $+\infty$). El factor de la asíntota en $x = 2$ no está al cuadrado, así que la gráfica tiene comportamiento opuesto a cada lado. Después de pasar los interceptos $x$, la gráfica se nivela hacia la salida cero, como indica la asíntota horizontal.

---

## 4. Escritura de Funciones Racionales

Una función racional escrita en forma factorizada tendrá un intercepto $x$ donde cada factor del numerador es cero, y una asíntota vertical donde cada factor del denominador es cero.

> **Escritura desde interceptos y asíntotas:** si una función racional tiene interceptos $x$ en $x_1, x_2, \dots, x_n$, asíntotas verticales en $v_1, v_2, \dots, v_m$, y ningún $x_i$ coincide con algún $v_j$, puede escribirse como:
>
> $$f(x) = a\frac{(x - x_1)^{p_1}(x - x_2)^{p_2}\cdots(x - x_n)^{p_n}}{(x - v_1)^{q_1}(x - v_2)^{q_2}\cdots(x - v_m)^{q_m}}$$
>
> donde las potencias se determinan por el comportamiento de la gráfica y $a$ es el factor de estiramiento.

### Algoritmo: escribir la función a partir de la gráfica

1. Determinar los **factores del numerador**: examinar el comportamiento de la gráfica en los interceptos $x$ para determinar los ceros y sus multiplicidades.
2. Determinar los **factores del denominador**: examinar el comportamiento a ambos lados de cada asíntota vertical.
3. Usar **cualquier punto claro** de la gráfica para encontrar el factor de estiramiento $a$.

### Ejemplo 4: Escribir una función racional desde interceptos y asíntotas

La gráfica tiene interceptos $x$ en $x = -2$ y $x = 3$ (en ambos la gráfica atraviesa, sugiriendo factores lineales) y dos asíntotas verticales: en $x = -1$ con comportamiento de $\frac{1}{x}$ (lados opuestos) y en $x = 2$ con comportamiento de $\frac{1}{x^2}$ (mismo lado, hacia $-\infty$). Escribe la función.

**Solución**

Con esta información escribimos una función de la forma:

$$f(x) = a\frac{(x + 2)(x - 3)}{(x + 1)(x - 2)^2}$$

Para encontrar $a$, usamos el intercepto $y$ $(0, -2)$:

$$-2 = a\frac{(0 + 2)(0 - 3)}{(0 + 1)(0 - 2)^2} = a\frac{-6}{4}$$
$$a = \frac{4}{3}$$

La función es:

$$f(x) = \frac{4(x + 2)(x - 3)}{3(x + 1)(x - 2)^2}$$
