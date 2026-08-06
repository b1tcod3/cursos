# Ejemplo 1: Encontrar los ceros de una función polinómica con ceros complejos

Encuentra los ceros de:

$$f(x) = 3x^3 + 9x^2 + x + 3$$

## Solución

### Paso 1: Posibles ceros racionales

El Teorema del Cero Racional indica que los posibles ceros son de la forma $\frac{p}{q}$, donde $p$ es factor de 3 (término constante) y $q$ es factor de 3 (coeficiente principal):

$$\frac{p}{q} = \pm 3, \pm 1, \pm \frac{1}{3}$$

### Paso 2: Probar con división sintética

Evaluamos con división sintética hasta obtener resto 0. Probamos $k = -3$:

Con coeficientes $3$, $9$, $1$, $3$ y $k = -3$:

$$3 \to 3(-3) = -9 \to 9 - 9 = 0 \to 0(-3) = 0 \to 1 + 0 = 1 \to 1(-3) = -3 \to 3 - 3 = 0$$

Resto 0, así que $-3$ es un cero:

$$f(x) = (x + 3)(3x^2 + 1)$$

### Paso 3: Resolver la cuadrática

$$3x^2 + 1 = 0 \implies x^2 = -\frac{1}{3} \implies x = \pm\frac{i\sqrt{3}}{3}$$

### Respuesta

Los ceros de $f(x)$ son:

$$-3 \qquad \text{y} \qquad \pm\frac{i\sqrt{3}}{3}$$

> En la gráfica, en $x = -3$ la curva cruza el eje (multiplicidad impar) y hay dos puntos de inflexión, el máximo para un cúbico.
