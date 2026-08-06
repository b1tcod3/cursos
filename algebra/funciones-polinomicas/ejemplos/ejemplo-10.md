# Ejemplo 10: Extremos locales en una aplicación

Se construirá una caja abierta cortando cuadrados en cada esquina de una lámina de plástico de 14 cm por 20 cm y doblando los lados. Encuentra el tamaño de los cuadrados que deben cortarse para **maximizar el volumen**.

## Solución

### Paso 1: Escribir la función de volumen

Con $w$ = lado del cuadrado cortado, la base queda de $(20 - 2w)$ por $(14 - 2w)$ cm y la altura es $w$ cm:

$$V(w) = (20 - 2w)(14 - 2w)w = 280w - 68w^2 + 4w^3$$

### Paso 2: Analizar el dominio razonable

Los ceros de los factores $w$, $20 - 2w$ y $14 - 2w$ son $0$, $10$ y $7$. Una altura de 0 cm no es razonable; además, al cortar dos cuadrados del lado más corto (14), $w$ debe satisfacer:

$$0 < w < 7$$

### Paso 3: Estimar el máximo con tecnología

Restringiendo el dominio a $[0, 7]$, la gráfica permite estimar el máximo del volumen en alrededor de **340 cm³** cuando los cuadrados miden unos **2.75 cm** por lado.

### Paso 4: Refinar la estimación

Acercando la vista a la gráfica, se refina la estimación a un máximo de aproximadamente **339 cm³** cuando los cuadrados miden **2.7 cm** por lado.

### Respuesta

Se deben cortar cuadrados de aproximadamente **2.7 cm** por lado para maximizar el volumen.
