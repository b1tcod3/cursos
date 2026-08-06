# Ceros de Funciones Polinómicas 🎯

## 1. Teorema Fundamental del Álgebra

Al observar la gráfica de una función polinómica se puede deducir la **multiplicidad** de sus ceros:

- Si la gráfica **rebota** en el eje $x$, el cero tiene **multiplicidad par** ($2, 4, 6, \dots$).
- Si la gráfica **cruza** el eje $x$, el cero tiene **multiplicidad impar** ($1, 3, 5, \dots$).

> **Teorema Fundamental del Álgebra:** si $f(x)$ es un polinomio de grado $n > 0$, entonces $f(x)$ tiene **al menos un cero complejo**.

Este teorema es la base para resolver ecuaciones polinómicas. Aplicándolo repetidamente: si $f$ es de grado 4 y $f(x) = 0$, existe al menos una solución compleja $c_1$; por el Teorema del Factor, $f(x) = (x - c_1) \cdot q(x)$ con $q$ de grado 3. Aplicamos el teorema al cociente, y así sucesivamente hasta encontrar los 4 ceros, cada uno correspondiente a un factor.

> **Consecuencia:** si $f(x)$ es un polinomio de grado $n > 0$ y $a$ es un número real distinto de cero, entonces $f(x)$ tiene exactamente $n$ factores lineales:
>
> $$f(x) = a(x - c_1)(x - c_2)\cdots(x - c_n)$$
>
> donde $c_1, c_2, \dots, c_n$ son números complejos. Por tanto, $f(x)$ tiene $n$ raíces si contamos las multiplicidades.

> **¿Todo polinomio tiene al menos un cero imaginario?**
> No. Los números reales son un subconjunto de los complejos, pero no al revés. Un número complejo no es necesariamente imaginario: los números reales también son números complejos.

### Ejemplo 1: Encontrar los ceros de una función polinómica con ceros complejos

Encuentra los ceros de $f(x) = 3x^3 + 9x^2 + x + 3$.

**Solución**

Por el **Teorema del Cero Racional**, si $\frac{p}{q}$ es un cero de $f(x)$, entonces $p$ es factor del término constante (3) y $q$ es factor del coeficiente principal (3):

$$\frac{p}{q} = \frac{\text{factores de } 3}{\text{factores de } 3}$$

Los factores de 3 son $\pm 1$ y $\pm 3$, así que los posibles ceros racionales son $\pm 3$, $\pm 1$ y $\pm \frac{1}{3}$. Usamos división sintética para evaluar cada posible cero hasta encontrar uno con resto 0. Empecemos con $-3$:

Dividir entre $(x + 3)$ da resto 0, así que $-3$ es un cero. El polinomio puede escribirse como:

$$(x + 3)(3x^2 + 1)$$

Igualamos la cuadrática a cero y resolvemos:

$$3x^2 + 1 = 0$$
$$x^2 = -\frac{1}{3}$$
$$x = \pm\sqrt{-\frac{1}{3}} = \pm \frac{i\sqrt{3}}{3}$$

Los ceros de $f(x)$ son $-3$ y $\pm \frac{i\sqrt{3}}{3}$.

> **Análisis:** en la gráfica, en $x = -3$ la gráfica cruza el eje $x$ (multiplicidad impar, 1). Además hay dos puntos de inflexión, el máximo para un polinomio de grado 3. Como solo hay un intercepto en $x$ y son dos soluciones complejas, el resultado es correcto (alternativamente, la multiplicidad en $x = -3$ podría ser 3).

---

## 2. Teorema de Factorización Lineal y Teorema del Conjugado Complejo

Una implicación vital del Teorema Fundamental del Álgebra es que una función polinómica de grado $n$ tiene $n$ ceros en el conjunto de los números complejos, contando multiplicidades.

> **Teorema de Factorización Lineal:** una función polinómica tendrá el mismo número de factores que su grado, y cada factor tendrá la forma $(x - c)$, donde $c$ es un número complejo.

> **Teorema del Conjugado Complejo:** si la función polinómica $f$ tiene coeficientes reales y un cero complejo de la forma $a + bi$, entonces el conjugado complejo $a - bi$ también es un cero de $f(x)$.

Esto se cumple porque solo la multiplicación con pares conjugados elimina las partes imaginarias y produce coeficientes reales.

### Algoritmo: encontrar la función a partir de sus ceros y un punto

1. Usar los **ceros** para construir los **factores lineales** del polinomio.
2. **Multiplicar** los factores lineales para expandir el polinomio.
3. **Sustituir** el punto $(c, f(c))$ en la función para determinar el coeficiente principal.
4. **Simplificar**.

### Ejemplo 2: Usar el Teorema de Factorización Lineal

Encuentra un polinomio de cuarto grado con coeficientes reales que tenga ceros $-3$, $2$, $i$, tal que $f(-2) = 100$.

**Solución**

Como $x = i$ es un cero, por el Teorema del Conjugado Complejo $x = -i$ también es un cero. El polinomio debe tener los factores $(x + 3)$, $(x - 2)$, $(x - i)$ y $(x + i)$. Multiplicamos:

$$f(x) = a(x + 3)(x - 2)(x - i)(x + i)$$
$$f(x) = a(x^2 + x - 6)(x^2 + 1)$$
$$f(x) = a(x^4 + x^3 - 5x^2 + x - 6)$$

Para hallar $a$, sustituimos $x = -2$ con $f(-2) = 100$:

$$100 = a((-2)^4 + (-2)^3 - 5(-2)^2 + (-2) - 6)$$
$$100 = a(16 - 8 - 20 - 2 - 6) = a(-20)$$
$$a = -5$$

La función es:

$$f(x) = -5(x^4 + x^3 - 5x^2 + x - 6) \qquad \text{o} \qquad f(x) = -5x^4 - 5x^3 + 25x^2 - 5x + 30$$

> **Análisis:** encontramos que tanto $i$ como $-i$ son ceros, aunque solo uno se dio. Si $i$ es cero de un polinomio con coeficientes reales, $-i$ también debe serlo, pues es su conjugado complejo.

> **¿Si $2 + 3i$ fuera un cero, también $2 - 3i$?** Sí. Cuando cualquier número complejo con componente imaginaria es un cero de un polinomio con coeficientes reales, el conjugado también debe ser cero.

---

## 3. Regla de los Signos de Descartes

Hay una forma directa de determinar los posibles números de ceros reales positivos y negativos de cualquier función polinómica escrita en orden descendente.

> **Regla de los Signos de Descartes:** sea $f(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ una función polinómica con coeficientes reales:
>
> - El número de **ceros reales positivos** es igual al número de cambios de signo de $f(x)$, o menor que este por un entero par.
> - El número de **ceros reales negativos** es igual al número de cambios de signo de $f(-x)$, o menor que este por un entero par.

### Ejemplo 3: Usar la Regla de los Signos de Descartes

Usa la Regla de los Signos de Descartes para determinar los posibles números de ceros reales positivos y negativos de $f(x) = -x^4 - 3x^3 + 6x^2 - 4x - 12$.

**Solución**

Contamos los cambios de signo de $f(x)$:

$$-x^4 \underset{1}{\longrightarrow} -3x^3 \underset{2}{\longrightarrow} 6x^2 \underset{3}{\longrightarrow} -4x \underset{}{\longrightarrow} -12$$

Hay **dos cambios de signo**, así que hay **2 o 0 ceros reales positivos**. Luego examinamos $f(-x)$:

$$f(-x) = -x^4 + 3x^3 + 6x^2 + 4x - 12$$

De nuevo hay **dos cambios de signo**, así que hay **2 o 0 ceros reales negativos**. Las cuatro posibilidades:

| Ceros positivos | Ceros negativos | Ceros complejos | Total |
|-----------------|-----------------|-----------------|-------|
| 2 | 2 | 0 | 4 |
| 2 | 0 | 2 | 4 |
| 0 | 2 | 2 | 4 |
| 0 | 0 | 4 | 4 |

> **Análisis:** al graficar la función se confirma que tiene **0 ceros reales positivos** y **2 ceros reales negativos**.

---

## 4. Aplicaciones: Resolver Ecuaciones Polinómicas

Las herramientas anteriores se combinan para resolver problemas del mundo real.

### Ejemplo 4: Resolver ecuaciones polinómicas

Una nueva panadería ofrece pasteles decorados. Quiere que el volumen de un pastel pequeño sea de 351 pulgadas cúbicas. El pastel tiene forma de sólido rectangular: el largo debe ser cuatro pulgadas más largo que el ancho, y la altura un tercio del ancho. ¿Cuáles deben ser las dimensiones del molde?

**Solución**

El volumen de un sólido rectangular es $V = lwh$. Con $l = w + 4$ y $h = \frac{1}{3}w$:

$$V = (w + 4)(w)\left(\frac{1}{3}w\right) = \frac{1}{3}w^3 + \frac{4}{3}w^2$$

Sustituimos el volumen dado:

$$351 = \frac{1}{3}w^3 + \frac{4}{3}w^2$$
$$1053 = w^3 + 4w^2 \qquad \text{multiplicamos por 3}$$
$$0 = w^3 + 4w^2 - 1053 \qquad \text{restamos 1053}$$

La Regla de los Signos de Descartes indica **una solución positiva**. El Teorema del Cero Racional da los posibles ceros racionales $\pm 3, \pm 9, \pm 13, \pm 27, \pm 39, \pm 81, \pm 117, \pm 351$ y $\pm 1053$. Solo los positivos tienen sentido; con división sintética probamos $w = 1$ (no), $w = 3$ (no) y $w = 9$ (resto 0).

Con $w = 9$:

$$l = w + 4 = 13 \qquad \text{y} \qquad h = \frac{1}{3}w = 3$$

El molde debe tener dimensiones de **13 × 9 × 3 pulgadas**.
