# Ejemplo 2: Teorema de Factorización Lineal

Encuentra un polinomio de cuarto grado con coeficientes reales que tenga ceros $-3$, $2$, $i$, tal que $f(-2) = 100$.

## Solución

### Paso 1: Escribir los factores lineales

Como $x = i$ es un cero, por el Teorema del Conjugado Complejo $x = -i$ también lo es. Los cuatro ceros $-3$, $2$, $i$ y $-i$ dan los factores:

$$(x + 3), \quad (x - 2), \quad (x - i), \quad (x + i)$$

### Paso 2: Multiplicar los factores

$$f(x) = a(x + 3)(x - 2)(x - i)(x + i)$$

Primero multiplicamos los pares conjugados y los otros dos:

$$(x - i)(x + i) = x^2 + 1 \qquad (x + 3)(x - 2) = x^2 + x - 6$$

$$f(x) = a(x^2 + x - 6)(x^2 + 1) = a(x^4 + x^3 - 5x^2 + x - 6)$$

### Paso 3: Determinar $a$ con el punto dado

$$100 = f(-2) = a((-2)^4 + (-2)^3 - 5(-2)^2 + (-2) - 6)$$
$$100 = a(16 - 8 - 20 - 2 - 6) = -20a \implies a = -5$$

### Respuesta

$$f(x) = -5(x^4 + x^3 - 5x^2 + x - 6)$$

o en forma expandida:

$$f(x) = -5x^4 - 5x^3 + 25x^2 - 5x + 30$$
