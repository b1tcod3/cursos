# División de Polinomios ➗

## 1. El Algoritmo de División

> **Definición (Algoritmo de División):** dado un dividendo polinómico $f(x)$ y un divisor $d(x)$ distinto de cero, donde el grado de $d(x)$ es menor o igual que el grado de $f(x)$, existen polinomios únicos $q(x)$ y $r(x)$ tales que:
>
> $$f(x) = d(x)q(x) + r(x)$$
>
> $q(x)$ es el **cociente** y $r(x)$ es el **resto**. El resto es cero o tiene grado estrictamente menor que $d(x)$.
>
> Si $r(x) = 0$, entonces $d(x)$ divide exactamente a $f(x)$; en ese caso, tanto $d(x)$ como $q(x)$ son factores de $f(x)$.

### Algoritmo: división larga de un polinomio entre un binomio

1. Plantear el problema de división.
2. Determinar el primer término del cociente dividiendo el **término principal del dividendo** entre el **término principal del divisor**.
3. Multiplicar la respuesta por el divisor y escribirla debajo de los términos semejantes del dividendo.
4. Restar el binomio inferior del binomio superior.
5. Bajar el siguiente término del dividendo.
6. Repetir los pasos 2–5 hasta llegar al último término del dividendo.
7. Si el resto no es cero, expresarlo como fracción usando el divisor como denominador.

### Ejemplo 1: División larga de un polinomio de segundo grado

Divide $5x^2 + 3x - 2$ entre $x + 1$.

**Solución**

El cociente es $5x - 2$ y el resto es $0$. Escribimos el resultado como:

$$\frac{5x^2 + 3x - 2}{x + 1} = 5x - 2 \qquad \text{o} \qquad 5x^2 + 3x - 2 = (x + 1)(5x - 2)$$

> **Análisis:** el resto fue $0$, lo que indica que el dividendo se divide exactamente por el divisor, y que el divisor es un **factor** del dividendo.

### Ejemplo 2: División larga de un polinomio de tercer grado

Divide $6x^3 + 11x^2 - 31x + 15$ entre $3x - 2$.

**Solución**

Hay un resto de $1$. Podemos expresar el resultado como:

$$\frac{6x^3 + 11x^2 - 31x + 15}{3x - 2} = 2x^2 + 5x - 7 + \frac{1}{3x - 2}$$

**Verificación con el Algoritmo de División:**

$$(3x - 2)(2x^2 + 5x - 7) + 1 = 6x^3 + 11x^2 - 31x + 15$$

Al escribir el resultado identificamos:

- **Dividendo:** $6x^3 + 11x^2 - 31x + 15$
- **Divisor:** $3x - 2$
- **Cociente:** $2x^2 + 5x - 7$
- **Resto:** $1$

---

## 2. División Sintética

La división larga puede involucrar muchos pasos. La **división sintética** es un método abreviado para dividir por un factor lineal de la forma $x - k$ (donde $k$ es un número real), usando **solo los coeficientes**.

### Algoritmo: división sintética

1. Escribir $k$ para el divisor.
2. Escribir los **coeficientes** del dividendo.
3. **Bajar** el coeficiente principal.
4. **Multiplicar** el coeficiente principal por $k$ y escribir el producto en la siguiente columna.
5. **Sumar** los términos de la segunda columna.
6. **Multiplicar** el resultado por $k$ y escribir el producto en la siguiente columna.
7. Repetir los pasos 5 y 6 para las columnas restantes.
8. Usar los números de la fila inferior para escribir el cociente: el último número es el resto (grado 0), el siguiente a la izquierda tiene grado 1, el siguiente grado 2, y así sucesivamente.

### Ejemplo 3: División sintética de un polinomio de segundo grado

Usa división sintética para dividir $5x^2 - 3x - 36$ entre $x - 3$.

**Solución**

Escribimos $k = 3$ y los coeficientes $5$, $-3$, $-36$. Bajamos el coeficiente principal, lo multiplicamos por $k$ y sumamos en cada columna:

$$5 \to 5(3) = 15 \to -3 + 15 = 12 \to 12(3) = 36 \to -36 + 36 = 0$$

El resultado es **$5x + 12$** con resto **$0$**. Así, $x - 3$ es factor del polinomio original.

**Verificación:**

$$(x - 3)(5x + 12) + 0 = 5x^2 - 3x - 36$$

### Ejemplo 4: División sintética de un polinomio de tercer grado

Usa división sintética para dividir $4x^3 + 10x^2 - 6x - 20$ entre $x + 2$.

**Solución**

El divisor binomial es $x + 2$, así que $k = -2$. Con los coeficientes $4$, $10$, $-6$, $-20$:

$$4 \to 4(-2) = -8 \to 10 - 8 = 2 \to 2(-2) = -4 \to -6 - 4 = -10 \to -10(-2) = 20 \to -20 + 20 = 0$$

El resultado es **$4x^2 + 2x - 10$** con resto **$0$**. Así, $x + 2$ es factor de $4x^3 + 10x^2 - 6x - 20$.

> **Análisis:** la gráfica de $f(x) = 4x^3 + 10x^2 - 6x - 20$ muestra un cero en $x = k = -2$, lo que confirma que $x + 2$ es factor.

### Ejemplo 5: División sintética de un polinomio de cuarto grado

Usa división sintética para dividir $-9x^4 + 10x^3 + 7x^2 - 6$ entre $x - 1$.

**Solución**

Nota que **no hay término en $x$**; usaremos un cero como coeficiente para ese término. Con $k = 1$ y los coeficientes $-9$, $10$, $7$, $0$, $-6$:

$$-9 \to -9(1) = -9 \to 10 - 9 = 1 \to 1(1) = 1 \to 7 + 1 = 8 \to 8(1) = 8 \to 0 + 8 = 8 \to 8(1) = 8 \to -6 + 8 = 2$$

El resultado es:

$$-9x^3 + x^2 + 8x + 8 + \frac{2}{x - 1}$$

---

## 3. Aplicaciones de la División de Polinomios

La división de polinomios se usa en problemas de área y volumen, donde hay que despejar una dimensión.

### Ejemplo 6: División de polinomios en un problema de aplicación

El volumen de un sólido rectangular está dado por el polinomio $3x^4 - 3x^3 - 33x^2 + 54x$. El largo del sólido es $3x$ y el ancho es $x - 2$. Encuentra la altura $h$ del sólido.

**Solución**

Usamos la fórmula del volumen de un sólido rectangular $V = l \cdot w \cdot h$:

$$3x^4 - 3x^3 - 33x^2 + 54x = 3x \cdot (x - 2) \cdot h$$

Para despejar $h$, primero dividimos ambos lados entre $3x$:

$$\frac{3x \cdot (x - 2) \cdot h}{3x} = \frac{3x^4 - 3x^3 - 33x^2 + 54x}{3x}$$
$$(x - 2)h = x^3 - x^2 - 11x + 18$$

Ahora despejamos $h$ con división sintética:

$$h = \frac{x^3 - x^2 - 11x + 18}{x - 2}$$

El cociente es $x^2 + x - 9$ y el resto es $0$. La altura del sólido es:

$$h = x^2 + x - 9$$
