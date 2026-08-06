# Funciones Cuadráticas y Aplicaciones 📈

Una función cuadrática es de la forma $f(x) = ax^2 + bx + c$ con $a \neq 0$. Su gráfica es una parábola. En este tema estudiamos cómo usar el vértice y los interceptos para resolver aplicaciones reales.

## 1. Aplicaciones: Máximo Ingreso (Revenue)

El ingreso ($Revenue$) es la cantidad de dinero que una empresa recibe. El vértice de una parábola que abre hacia abajo ($a < 0$) nos indica el punto máximo.

### Algoritmo: maximizar el ingreso

Dada una aplicación que involucra ingreso, usa una ecuación cuadrática para encontrar el máximo:

1. Escribir una **ecuación cuadrática** para la función de ingreso.
2. Encontrar el **vértice** de la ecuación cuadrática.
3. Determinar el **valor de $y$ del vértice**.

### Ejemplo 1: Encontrar el máximo ingreso

El precio unitario de un artículo afecta su oferta y demanda. Un periódico local tiene actualmente 84 000 suscriptores con una tarifa trimestral de \$30. La investigación de mercado sugiere que si los dueños suben el precio a \$32, perderían 5 000 suscriptores. Suponiendo que las suscripciones están linealmente relacionadas con el precio, ¿qué precio debería cobrar el periódico por una suscripción trimestral para **maximizar su ingreso**?

**Solución**

El ingreso se calcula multiplicando el precio por suscripción por el número de suscriptores (cantidad). Introducimos variables: $p$ para el precio por suscripción y $Q$ para la cantidad:

$$Ingreso = pQ$$

Como el número de suscriptores cambia con el precio, buscamos una relación lineal entre las variables. Sabemos que actualmente $p = 30$ y $Q = 84\,000$, y que si el precio sube a \$32, se perderían 5 000 suscriptores: $p = 32$ y $Q = 79\,000$. La pendiente es:

$$m = \frac{79\,000 - 84\,000}{32 - 30} = \frac{-5\,000}{2} = -2\,500$$

Esto indica que se pierden 2 500 suscriptores por cada dólar de aumento. Resolvemos para el intercepto $b$:

$$Q = -2\,500p + b$$
$$84\,000 = -2\,500(30) + b$$
$$b = 159\,000$$

Obtenemos la ecuación lineal $Q = -2\,500p + 159\,000$. Volvemos a la ecuación de ingreso:

$$Ingreso = pQ = p(-2\,500p + 159\,000) = -2\,500p^2 + 159\,000p$$

Tenemos una función cuadrática para el ingreso en función de la tarifa. Para encontrar el precio que maximiza el ingreso, hallamos el vértice:

$$h = -\frac{159\,000}{2(-2\,500)} = 31.8$$

El modelo indica que el ingreso máximo ocurre al cobrar **\$31.80** por la suscripción. Para el ingreso máximo, evaluamos:

$$Ingreso_{máx} = -2\,500(31.8)^2 + 159\,000(31.8) = 2\,528\,100$$

El ingreso máximo es de **\$2 528 100**.

> **Análisis:** esto también podría resolverse graficando la cuadrática; el máximo del ingreso se observa en el vértice de la parábola.

---

## 2. Interceptos $x$ e $y$ de una Función Cuadrática

Recordemos que el intercepto $y$ se obtiene evaluando la función en $x = 0$, y los interceptos $x$ se encuentran donde la salida es cero.

### Algoritmo: encontrar los interceptos de $f(x)$

1. Evaluar $f(0)$ para encontrar el **intercepto $y$**.
2. Resolver la ecuación cuadrática $f(x) = 0$ para encontrar los **interceptos $x$**.

> **Nota:** la cantidad de interceptos $x$ puede variar según la ubicación de la gráfica: una parábola puede tener 2, 1 o 0 interceptos en $x$.

### Ejemplo 2: Interceptos $y$ y $x$ de una parábola

Encuentra los interceptos de $f(x) = 3x^2 + 5x - 2$.

**Solución**

Intercepto $y$: evaluamos $f(0)$.

$$f(0) = 3(0)^2 + 5(0) - 2 = -2$$

El intercepto $y$ está en $(0, -2)$.

Interceptos $x$: resolvemos $f(x) = 0$.

$$0 = 3x^2 + 5x - 2$$

En este caso, la cuadrática se factoriza fácilmente:

$$0 = (3x - 1)(x + 2)$$

Los interceptos $x$ están en $\left(\frac{1}{3}, 0\right)$ y $(-2, 0)$.

> **Análisis:** al graficar, se confirma que la gráfica cruza el eje $y$ en $(0, -2)$ y el eje $x$ en $\left(\frac{1}{3}, 0\right)$ y $(-2, 0)$.

---

## 3. Reescribir Cuadráticas en Forma Estándar

En el ejemplo anterior, la cuadrática se resolvió fácilmente factorizando. Sin embargo, hay muchas cuadráticas que no pueden factorizarse. Podemos resolverlas reescribiéndolas primero en forma estándar:

$$f(x) = a(x - h)^2 + k$$

### Algoritmo: encontrar los interceptos $x$ reescribiendo en forma estándar

1. Sustituir $a$ y $b$ en $h = -\frac{b}{2a}$.
2. Sustituir $x = h$ en la forma general de la función cuadrática para encontrar $k$.
3. Reescribir la cuadrática en forma estándar usando $h$ y $k$.
4. Resolver para cuando la salida de la función sea cero.

### Ejemplo 3: Interceptos $x$ de una parábola

Encuentra los interceptos $x$ de $f(x) = 2x^2 + 4x - 4$.

**Solución**

Resolvemos para cuando la salida es cero:

$$0 = 2x^2 + 4x - 4$$

Como la cuadrática no es fácilmente factorizable, resolvemos reescribiendo en forma estándar $f(x) = a(x - h)^2 + k$. Sabemos que $a = 2$; resolvemos para $h$ y $k$:

$$h = -\frac{b}{2a} = -\frac{4}{2(2)} = -1$$
$$k = f(h) = f(-1) = 2(-1)^2 + 4(-1) - 4 = -6$$

Ahora reescribimos en forma estándar:

$$f(x) = 2(x + 1)^2 - 6$$

Resolvemos para cuando la salida es cero:

$$0 = 2(x + 1)^2 - 6$$
$$6 = 2(x + 1)^2$$
$$3 = (x + 1)^2$$
$$x + 1 = \pm\sqrt{3}$$
$$x = -1 \pm \sqrt{3}$$

Los interceptos $x$ están en $(-1 - \sqrt{3}, 0)$ y $(-1 + \sqrt{3}, 0)$.

> **Análisis:** también podríamos haber llegado al mismo resultado con la fórmula cuadrática. Con $a = 2$, $b = 4$ y $c = -4$:
>
> $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{-4 \pm \sqrt{4^2 - 4(2)(-4)}}{2(2)} = \frac{-4 \pm \sqrt{48}}{4} = \frac{-4 \pm \sqrt{3(16)}}{4} = -1 \pm \sqrt{3}$$

---

## 4. Aplicación: Vértice e Interceptos de una Parábola

### Ejemplo 4: Aplicando el vértice y los interceptos de una parábola

Se lanza una pelota hacia arriba desde la azotea de un edificio de 40 pies de altura con una velocidad de 80 pies por segundo. La altura de la pelota sobre el suelo se modela con la ecuación $H(t) = -16t^2 + 80t + 40$.

a. ¿Cuándo alcanza la pelota su altura máxima?

b. ¿Cuál es la altura máxima de la pelota?

c. ¿Cuándo cae la pelota al suelo?

**Solución**

**a.** La pelota alcanza la altura máxima en el vértice de la parábola.

$$h = -\frac{80}{2(-16)} = \frac{80}{32} = \frac{5}{2} = 2.5$$

La pelota alcanza la altura máxima después de **2.5 segundos**.

**b.** Para la altura máxima, encontramos la coordenada $y$ del vértice:

$$k = H\left(-\frac{b}{2a}\right) = H(2.5) = -16(2.5)^2 + 80(2.5) + 40 = 140$$

La pelota alcanza una altura máxima de **140 pies**.

**c.** Para saber cuándo cae la pelota, determinamos cuándo la altura es cero, $H(t) = 0$. Usamos la fórmula cuadrática:

$$t = \frac{-80 \pm \sqrt{80^2 - 4(-16)(40)}}{2(-16)} = \frac{-80 \pm \sqrt{8960}}{-32}$$

Como la raíz no se simplifica fácilmente, aproximamos:

$$t = \frac{-80 - \sqrt{8960}}{-32} \approx 5.458 \qquad \text{o} \qquad t = \frac{-80 + \sqrt{8960}}{-32} \approx -0.458$$

La segunda respuesta está fuera del dominio razonable del modelo, por lo que concluimos que la pelota toca el suelo después de aproximadamente **5.458 segundos**.

> **Nota:** la gráfica no representa la trayectoria física de la pelota hacia arriba y hacia abajo. Ten en cuenta las cantidades de cada eje al interpretar la gráfica.
