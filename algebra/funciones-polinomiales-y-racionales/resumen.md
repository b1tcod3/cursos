# Resumen del Capítulo 5: Funciones polinomiales y racionales

## Glosario

### A–C
- **Asíntota horizontal:** recta horizontal $y = b$ a la que la gráfica se acerca cuando las entradas crecen o decrecen sin límite.
- **Asíntota vertical:** recta vertical $x = a$ hacia la cual la gráfica tiende a $+\infty$ o $-\infty$ cuando las entradas se acercan a $a$.
- **Coeficiente principal:** el coeficiente del término principal.
- **Curva suave:** gráfica sin esquinas afiladas.
- **Comportamiento local/terminal (notación de flechas):** forma de representar simbólicamente el comportamiento local y terminal de una función usando flechas para indicar que una entrada o salida se acerca a un valor.

### D–L
- **División sintética:** método abreviado para dividir un polinomio por un binomio de la forma $x - k$.
- **Eje de simetría:** recta vertical que pasa por el vértice de una parábola, alrededor de la cual la parábola es simétrica; se define por $x = -\frac{b}{2a}$.
- **Forma estándar de una función cuadrática:** la función que describe una parábola, $f(x) = a(x - h)^2 + k$, donde $(h, k)$ es el vértice.
- **Forma general de una función cuadrática:** $f(x) = ax^2 + bx + c$, donde $a$, $b$ y $c$ son reales y $a \neq 0$.
- **Forma de vértice de una función cuadrática:** otro nombre para la forma estándar de una función cuadrática.
- **Función inyectiva (uno-a-uno):** cualquier función que tiene función inversa.
- **Función polinomial:** función que consiste de cero o la suma de un número finito de términos no nulos, cada uno producto de un número (el coeficiente del término) y una variable elevada a una potencia entera no negativa.
- **Función potencia:** función de la forma $f(x) = kx^p$, donde $k$ es constante, la base es una variable y el exponente $p$ es constante.
- **Función racional:** función que puede escribirse como el cociente de dos polinomios.
- **Grado de un polinomio:** la mayor potencia de la variable que ocurre en un polinomio.
- **Ley de Signos de Descartes:** regla que determina el máximo número posible de ceros reales positivos y negativos según el número de cambios de signo de $f(x)$ y $f(-x)$.

### M–V
- **Multiplicidad:** el número de veces que un factor dado aparece en la forma factorizada de la ecuación de un polinomio; si un polinomio contiene un factor de la forma $(x - h)^p$, entonces $x = h$ es un cero de multiplicidad $p$.
- **Notación de flechas:** ver *Comportamiento local/terminal*.
- **Punto de giro:** el lugar donde la gráfica de una función cambia de dirección.
- **Raíces:** en una función dada, los valores de $x$ para los cuales $y = 0$; también llamados ceros.
- **Término de una función polinomial:** cualquier $a_i x^i$ de una función de la forma $f(x) = a_n x^n + \dots + a_2 x^2 + a_1 x + a_0$.
- **Término principal:** el término que contiene la mayor potencia de la variable.
- **Teorema de la factorización lineal:** permitiendo multiplicidades, una función polinomial tendrá el mismo número de factores que su grado, y cada factor tendrá la forma $(x - c)$, donde $c$ es un número complejo.
- **Teorema de la raíz racional:** los posibles ceros racionales de una función polinomial tienen la forma $\frac{p}{q}$, donde $p$ es factor del término constante y $q$ es factor del coeficiente principal.
- **Teorema del resto:** si un polinomio $f(x)$ se divide entre $x - k$, entonces el resto es igual al valor $f(k)$.
- **Teorema del valor intermedio:** para dos números $a$ y $b$ en el dominio de $f$, si $a < b$ y $f(a) \neq f(b)$, entonces la función $f$ toma todos los valores entre $f(a)$ y $f(b)$; en particular, cuando una función polinomial cambia de valor negativo a positivo, la función debe cruzar el eje $x$.
- **Teorema fundamental del álgebra:** una función polinomial de grado mayor que 0 tiene al menos un cero complejo.
- **Discontinuidad removible:** punto único en el que una función es indefinida y que, si se rellenara, haría la función continua; aparece como un hueco en la gráfica.
- **Varias directamente:** relación donde una cantidad es una constante multiplicada por la otra cantidad.
- **Varias inversamente:** relación donde una cantidad es una constante dividida por la otra cantidad.
- **Variación conjunta:** relación donde una variable varía directamente o inversamente con varias variables.
- **Vértice:** el punto en el que una parábola cambia de dirección, correspondiente al valor mínimo o máximo de la función cuadrática.
- **Zeros:** en una función dada, los valores de $x$ para los cuales $y = 0$; también llamados raíces.

### Otros
- **Algoritmo de división:** dado un dividendo polinomial $f(x)$ y un divisor no nulo $d(x)$ donde el grado de $d(x)$ es menor o igual que el grado de $f(x)$, existen polinomios únicos $q(x)$ y $r(x)$ tales que $f(x) = d(x)q(x) + r(x)$, donde $q(x)$ es el cociente y $r(x)$ el resto; el resto es cero o tiene grado estrictamente menor que $d(x)$.
- **Constante de variación:** el valor no nulo $k$ que ayuda a definir la relación entre las variables en la variación directa o inversa.
- **Máximo local/global:** punto más alto de una gráfica; $f(a)$ donde $f(a) \geq f(x)$ para toda $x$.
- **Mínimo local/global:** punto más bajo de una gráfica; $f(a)$ donde $f(a) \leq f(x)$ para toda $x$.
- **Comportamiento terminal:** el comportamiento de la gráfica de una función cuando la entrada decrece sin límite y crece sin límite.
- **Coeficiente:** número real no nulo multiplicado por una variable elevada a un exponente.
- **Función continua:** función cuya gráfica puede dibujarse sin levantar el lápiz del papel porque no hay rupturas en la gráfica.

## Ecuaciones clave

| Nombre | Ecuación |
|---|---|
| Forma general de una función cuadrática | $f(x) = ax^2 + bx + c$ |
| Forma estándar de una función cuadrática | $f(x) = a(x - h)^2 + k$ |
| Forma general de una función polinomial | $f(x) = a_n x^n + \dots + a_2 x^2 + a_1 x + a_0$ |
| Algoritmo de división | $f(x) = d(x)q(x) + r(x)$ |
| Función racional | $f(x) = \frac{P(x)}{Q(x)} = \frac{a_p x^p + a_{p-1} x^{p-1} + \dots + a_1 x + a_0}{b_q x^q + b_{q-1} x^{q-1} + \dots + b_1 x + b_0}$, $Q(x) \neq 0$ |
| Variación directa | $y = kx^n$, $k$ constante no nula |
| Variación inversa | $y = \frac{k}{x^n}$, $k$ constante no nula |

## Conceptos clave por sección

### 5.1 Funciones cuadráticas
- Una función polinomial de grado dos se llama función cuadrática.
- La gráfica de una función cuadrática es una parábola, una curva con forma de U que puede abrir hacia arriba o hacia abajo.
- El eje de simetría es la recta vertical que pasa por el vértice. Los ceros, o interceptos $x$, son los puntos donde la parábola cruza el eje $x$. El intercepto $y$ es donde cruza el eje $y$.
- Las funciones cuadráticas suelen escribirse en forma general; la forma estándar (de vértice) sirve para identificar el vértice con facilidad. Cualquiera de las dos puede escribirse desde una gráfica.
- El vértice puede hallarse a partir de la ecuación de la función cuadrática.
- El dominio de una función cuadrática son todos los números reales; el rango varía según la función.
- El valor mínimo o máximo de una función cuadrática está dado por el valor $y$ del vértice.
- El mínimo o máximo permite determinar el rango y resolver problemas del mundo real (área, ingresos).
- El vértice y los interceptos pueden identificarse e interpretarse para resolver problemas reales.

### 5.2 Funciones potencia y funciones polinomiales
- Una función potencia es una base variable elevada a un exponente numérico.
- El comportamiento de una gráfica cuando la entrada crece o decrece sin límite se llama comportamiento terminal.
- El comportamiento terminal depende de si la potencia es par o impar.
- Una función polinomial es la suma de términos, cada uno función potencia transformada con exponente entero positivo.
- El grado de una función polinomial es la mayor potencia de la variable; el término que la contiene es el término principal y su coeficiente es el coeficiente principal.
- El comportamiento terminal de una función polinomial es igual al de la función potencia representada por el término principal.
- Un polinomio de grado $n$ tiene a lo más $n$ interceptos $x$ y a lo más $n - 1$ puntos de giro.

### 5.3 Gráficas de funciones polinomiales
- Las funciones polinomiales de grado 2 o más son funciones suaves y continuas.
- Para hallar los ceros de una función polinomial, factorizar y hacer cada factor igual a cero (o graficar e identificar los cruces con el eje $x$).
- La multiplicidad de un cero determina cómo se comporta la gráfica en el intercepto: cruza el eje con multiplicidad impar y solo lo toca con multiplicidad par.
- El comportamiento terminal depende del término principal.
- Una función polinomial de grado $n$ tiene a lo más $n - 1$ puntos de giro.
- Para graficar: hallar los ceros y sus multiplicidades, determinar el comportamiento terminal y asegurar a lo más $n - 1$ puntos de giro.
- El teorema del valor intermedio: si $f(a)$ y $f(b)$ tienen signos opuestos, existe al menos un valor $c$ entre $a$ y $b$ con $f(c) = 0$.

### 5.4 División de polinomios
- La división larga sirve para dividir un polinomio entre cualquier polinomio de grado menor o igual.
- El algoritmo de división permite escribir el dividendo como producto del divisor por el cociente más el resto.
- La división sintética es un atajo para dividir entre binomios de la forma $x - k$.
- La división de polinomios resuelve problemas de aplicación (área, volumen).

### 5.5 Ceros de funciones polinomiales
- Teorema del resto: para hallar $f(k)$, determinamos el resto de dividir $f(x)$ entre $x - k$.
- Teorema del factor: $k$ es cero de $f(x)$ si y solo si $(x - k)$ es factor de $f(x)$.
- Teorema de la raíz racional: cada cero racional de una función polinomial con coeficientes enteros es un factor del término constante dividido por un factor del coeficiente principal. Si el coeficiente principal es 1, los posibles ceros racionales son los factores del término constante.
- La división sintética se usa para hallar ceros.
- Teorema fundamental del álgebra: toda función polinomial de grado mayor que 0 tiene al menos un cero complejo.
- Permitiendo multiplicidades, una función polinomial tiene el mismo número de factores que su grado; cada factor es de la forma $(x - c)$ con $c$ complejo.
- Número de ceros reales positivos: el número de cambios de signo de $f(x)$ o menos por un entero par.
- Número de ceros reales negativos: el número de cambios de signo de $f(-x)$ o menos por un entero par.
- Las ecuaciones polinomiales modelan escenarios reales; resolverlas es más fácil con división sintética.

### 5.6 Funciones racionales
- Se usa notación de flechas para describir el comportamiento local y terminal de $f(x) = \frac{1}{x}$ y $f(x) = \frac{1}{x^2}$.
- Una función que se nivela en un valor horizontal tiene asíntota horizontal; puede tener más de una asíntota vertical.
- Los problemas de tasas y concentraciones suelen involucrar funciones racionales.
- El dominio de una función racional incluye todos los reales excepto los que hacen el denominador cero.
- Las asíntotas verticales ocurren donde el denominador es cero y el numerador no.
- Una discontinuidad removible puede ocurrir si una entrada hace cero numerador y denominador a la vez.
- El comportamiento terminal de una función racional refleja el cociente de los términos principales.
- Para graficar: hallar interceptos, comportamiento en interceptos y asíntotas, y comportamiento terminal.
- Si hay interceptos $x$ en $x_1, x_2, \dots, x_n$ y asíntotas verticales en $v_1, v_2, \dots, v_m$ (sin que ningún $x_i = v_j$):
  $$f(x) = \frac{a(x - x_1)^{p_1}(x - x_2)^{p_2} \cdots (x - x_n)^{p_n}}{(x - v_1)^{q_1}(x - v_2)^{q_2} \cdots (x - v_m)^{q_m}}$$

### 5.7 Funciones inversas y radicales
- La inversa de una función cuadrática es una función raíz cuadrada.
- Si $f^{-1}$ es la inversa de $f$, entonces $f$ es la inversa de $f^{-1}$.
- No es posible hallar la inversa de la mayoría de las funciones polinomiales, pero algunos polinomios básicos son invertibles.
- Para hallar la inversa de ciertas funciones, se debe restringir el dominio para que sea uno-a-uno.
- Al hallar la inversa de una función radical, se necesita una restricción en el dominio de la respuesta.
- Las funciones inversas y radicales resuelven problemas de aplicación.

### 5.8 Modelado con variación
- Una relación donde una cantidad es una constante multiplicada por otra es variación directa.
- Dos variables directamente proporcionales tienen razón constante.
- Una relación donde una cantidad es una constante dividida por otra es variación inversa.
- Dos variables inversamente proporcionales tienen producto constante.
- Cuando una variable varía directa o inversamente con varias variables, es variación conjunta.
