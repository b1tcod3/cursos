# Funciones Polinómicas 📊

## 1. Funciones Potencia y Comportamiento Final

El comportamiento final (end behavior) describe cómo se comporta la salida de una función cuando la entrada tiende a $\infty$ o a $-\infty$.

> **Notación simbólica:**
>
> - as $x \to -\infty$, $f(x) \to \infty$
> - as $x \to \infty$, $f(x) \to -\infty$

### Ejemplo 1: Comportamiento final de una función potencia

Describe el comportamiento final de la gráfica de $f(x) = -x^9$.

**Solución**

El exponente de la función potencia es $9$ (un número **impar**). Como el coeficiente es $-1$ (negativo), la gráfica es el reflejo sobre el eje $x$ de la gráfica de $f(x) = x^9$. A medida que $x$ tiende a infinito, la salida decrece sin límite. A medida que $x$ tiende a infinito negativo, la salida crece sin límite. En forma simbólica:

$$x \to -\infty, \quad f(x) \to \infty$$
$$x \to \infty, \quad f(x) \to -\infty$$

**Verificación con tabla de valores:**

| $x$  | $f(x)$         |
|------|----------------|
| $-10$| $1\,000\,000\,000$ |
| $-5$ | $1\,953\,125$  |
| $0$  | $0$            |
| $5$  | $-1\,953\,125$ |
| $10$ | $-1\,000\,000\,000$ |

Podemos ver que al sustituir valores muy pequeños para $x$, la salida es muy grande, y al sustituir valores muy grandes, la salida es muy pequeña (un valor negativo muy grande).

---

## 2. Identificación de Funciones Polinómicas

### Ejemplo 2: Derrame de petróleo

Un oleoducto revienta en el Golfo de México, causando una mancha de petróleo de forma aproximadamente circular. La mancha tiene actualmente 24 millas de radio, pero este radio aumenta 8 millas cada semana. Queremos escribir una fórmula para el área cubierta por la mancha combinando dos funciones.

El radio $r$ de la mancha depende del número de semanas $w$ transcurridas. Esta relación es **lineal**:

$$r(w) = 24 + 8w$$

Podemos combinar esto con la fórmula del área de un círculo:

$$A(r) = \pi r^2$$

Componiendo estas funciones obtenemos una fórmula para el área en términos de las semanas:

$$A(w) = A(r(w)) = A(24 + 8w) = \pi(24 + 8w)^2$$

Multiplicando:

$$A(w) = 576\pi + 384\pi w + 64\pi w^2$$

Esta fórmula es un ejemplo de una **función polinómica**.

> **Definición:** una función polinómica consiste en cero o la suma de un número finito de términos no nulos, cada uno de los cuales es el producto de un número —llamado **coeficiente** del término— y una variable elevada a una potencia entera no negativa.

> **Forma general de una función polinómica:** sea $n$ un entero no negativo. Una función polinómica es una función que puede escribirse de la forma:
>
> $$f(x) = a_n x^n + \dots + a_2 x^2 + a_1 x + a_0$$
>
> Cada $a_i$ es un **coeficiente** y puede ser cualquier número real distinto de cero. Cada expresión $a_i x^i$ es un **término** de la función polinómica.

---

## 3. Grado y Coeficiente Principal

Debido a la forma de una función polinómica, podemos ver una variedad infinita en el número de términos y en la potencia de la variable. Aunque el orden de los términos no importa para realizar operaciones, normalmente ordenamos los términos en potencias descendentes, o en **forma general**.

> **Definiciones:**
>
> - **Grado** del polinomio: la potencia más alta de la variable que aparece en el polinomio; es la potencia de la primera variable si la función está en forma general.
> - **Término principal** (leading term): el término que contiene la potencia más alta de la variable, o el término de mayor grado.
> - **Coeficiente principal** (leading coefficient): el coeficiente del término principal.

### Algoritmo: identificar el grado y el coeficiente principal

1. Encontrar la **potencia más alta** de $x$ para determinar el grado de la función.
2. Identificar el **término** que contiene la potencia más alta de $x$ para encontrar el término principal.
3. Identificar el **coeficiente** del término principal.

---

## 4. Interceptos y Puntos de Inflexión (Turning Points)

> **Definiciones:**
>
> - **Punto de inflexión** (turning point) de una gráfica: un punto en el cual la gráfica cambia de dirección, de creciente a decreciente o de decreciente a creciente.
> - **Intercepto $y$:** el punto en el cual la función tiene un valor de entrada igual a cero.
> - **Interceptos $x$:** los puntos en los cuales el valor de salida es cero.

### Algoritmo: determinar los interceptos

1. Determinar el **intercepto $y$** sustituyendo $x = 0$ y encontrando el valor de salida correspondiente.
2. Determinar los **interceptos $x$** resolviendo para los valores de entrada que producen un valor de salida de cero.

### Ejemplo 3: Interceptos de una función polinómica en forma factorizada

Dada la función polinómica $f(x) = (x - 2)(x + 1)(x - 4)$, escrita en forma factorizada, determina los interceptos $y$ y $x$.

**Solución**

El intercepto $y$ ocurre cuando la entrada es cero; sustituimos $0$ por $x$:

$$f(0) = (0 - 2)(0 + 1)(0 - 4) = (-2)(1)(-4) = 8$$

El intercepto $y$ es $(0, 8)$.

Los interceptos $x$ ocurren cuando la salida es cero:

$$0 = (x - 2)(x + 1)(x - 4)$$
$$x - 2 = 0 \quad \text{o} \quad x + 1 = 0 \quad \text{o} \quad x - 4 = 0$$
$$x = 2 \quad \text{o} \quad x = -1 \quad \text{o} \quad x = 4$$

Los interceptos $x$ son $(2, 0)$, $(-1, 0)$ y $(4, 0)$.

### Ejemplo 4: Interceptos de una función polinómica factorizando

Dada la función polinómica $f(x) = x^4 - 4x^2 - 45$, determina los interceptos $y$ y $x$.

**Solución**

El intercepto $y$ ocurre cuando la entrada es cero:

$$f(0) = (0)^4 - 4(0)^2 - 45 = -45$$

El intercepto $y$ es $(0, -45)$.

Los interceptos $x$ ocurren cuando la salida es cero; para determinarlos factorizamos el polinomio:

$$f(x) = x^4 - 4x^2 - 45 = (x^2 - 9)(x^2 + 5) = (x - 3)(x + 3)(x^2 + 5)$$
$$0 = (x - 3)(x + 3)(x^2 + 5)$$
$$x - 3 = 0 \quad \text{o} \quad x + 3 = 0 \quad \text{o} \quad x^2 + 5 = 0$$
$$x = 3 \quad \text{o} \quad x = -3 \quad \text{o} \quad \text{(sin solución real)}$$

Los interceptos $x$ son $(3, 0)$ y $(-3, 0)$.

> **Nota:** la función es par, pues $f(x) = f(-x)$.

### Gráficas continuas y suaves

- El grado de una función polinómica ayuda a determinar el número de interceptos $x$ y de puntos de inflexión.
- Una función polinómica de grado $n$ es el producto de $n$ factores, por lo que tendrá **como máximo $n$ raíces o ceros** (interceptos $x$).
- La gráfica de una función polinómica de grado $n$ debe tener **como máximo $n - 1$ puntos de inflexión**: uno menos que el grado del polinomio.

> **Definiciones:**
>
> - Una función **continua** no tiene rupturas en su gráfica: puede dibujarse sin levantar el lápiz del papel.
> - Una curva **suave** es una gráfica sin esquinas pronunciadas. Los puntos de inflexión de una gráfica suave siempre ocurren en curvas redondeadas.
> - Las gráficas de las funciones polinómicas son **continuas y suaves**.

> **Interceptos y puntos de inflexión:** un polinomio de grado $n$ tendrá, como máximo, $n$ interceptos en $x$ y $n - 1$ puntos de inflexión.

### Ejemplo 5: Número máximo de interceptos y puntos de inflexión

Sin graficar la función, determina el comportamiento local de $f(x) = -3x^{10} + 4x^7 - x^4 + 2x^3$ encontrando el número máximo de interceptos en $x$ y de puntos de inflexión.

**Solución**

El polinomio tiene grado $10$, por lo que hay como máximo **10 interceptos en $x$** y como máximo **9 puntos de inflexión**.

### Conclusión a partir de la gráfica

En el texto se muestra una gráfica (Figura 5.30) y se razona de la siguiente manera: el comportamiento final indica que es un polinomio de **grado par**; la gráfica tiene 2 interceptos en $x$ (sugiriendo un grado de 2 o mayor) y 3 puntos de inflexión (sugiriendo un grado de 4 o mayor). Sería razonable concluir que el grado es **par y al menos 4**.

### Ejemplo 6: Comportamiento local a partir de los factores

Dada la función $f(x) = -4x(x + 3)(x - 4)$, determina el comportamiento local.

**Solución**

El intercepto $y$ se encuentra evaluando $f(0)$:

$$f(0) = -4(0)(0 + 3)(0 - 4) = 0$$

El intercepto $y$ es $(0, 0)$.

Los interceptos $x$ se encuentran determinando los ceros de la función:

$$0 = -4x(x + 3)(x - 4)$$
$$x = 0 \quad \text{o} \quad x + 3 = 0 \quad \text{o} \quad x - 4 = 0$$
$$x = 0 \quad \text{o} \quad x = -3 \quad \text{o} \quad x = 4$$

Los interceptos $x$ son $(0, 0)$, $(-3, 0)$ y $(4, 0)$.

El grado es $3$, por lo que la gráfica tiene como máximo **2 puntos de inflexión**.

---

## 5. Esbozo de Gráficas de Funciones Polinómicas

Para esbozar la gráfica de un polinomio en forma factorizada se usan sus ceros, su multiplicidad, el comportamiento final y el intercepto $y$.

### Ejemplo 7: Esbozar la gráfica de un polinomio factorizado

Esboza la gráfica de $f(x) = -2(x + 3)^2(x - 5)$.

**Solución**

La función tiene ceros en $x = -3$ (multiplicidad 2, por lo que la gráfica **rebota** en el eje) y $x = 5$ (multiplicidad 1, por lo que la gráfica **cruza** el eje). El intercepto $y$ es:

$$f(0) = -2(3)^2(-5) = 90$$

El grado es $3$ (impar) y el coeficiente principal es $-2$ (negativo), por lo que:

$$x \to -\infty, \quad f(x) \to \infty \qquad \text{y} \qquad x \to \infty, \quad f(x) \to -\infty$$

Como $x \to \infty$ implica $f(x) \to -\infty$, sabemos que la gráfica continúa decreciendo y podemos dejar de dibujar en el cuarto cuadrante. Con tecnología se puede verificar que el esbozo coincide con la gráfica completa.

---

## 6. Teorema del Valor Intermedio

En algunas situaciones conocemos dos puntos de una gráfica pero no los ceros. Si esos dos puntos están a lados opuestos del eje $x$, podemos confirmar que existe un cero entre ellos.

> **Teorema del Valor Intermedio:** sea $f$ una función polinómica. Si $f(a)$ y $f(b)$ tienen **signos opuestos**, entonces existe al menos un valor $c$ entre $a$ y $b$ para el cual $f(c) = 0$.

> **Idea intuitiva:** cuando una función polinómica cambia de un valor negativo a uno positivo (o viceversa), la gráfica debe cruzar el eje $x$.

### Ejemplo 8: Usar el Teorema del Valor Intermedio

Muestra que la función $f(x) = x^3 - 5x^2 + 3x + 6$ tiene al menos dos ceros reales entre $x = 1$ y $x = 4$.

**Solución**

Evaluamos $f(x)$ en los valores enteros $x = 1, 2, 3$ y $4$:

| $x$ | $1$ | $2$ | $3$ | $4$ |
|-----|-----|-----|-----|-----|
| $f(x)$ | $5$ | $0$ | $-3$ | $2$ |

Vemos que un cero ocurre en $x = 2$. Además, como $f(3)$ es negativo y $f(4)$ es positivo, por el Teorema del Valor Intermedio debe existir al menos un cero real entre $3$ y $4$.

Por lo tanto, hay **al menos dos ceros reales entre $x = 1$ y $x = 4$**.

---

## 7. Escritura de Fórmulas para Funciones Polinómicas

Como una función polinómica en forma factorizada tiene un intercepto en $x$ donde cada factor es cero, podemos construir una función que pase por un conjunto de interceptos introduciendo los factores correspondientes.

> **Forma factorizada:** si un polinomio de grado mínimo $p$ tiene interceptos horizontales en $x = x_1, x_2, \dots, x_n$, entonces puede escribirse como:
>
> $$f(x) = a(x - x_1)^{p_1}(x - x_2)^{p_2} \cdots (x - x_n)^{p_n}$$
>
> donde las potencias $p_i$ de cada factor se determinan por el comportamiento de la gráfica en el intercepto correspondiente, y el factor de estiramiento $a$ se determina a partir de un valor de la función distinto del intercepto en $x$.

### Algoritmo: escribir una fórmula a partir de la gráfica

1. Identificar los **interceptos en $x$** de la gráfica para encontrar los factores del polinomio.
2. Examinar el **comportamiento** de la gráfica en los interceptos en $x$ para determinar la **multiplicidad** de cada factor.
3. Encontrar el polinomio de **menor grado** que contenga todos los factores hallados en el paso anterior.
4. Usar **cualquier otro punto** de la gráfica (el intercepto $y$ suele ser el más fácil) para determinar el factor de estiramiento $a$.

### Ejemplo 9: Escribir una fórmula para una función polinómica desde la gráfica

La gráfica de un polinomio tiene tres interceptos en $x$: $x = -3$, $x = 2$ y $x = 5$. El intercepto $y$ está en $(0, -2)$. En $x = -3$ y $x = 5$ la gráfica pasa por el eje de forma lineal (factores lineales), y en $x = 2$ la gráfica rebota en el intercepto (factor cuadrático). Escribe la fórmula.

**Solución**

Con los interceptos y sus multiplicidades, la forma es:

$$f(x) = a(x + 3)(x - 2)^2(x - 5)$$

Para determinar $a$, usamos el intercepto $y$ $(0, -2)$:

$$f(0) = a(0 + 3)(0 - 2)^2(0 - 5)$$
$$-2 = a(3)(4)(-5) = -60a$$
$$a = \frac{1}{30}$$

La función es:

$$f(x) = \frac{1}{30}(x + 3)(x - 2)^2(x - 5)$$

---

## 8. Extremos Locales y Globales

Con cuadráticas, el máximo o mínimo se hallaba algebraicamente con el vértice. Para polinomios generales, encontrar estos puntos de inflexión requiere técnicas de cálculo; por ahora, estimamos su ubicación usando tecnología.

> **Definiciones:**
>
> - **Máximo o mínimo local** en $x = a$ (también llamado máximo o mínimo relativo): la salida en el punto más alto o más bajo de la gráfica en un intervalo abierto alrededor de $x = a$. Si hay máximo local en $a$, $f(a) \geq f(x)$ para todo $x$ en un intervalo abierto alrededor de $a$. Si hay mínimo local, $f(a) \leq f(x)$ en ese intervalo.
> - **Máximo o mínimo global**: la salida en el punto más alto o más bajo de toda la función. Si hay máximo global en $a$, $f(a) \geq f(x)$ para todo $x$; si hay mínimo global, $f(a) \leq f(x)$ para todo $x$.

> **¿Todas las funciones polinómicas tienen un mínimo o máximo global?**
> No. Solo las funciones polinómicas de **grado par** tienen un mínimo o máximo global. Por ejemplo, $f(x) = x$ no tiene ni máximo ni mínimo global.

### Ejemplo 10: Usar extremos locales en una aplicación

Se construirá una caja abierta cortando cuadrados en cada esquina de una lámina de plástico de 14 cm por 20 cm y doblando los lados. Encuentra el tamaño de los cuadrados que deben cortarse para **maximizar el volumen** encerrado por la caja.

**Solución**

Tras cortar un cuadrado de lado $w$ en cada esquina, queda un rectángulo de $(14 - 2w)$ cm por $(20 - 2w)$ cm para la base, y la caja tendrá $w$ cm de altura. El volumen es:

$$V(w) = (20 - 2w)(14 - 2w)w = 280w - 68w^2 + 4w^3$$

Los factores $w$, $20 - 2w$ y $14 - 2w$ dan los ceros $0$, $10$ y $7$. Una altura de 0 cm no es razonable, y como el lado más corto es 14 y cortamos dos cuadrados, $w$ debe estar entre 0 y 7:

$$0 < w < 7$$

Restringiendo el dominio a $[0, 7]$ y graficando con tecnología, podemos estimar el valor máximo del volumen en alrededor de **340 cm³**, que ocurre cuando los cuadrados miden unos **2.75 cm** por lado. Con un acercamiento de la gráfica, refinamos la estimación a un máximo de aproximadamente **339 cm³** cuando los cuadrados miden **2.7 cm** por lado.
