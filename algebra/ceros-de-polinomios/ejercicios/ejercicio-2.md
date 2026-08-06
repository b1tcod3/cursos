# Ejercicio 2: Teorema de Factorización Lineal

Encuentra un polinomio de tercer grado con coeficientes reales que tenga ceros $5$ y $-2i$, tal que $f(1) = 10$.

<details>
<summary>Ver respuesta</summary>

Como $-2i$ es un cero y los coeficientes son reales, su conjugado $2i$ también es cero. Los factores son $(x - 5)$, $(x + 2i)$ y $(x - 2i)$:

$$f(x) = a(x - 5)(x + 2i)(x - 2i) = a(x - 5)(x^2 + 4)$$

Con $f(1) = 10$:

$$10 = a(1 - 5)(1^2 + 4) = a(-4)(5) = -20a \implies a = -\frac{1}{2}$$

El polinomio es:

$$f(x) = -\frac{1}{2}(x - 5)(x^2 + 4) = -\frac{1}{2}x^3 + \frac{5}{2}x^2 - 2x + 10$$
</details>
