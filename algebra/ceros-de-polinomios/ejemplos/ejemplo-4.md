# Ejemplo 4: Resolver una aplicación con ecuaciones polinómicas

Una panadería quiere que el volumen de un pastel pequeño sea de 351 pulgadas cúbicas. El pastel tiene forma de sólido rectangular: el largo debe ser cuatro pulgadas más largo que el ancho, y la altura un tercio del ancho. ¿Cuáles deben ser las dimensiones del molde?

## Solución

### Paso 1: Escribir la ecuación del volumen

Con $l = w + 4$ y $h = \frac{1}{3}w$:

$$V = (w + 4)(w)\left(\frac{1}{3}w\right) = \frac{1}{3}w^3 + \frac{4}{3}w^2$$

### Paso 2: Sustituir el volumen y simplificar

$$351 = \frac{1}{3}w^3 + \frac{4}{3}w^2$$
$$1053 = w^3 + 4w^2$$
$$0 = w^3 + 4w^2 - 1053$$

### Paso 3: Analizar las posibles soluciones

Descartes indica **una solución positiva**. Los posibles ceros racionales son $\pm 3, \pm 9, \pm 13, \pm 27, \pm 39, \pm 81, \pm 117, \pm 351$ y $\pm 1053$. Solo probamos positivos con división sintética:

- $w = 1$: resto distinto de 0.
- $w = 3$: resto distinto de 0.
- $w = 9$: resto **0** ✔

### Paso 4: Calcular las demás dimensiones

$$l = w + 4 = 9 + 4 = 13$$
$$h = \frac{1}{3}w = \frac{1}{3}(9) = 3$$

### Respuesta

El molde debe tener dimensiones de **13 × 9 × 3 pulgadas**.
