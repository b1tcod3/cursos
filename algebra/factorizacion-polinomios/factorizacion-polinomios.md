# Factorización de Polinomios 🧮

La factorización de polinomios consiste en escribir un polinomio como producto de polinomios de menor grado, llamados **factores**. Es una herramienta fundamental en álgebra: permite simplificar expresiones, resolver ecuaciones y encontrar raíces.

> **Regla de oro:** al factorizar una expresión polinómica, el primer paso debe ser buscar un **factor común (GCF)**. Revisa el GCF de los coeficientes y luego el GCF de las variables.

## 1. Factor Común (GCF)

> **Definición:** el máximo común divisor (GCF) de polinomios es el polinomio más grande que divide exactamente a todos los polinomios de la expresión.

### Algoritmo: factorizar el GCF

1. Identificar el GCF de los **coeficientes**.
2. Identificar el GCF de las **variables**.
3. Combinar ambos para hallar el GCF de la expresión.
4. Determinar por qué debe multiplicarse el GCF para obtener cada término de la expresión.
5. Escribir la expresión factorizada como el producto del GCF y la suma de los términos multiplicadores.

> **Nota:** el GCF de un conjunto de expresiones de la forma $x^n$ siempre será la potencia de menor grado.

### Ejemplo 1: Factorizar el GCF

Factoriza $6x^3y^3 + 45x^2y^2 + 21xy$.

**Solución**

Primero, hallamos el GCF de la expresión:
- El GCF de $6$, $45$ y $21$ es $3$.
- El GCF de $x^3$, $x^2$ y $x$ es $x$.
- El GCF de $y^3$, $y^2$ y $y$ es $y$.

Combinando: el GCF del polinomio es **$3xy$**.

Ahora determinamos por qué multiplicar el GCF para obtener cada término:

$$3xy(2x^2y^2) = 6x^3y^3, \qquad 3xy(15xy) = 45x^2y^2, \qquad 3xy(7) = 21xy$$

Finalmente, escribimos la expresión factorizada:

$$(3xy)(2x^2y^2 + 15xy + 7)$$

**Verificación:** multiplicamos usando la propiedad distributiva para confirmar que $(3xy)(2x^2y^2 + 15xy + 7) = 6x^3y^3 + 45x^2y^2 + 21xy$. ✔

---

## 2. Trinomio con Coeficiente Principal 1

Aunque siempre debemos empezar buscando un GCF, no es la única forma de factorizar. El polinomio $x^2 + 5x + 6$ tiene GCF $1$, pero puede escribirse como producto de los factores $(x + 2)$ y $(x + 3)$.

> **Definición:** un trinomio de la forma $x^2 + bx + c$ puede escribirse en forma factorizada como $(x + p)(x + q)$ donde:
>
> $$pq = c \qquad \text{y} \qquad p + q = b$$

> **¿Se puede factorizar todo trinomio como producto de binomios?**
> No. Algunos polinomios no pueden factorizarse; se dice que son **primos**.

### Algoritmo: factorizar $x^2 + bx + c$

1. Listar los factores de $c$.
2. Hallar $p$ y $q$, un par de factores de $c$ cuya suma sea $b$.
3. Escribir la expresión factorizada como $(x + p)(x + q)$.

### Ejemplo 2: Factorizar un trinomio con coeficiente principal 1

Factoriza $x^2 + 2x - 15$.

**Solución**

Tenemos $b = 2$ y $c = -15$. Buscamos dos números cuyo producto sea $-15$ y cuya suma sea $2$. Listamos los factores:

| Factores de $-15$ | Suma de factores |
|-------------------|------------------|
| $1, -15$          | $-14$            |
| $-1, 15$          | $14$             |
| $3, -5$           | $-2$             |
| $-3, 5$           | $2$ ✔            |

Identificamos $p = -3$ y $q = 5$, y escribimos la forma factorizada:

$$(x - 3)(x + 5)$$

**Verificación:** usando FOIL, $(x - 3)(x + 5) = x^2 + 2x - 15$. ✔

> **¿Importa el orden de los factores?**
> No. La multiplicación es conmutativa, por lo que el orden de los factores no importa.

---

## 3. Factorización por Agrupación

Los trinomios con coeficiente principal distinto de 1 son un poco más complicados. Para ellos, podemos factorizar por **agrupación**: dividir el término en $x$ como suma de dos términos, factorizar cada parte por separado y luego sacar el GCF de toda la expresión.

Por ejemplo, $2x^2 + 5x + 3$ se reescribe como $2x^2 + 2x + 3x + 3$; se factoriza cada parte para obtener $2x(x + 1) + 3(x + 1)$ y luego se saca el GCF $(x + 1)$.

> **Definición:** para factorizar un trinomio de la forma $ax^2 + bx + c$ por agrupación, se hallan dos números con producto $ac$ y suma $b$. Con ellos se divide el término en $x$ en dos términos, se factoriza cada parte de la expresión por separado y se extrae el GCF de toda la expresión.

### Algoritmo: factorizar $ax^2 + bx + c$ por agrupación

1. Listar los factores de $ac$.
2. Hallar $p$ y $q$, un par de factores de $ac$ cuya suma sea $b$.
3. Reescribir la expresión original como $ax^2 + px + qx + c$.
4. Sacar el GCF de $ax^2 + px$.
5. Sacar el GCF de $qx + c$.
6. Factorizar el GCF de toda la expresión.

### Ejemplo 3: Factorizar un trinomio por agrupación

Factoriza $5x^2 + 7x - 6$ por agrupación.

**Solución**

Tenemos $a = 5$, $b = 7$ y $c = -6$. Primero, $ac = -30$. Buscamos dos números con producto $-30$ y suma $7$:

| Factores de $-30$ | Suma de factores |
|-------------------|------------------|
| $1, -30$          | $-29$            |
| $-1, 30$          | $29$             |
| $2, -15$          | $-13$            |
| $-2, 15$          | $13$             |
| $3, -10$          | $-7$             |
| $-3, 10$          | $7$ ✔            |

Entonces $p = -3$ y $q = 10$.

$$5x^2 - 3x + 10x - 6 \quad \text{Reescribimos como } ax^2 + px + qx + c$$
$$x(5x - 3) + 2(5x - 3) \quad \text{Sacamos el GCF de cada parte}$$
$$(5x - 3)(x + 2) \quad \text{Sacamos el GCF de la expresión}$$

**Verificación:** con FOIL, $(5x - 3)(x + 2) = 5x^2 + 7x - 6$. ✔

---

## 4. Trinomio Cuadrado Perfecto

Un trinomio cuadrado perfecto es un trinomio que puede escribirse como el cuadrado de un binomio. Recuerda que al elevar un binomio al cuadrado, el resultado es el cuadrado del primer término, más el doble producto de ambos términos, más el cuadrado del último término:

$$a^2 + 2ab + b^2 = (a + b)^2 \qquad \text{y} \qquad a^2 - 2ab + b^2 = (a - b)^2$$

> **Definición:** un trinomio cuadrado perfecto puede escribirse como el cuadrado de un binomio:
>
> $$a^2 + 2ab + b^2 = (a + b)^2$$

### Algoritmo: factorizar un trinomio cuadrado perfecto

1. Confirmar que el primer y el último término son cuadrados perfectos.
2. Confirmar que el término central es el doble del producto de $ab$.
3. Escribir la forma factorizada como $(a + b)^2$.

### Ejemplo 4: Factorizar un trinomio cuadrado perfecto

Factoriza $25x^2 + 20x + 4$.

**Solución**

Notamos que $25x^2$ y $4$ son cuadrados perfectos, pues $25x^2 = (5x)^2$ y $4 = 2^2$. Luego verificamos si el término central es el doble del producto de $5x$ y $2$:

$$2(5x)(2) = 20x \quad ✔$$

El término central es, efectivamente, el doble del producto. Por lo tanto, el trinomio es un cuadrado perfecto y se escribe:

$$(5x + 2)^2$$

---

## 5. Diferencia de Cuadrados

Una diferencia de cuadrados es un cuadrado perfecto restado de otro cuadrado perfecto. Puede reescribirse como dos factores con los mismos términos pero signos opuestos, porque los términos centrales se cancelan al multiplicar.

> **Definición:** una diferencia de cuadrados puede reescribirse como dos factores con los mismos términos pero signos opuestos:
>
> $$a^2 - b^2 = (a + b)(a - b)$$

### Algoritmo: factorizar una diferencia de cuadrados

1. Confirmar que el primer y el último término son cuadrados perfectos.
2. Escribir la forma factorizada como $(a + b)(a - b)$.

### Ejemplo 5: Factorizar una diferencia de cuadrados

Factoriza $9x^2 - 25$.

**Solución**

Notamos que $9x^2 = (3x)^2$ y $25 = 5^2$ son cuadrados perfectos. El polinomio es una diferencia de cuadrados y se reescribe como:

$$(3x + 5)(3x - 5)$$

> **¿Existe una fórmula para factorizar la suma de cuadrados?**
> No. Una suma de cuadrados no puede factorizarse.

---

## 6. Suma y Diferencia de Cubos

Ahora veremos dos productos especiales nuevos: la suma y la diferencia de cubos. Aunque la suma de cuadrados no puede factorizarse, la suma de cubos sí puede factorizarse en un binomio y un trinomio.

> **Definición:** la suma de dos cubos se factoriza como:
>
> $$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
>
> y la diferencia de dos cubos como:
>
> $$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

### Regla nemotécnica SOAP

Para recordar los signos al factorizar sumas o diferencias de cubos se usa el acrónimo **SOAP**: **S**ame, **O**pposite, **A**lways **P**ositive (igual, opuesto, siempre positivo). Por ejemplo:

$$x^3 - 2^3 = (x - 2)(x^2 + 2x + 4)$$

- El signo del primer término es el **mismo** que el signo entre $x^3 - 2^3$.
- El signo del término $2x$ es **opuesto** al signo entre $x^3 - 2^3$.
- El signo del último término, $4$, es **siempre positivo**.

### Algoritmo: factorizar suma o diferencia de cubos

1. Confirmar que el primer y el último término son cubos, $a^3 + b^3$ o $a^3 - b^3$.
2. Para una suma de cubos, escribir la forma factorizada como $(a + b)(a^2 - ab + b^2)$. Para una diferencia de cubos, escribir $(a - b)(a^2 + ab + b^2)$.

### Ejemplo 6: Factorizar una suma de cubos

Factoriza $x^3 + 512$.

**Solución**

Notamos que $x^3$ y $512$ son cubos, pues $8^3 = 512$. Reescribimos la suma de cubos:

$$(x + 8)(x^2 - 8x + 64)$$

> **Análisis:** después de escribir la suma de cubos de esta manera, podríamos pensar en verificar si el trinomio se puede factorizar más. Sin embargo, el trinomio no puede factorizarse más, así que no hace falta comprobarlo.

### Ejemplo 7: Factorizar una diferencia de cubos

Factoriza $8x^3 - 125$.

**Solución**

Notamos que $8x^3 = (2x)^3$ y $125 = 5^3$ son cubos. Escribimos la diferencia de cubos:

$$(2x - 5)(4x^2 + 10x + 25)$$

> **Análisis:** igual que con la suma de cubos, no podremos factorizar más el trinomio.

---

## 7. Exponentes Fraccionarios o Negativos

Las expresiones con exponentes fraccionarios o negativos pueden factorizarse sacando un GCF: se busca la variable o el exponente común a cada término y se extrae elevado a la potencia más baja. Estas expresiones siguen las mismas reglas de factorización que las de exponentes enteros.

Por ejemplo, $2x^{\frac{1}{4}} + 5x^{\frac{3}{4}}$ puede factorizarse sacando $x^{\frac{1}{4}}$:

$$x^{\frac{1}{4}}\left(2 + 5x^{\frac{1}{2}}\right)$$

### Ejemplo 8: Factorizar una expresión con exponentes fraccionarios o negativos

Factoriza $3x(x + 2)^{-\frac{1}{3}} + 4(x + 2)^{\frac{2}{3}}$.

**Solución**

Sacamos el término con el menor valor del exponente. En este caso, $(x + 2)^{-\frac{1}{3}}$:

$$(x + 2)^{-\frac{1}{3}}(3x + 4(x + 2)) \quad \text{Sacamos el GCF}$$
$$(x + 2)^{-\frac{1}{3}}(3x + 4x + 8) \quad \text{Simplificamos}$$
$$(x + 2)^{-\frac{1}{3}}(7x + 8)$$

---

## Resumen de identidades de factorización

| Identidad | Forma factorizada |
|-----------|-------------------|
| Diferencia de cuadrados | $a^2 - b^2 = (a + b)(a - b)$ |
| Trinomio cuadrado perfecto | $a^2 + 2ab + b^2 = (a + b)^2$ |
| Trinomio cuadrado perfecto | $a^2 - 2ab + b^2 = (a - b)^2$ |
| Suma de cubos | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| Diferencia de cubos | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |
