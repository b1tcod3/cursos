# Banco de Ejercicios — Sección 5.5

Ejercicios del libro sobre ceros de funciones polinómicas, con respuestas. Consulta `ceros-de-polinomios.md` para la teoría.

## Verbales

**1.** Describe un uso del Teorema del Resto.

<details>
<summary>Ver respuesta</summary>

Permite encontrar el resto de dividir $f(x)$ entre $(x - k)$ evaluando $f(k)$, sin hacer la división completa. También sirve para verificar si $k$ es un cero (resto 0).
</details>

**2.** Explica por qué el Teorema del Cero Racional no garantiza encontrar los ceros de una función polinómica.

<details>
<summary>Ver respuesta</summary>

Solo lista los ceros racionales **posibles**. La función puede tener ceros irracionales o complejos, o los racionales posibles pueden no ser ceros reales.
</details>

**3.** ¿Cuál es la diferencia entre ceros racionales y reales?

<details>
<summary>Ver respuesta</summary>

Todo cero racional es real, pero no todo cero real es racional. Por ejemplo, $\sqrt{2}$ es real pero no racional.
</details>

**4.** Si la Regla de los Signos de Descartes revela sin cambio de signos o un cambio de signos, ¿qué conclusión específica se puede extraer?

<details>
<summary>Ver respuesta</summary>

Sin cambios de signo: hay **cero** ceros reales positivos (o negativos, según la función analizada). Un cambio de signo: hay **exactamente uno**.
</details>

**5.** Si la división sintética revela un cero, ¿por qué conviene probar ese valor de nuevo como posible solución?

<details>
<summary>Ver respuesta</summary>

Porque el cero puede tener **multiplicidad** mayor que 1; probar de nuevo permite detectar multiplicidades.
</details>

## Teorema del Resto

Usa el Teorema del Resto para encontrar el resto. Recuerda: el resto de dividir entre $(x - k)$ es $f(k)$.

**6.** $(x^4 - 9x^2 + 14) \div (x - 2)$

<details>
<summary>Ver respuesta</summary>

$f(2) = 16 - 36 + 14 = -6$.
</details>

**7.** $(3x^3 - 2x^2 + x - 4) \div (x + 3)$

<details>
<summary>Ver respuesta</summary>

$f(-3) = -81 - 18 - 3 - 4 = -106$.
</details>

**8.** $(x^4 + 5x^3 - 4x - 17) \div (x + 1)$

<details>
<summary>Ver respuesta</summary>

$f(-1) = 1 - 5 + 4 - 17 = -17$.
</details>

**9.** $(-3x^2 + 6x + 24) \div (x - 4)$

<details>
<summary>Ver respuesta</summary>

$f(4) = -48 + 24 + 24 = 0$. ($x - 4$ es factor.)
</details>

**10.** $(5x^5 - 4x^4 + 3x^3 - 2x^2 + x - 1) \div (x + 6)$

<details>
<summary>Ver respuesta</summary>

$f(-6) = -44791$.
</details>

**11.** $(x^4 - 1) \div (x - 4)$

<details>
<summary>Ver respuesta</summary>

$f(4) = 255$.
</details>

**12.** $(3x^3 + 4x^2 - 8x + 2) \div (x - 3)$

<details>
<summary>Ver respuesta</summary>

$f(3) = 81 + 36 - 24 + 2 = 95$.
</details>

**13.** $(4x^3 + 5x^2 - 2x + 7) \div (x + 2)$

<details>
<summary>Ver respuesta</summary>

$f(-2) = -32 + 20 + 4 + 7 = -1$.
</details>

## Teorema del Factor

Usa el Teorema del Factor para encontrar todos los ceros reales de la función dada y el factor dado.

**14.** $f(x) = 2x^3 - 9x^2 + 13x - 6$; $x - 1$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $2x^2 - 7x + 6 = (2x - 3)(x - 2)$. Ceros: $1, \frac{3}{2}, 2$.
</details>

**15.** $f(x) = 2x^3 + x^2 - 5x + 2$; $x + 2$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $2x^2 - 3x + 1 = (2x - 1)(x - 1)$. Ceros: $-2, \frac{1}{2}, 1$.
</details>

**16.** $f(x) = 3x^3 + x^2 - 20x + 12$; $x + 3$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $3x^2 - 8x + 4 = (3x - 2)(x - 2)$. Ceros: $-3, \frac{2}{3}, 2$.
</details>

**17.** $f(x) = 2x^3 + 3x^2 + x + 6$; $x + 2$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $2x^2 - x + 3$, sin raíces reales. Cero real: $-2$ (los otros dos son complejos: $\frac{1}{4} \pm \frac{\sqrt{23}}{4}i$).
</details>

**18.** $f(x) = -5x^3 + 16x^2 - 9$; $x - 3$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $-5x^2 + x + 3$. Ceros: $3, \frac{1 + \sqrt{61}}{10}, \frac{1 - \sqrt{61}}{10}$.
</details>

**19.** $x^3 + 3x^2 + 4x + 12$; $x + 3$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $x^2 + 4$, sin raíces reales. Cero real: $-3$.
</details>

**20.** $4x^3 - 7x + 3$; $x - 1$

<details>
<summary>Ver respuesta</summary>

Dividiendo: $4x^2 + 4x - 3 = (2x - 1)(2x + 3)$. Ceros: $1, \frac{1}{2}, -\frac{3}{2}$.
</details>

**21.** $2x^3 + 5x^2 - 12x - 30$; $2x + 5$

<details>
<summary>Ver respuesta</summary>

Con $x = -\frac{5}{2}$: cociente $x^2 - 6$. Ceros: $-\frac{5}{2}, \pm\sqrt{6}$.
</details>

## Teorema del Cero Racional

Usa el Teorema del Cero Racional para encontrar todos los ceros reales.

**22.** $x^3 - 3x^2 - 10x + 24 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -3, 2, 4$.
</details>

**23.** $2x^3 + 7x^2 - 10x - 24 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -4, -\frac{3}{2}, 2$.
</details>

**24.** $x^3 + 2x^2 - 9x - 18 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -3, -2, 3$.
</details>

**25.** $x^3 + 5x^2 - 16x - 80 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -5, -4, 4$.
</details>

**26.** $x^3 - 3x^2 - 25x + 75 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -5, 3, 5$.
</details>

**27.** $2x^3 - 3x^2 - 32x - 15 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -3, -\frac{1}{2}, 5$.
</details>

**28.** $2x^3 + x^2 - 7x - 6 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -\frac{3}{2}, -1, 2$.
</details>

**29.** $2x^3 - 3x^2 - x + 1 = 0$

<details>
<summary>Ver respuesta</summary>

$x = \frac{1}{2}, \frac{1 \pm \sqrt{5}}{2}$.
</details>

**30.** $3x^3 - x^2 - 11x - 6 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -\frac{2}{3}, \frac{1 \pm \sqrt{13}}{2}$.
</details>

**31.** $2x^3 - 5x^2 + 9x - 9 = 0$

<details>
<summary>Ver respuesta</summary>

$x = \frac{3}{2}$ (los otros dos son complejos: $\frac{1}{2} \pm \frac{\sqrt{11}}{2}i$).
</details>

**32.** $2x^3 - 3x^2 + 4x + 3 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -\frac{1}{2}$ (los otros dos son complejos: $1 \pm \sqrt{2}i$).
</details>

**33.** $x^4 - 2x^3 - 7x^2 + 8x + 12 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -2, -1, 2, 3$.
</details>

**34.** $x^4 + 2x^3 - 9x^2 - 2x + 8 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -4, -1, 1, 2$.
</details>

**35.** $4x^4 + 4x^3 - 25x^2 - x + 6 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -3, -\frac{1}{2}, \frac{1}{2}, 2$.
</details>

**36.** $2x^4 - 3x^3 - 15x^2 + 32x - 12 = 0$

<details>
<summary>Ver respuesta</summary>

$(x - 2)^2(x + 3)(2x - 1) = 0$. Ceros: $2$ (doble), $-3$, $\frac{1}{2}$.
</details>

**37.** $x^4 + 2x^3 - 4x^2 - 10x - 5 = 0$

<details>
<summary>Ver respuesta</summary>

$(x + 1)^2(x^2 - 5) = 0$. Ceros: $-1$ (doble), $\pm\sqrt{5}$.
</details>

**38.** $4x^3 - 3x + 1 = 0$

<details>
<summary>Ver respuesta</summary>

$(x + 1)(2x - 1)^2 = 0$. Ceros: $-1$, $\frac{1}{2}$ (doble).
</details>

**39.** $8x^4 + 26x^3 + 39x^2 + 26x + 6 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -\frac{3}{4}, -\frac{1}{2}$ y los complejos $-1 \pm i$.
</details>

## Soluciones complejas (reales y no reales)

Encuentra todas las soluciones complejas.

**40.** $x^3 + x^2 + x + 1 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -1, \pm i$.
</details>

**41.** $x^3 - 8x^2 + 25x - 26 = 0$

<details>
<summary>Ver respuesta</summary>

$x = 2, 3 \pm 2i$.
</details>

**42.** $x^3 + 13x^2 + 57x + 85 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -5, -4 \pm i$.
</details>

**43.** $3x^3 - 4x^2 + 11x + 10 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -\frac{2}{3}, 1 \pm 2i$.
</details>

**44.** $x^4 + 2x^3 + 22x^2 + 50x - 75 = 0$

<details>
<summary>Ver respuesta</summary>

$x = 1, -3, \pm 5i$.
</details>

**45.** $2x^3 - 3x^2 + 32x + 17 = 0$

<details>
<summary>Ver respuesta</summary>

$x = -\frac{1}{2}, 1 \pm 4i$.
</details>

## Regla de los Signos de Descartes

Usa la Regla de Descartes para determinar el número posible de soluciones positivas y negativas.

**46.** $f(x) = x^3 - 1$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 1 cambio de signo → **1 positivo**. $f(-x) = -x^3 - 1$: 0 cambios → **0 negativos**.
</details>

**47.** $f(x) = x^4 - x^2 - 1$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 1 cambio → **1 positivo**. $f(-x) = x^4 - x^2 - 1$: 1 cambio → **1 negativo**. (2 complejos.)
</details>

**48.** $f(x) = x^3 - 2x^2 - 5x + 6$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 2 cambios → **2 o 0 positivos**. $f(-x) = -x^3 - 2x^2 + 5x + 6$: 1 cambio → **1 negativo**. (Gráfica: 2 positivos.)
</details>

**49.** $f(x) = x^3 - 2x^2 + x - 1$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 3 cambios → **3 o 1 positivos**. $f(-x) = -x^3 - 2x^2 - x - 1$: 0 cambios → **0 negativos**.
</details>

**50.** $f(x) = x^4 + 2x^3 - 12x^2 + 14x - 5$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 3 cambios → **3 o 1 positivos**. $f(-x) = x^4 - 2x^3 - 12x^2 - 14x - 5$: 1 cambio → **1 negativo**. (Gráfica: 1 positivo.)
</details>

**51.** $f(x) = 2x^3 + 37x^2 + 200x + 300$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 0 cambios → **0 positivos**. $f(-x) = -2x^3 + 37x^2 - 200x + 300$: 3 cambios → **3 o 1 negativos**. (Gráfica: 3 negativos.)
</details>

**52.** $f(x) = x^3 - 2x^2 - 16x + 32$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 2 cambios → **2 o 0 positivos**. $f(-x) = -x^3 - 2x^2 + 16x + 32$: 1 cambio → **1 negativo**. (Gráfica: 2 positivos.)
</details>

**53.** $f(x) = 2x^4 - 5x^3 - 5x^2 + 5x + 3$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 2 cambios → **2 o 0 positivos**. $f(-x) = 2x^4 + 5x^3 - 5x^2 - 5x + 3$: 2 cambios → **2 o 0 negativos**. (Gráfica: 2 positivos, 2 negativos.)
</details>

**54.** $f(x) = 2x^4 - 5x^3 - 14x^2 + 20x + 8$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 2 cambios → **2 o 0 positivos**. $f(-x) = 2x^4 + 5x^3 - 14x^2 - 20x + 8$: 2 cambios → **2 o 0 negativos**. (Gráfica: 0 positivos, 0 negativos; los 4 son complejos.)
</details>

**55.** $f(x) = 10x^4 - 21x^2 + 11$

<details>
<summary>Ver respuesta</summary>

$f(x)$: 2 cambios → **2 o 0 positivos**. $f(-x) = 10x^4 - 21x^2 + 11$: 2 cambios → **2 o 0 negativos**. (Ceros reales: $\pm 1, \pm\frac{\sqrt{110}}{10}$.)
</details>

## Numéricos

Enumera todos los posibles ceros racionales de las funciones.

**56.** $f(x) = x^4 + 3x^3 - 4x + 4$

<details>
<summary>Ver respuesta</summary>

$\pm 1, \pm 2, \pm 4$.
</details>

**57.** $f(x) = 2x^3 + 3x^2 - 8x + 5$

<details>
<summary>Ver respuesta</summary>

$\pm 1, \pm 5, \pm \frac{1}{2}, \pm \frac{5}{2}$.
</details>

**58.** $f(x) = 3x^3 + 5x^2 - 5x + 4$

<details>
<summary>Ver respuesta</summary>

$\pm 1, \pm 2, \pm 4, \pm \frac{1}{3}, \pm \frac{2}{3}, \pm \frac{4}{3}$.
</details>

**59.** $f(x) = 6x^4 - 10x^2 + 13x + 1$

<details>
<summary>Ver respuesta</summary>

$\pm 1, \pm \frac{1}{2}, \pm \frac{1}{3}, \pm \frac{1}{6}$.
</details>

**60.** $f(x) = 4x^5 - 10x^4 + 8x^3 + x^2 - 8$

<details>
<summary>Ver respuesta</summary>

$\pm 1, \pm 2, \pm 4, \pm 8, \pm \frac{1}{2}, \pm \frac{1}{4}$.
</details>

## Tecnología

Grafica la función con tu calculadora. Basándote en la gráfica, encuentra los ceros racionales (todas las soluciones reales son racionales).

**61.** $f(x) = 6x^3 - 7x^2 + 1$

<details>
<summary>Ver respuesta</summary>

$-\frac{1}{3}, \frac{1}{2}, 1$.
</details>

**62.** $f(x) = 4x^3 - 4x^2 - 13x - 5$

<details>
<summary>Ver respuesta</summary>

$-1, -\frac{1}{2}, \frac{5}{2}$.
</details>

**63.** $f(x) = 8x^3 - 6x^2 - 23x + 6$

<details>
<summary>Ver respuesta</summary>

$-\frac{3}{2}, \frac{1}{4}, 2$.
</details>

**64.** $f(x) = 12x^4 + 55x^3 + 12x^2 - 117x + 54$

<details>
<summary>Ver respuesta</summary>

$(x + 3)^2(3x - 2)(4x - 3)$. Ceros: $-3$ (doble), $\frac{2}{3}, \frac{3}{4}$.
</details>

**65.** $f(x) = 16x^4 - 24x^3 + x^2 - 15x + 25$

<details>
<summary>Ver respuesta</summary>

$(4x - 5)^2(x^2 + x + 1)$. Cero racional: $\frac{5}{4}$ (doble); los otros dos son complejos.
</details>

## Extensiones

Construye una función polinómica del menor grado posible con la información dada.

**66.** Raíces reales $-1$, $1$, $3$ y $(2, f(2)) = (2, 4)$

<details>
<summary>Ver respuesta</summary>

$f(x) = a(x + 1)(x - 1)(x - 3)$. Con $f(2) = a(3)(1)(-1) = -3a = 4$ → $a = -\frac{4}{3}$.

$$f(x) = -\frac{4}{3}(x + 1)(x - 1)(x - 3)$$
</details>

**67.** Raíces reales $-1$ (con multiplicidad 2) y $1$, y $(2, f(2)) = (2, 4)$

<details>
<summary>Ver respuesta</summary>

$f(x) = a(x + 1)^2(x - 1)$. Con $f(2) = a(9)(1) = 9a = 4$ → $a = \frac{4}{9}$.

$$f(x) = \frac{4}{9}(x + 1)^2(x - 1)$$
</details>

**68.** Raíces reales $-2$, $\frac{1}{2}$ (con multiplicidad 2) y $(-3, f(-3)) = (-3, 5)$

<details>
<summary>Ver respuesta</summary>

$f(x) = a(x + 2)(x - \frac{1}{2})^2$. Con $f(-3) = a(-1)(\frac{49}{4}) = 5$ → $a = -\frac{20}{49}$.

$$f(x) = -\frac{20}{49}(x + 2)\left(x - \frac{1}{2}\right)^2$$
</details>

**69.** Raíces reales $-\frac{1}{2}$, $0$, $\frac{1}{2}$ y $(-2, f(-2)) = (-2, 6)$

<details>
<summary>Ver respuesta</summary>

$f(x) = a\left(x + \frac{1}{2}\right)x\left(x - \frac{1}{2}\right)$. Con $f(-2) = a(-\frac{15}{2}) = 6$ → $a = -\frac{4}{5}$.

$$f(x) = -\frac{4}{5}x\left(x^2 - \frac{1}{4}\right)$$
</details>

**70.** Raíces reales $-4$, $-1$, $1$, $4$ y $(-2, f(-2)) = (-2, 10)$

<details>
<summary>Ver respuesta</summary>

$f(x) = a(x + 4)(x + 1)(x - 1)(x - 4) = a(x^2 - 16)(x^2 - 1)$. Con $f(-2) = a(-12)(3) = -36a = 10$ → $a = -\frac{5}{18}$.

$$f(x) = -\frac{5}{18}(x^2 - 16)(x^2 - 1)$$
</details>

## Aplicaciones del mundo real

Encuentra las dimensiones de la caja descrita.

**71.** El largo es el doble del ancho. La altura es 2 pulgadas mayor que el ancho. El volumen es 192 pulgadas cúbicas.

<details>
<summary>Ver respuesta</summary>

$V = w(2w)(w + 2) = 2w^3 + 4w^2 = 192$ → $w^3 + 2w^2 - 96 = 0$. $w = 4$. Dimensiones: **8 × 4 × 6** pulgadas.
</details>

**72.** El largo, el ancho y la altura son números enteros consecutivos. El volumen es 120 pulgadas cúbicas.

<details>
<summary>Ver respuesta</summary>

$4 \cdot 5 \cdot 6 = 120$. Dimensiones: **4 × 5 × 6** pulgadas.
</details>

**73.** El largo es una pulgada mayor que el ancho, que es una pulgada mayor que la altura. El volumen es 86.625 pulgadas cúbicas.

<details>
<summary>Ver respuesta</summary>

$h(x)(x + 1)(x + 2) = 86.625$. $h = 3.5$. Dimensiones: **5.5 × 4.5 × 3.5** pulgadas.
</details>

**74.** El largo es tres veces la altura, y la altura es una pulgada menor que el ancho. El volumen es 108 pulgadas cúbicas.

<details>
<summary>Ver respuesta</summary>

$V = h(3h)(h + 1) = 3h^3 + 3h^2 = 108$ → $h^3 + h^2 - 36 = 0$. $h = 3$. Dimensiones: **9 × 4 × 3** pulgadas.
</details>

**75.** El largo es 3 pulgadas mayor que el ancho. El ancho es 2 pulgadas mayor que la altura. El volumen es 120 pulgadas cúbicas.

<details>
<summary>Ver respuesta</summary>

$V = h(h + 2)(h + 5) = 120$. $h = 3$. Dimensiones: **8 × 5 × 3** pulgadas.
</details>
