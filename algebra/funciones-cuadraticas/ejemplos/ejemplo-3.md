# Ejemplo 3: Interceptos $x$ de una parábola (forma estándar)

Encuentra los interceptos $x$ de la función cuadrática:

$$f(x) = 2x^2 + 4x - 4$$

## Solución

Resolvemos para cuando la salida es cero:

$$0 = 2x^2 + 4x - 4$$

Como la cuadrática no es fácilmente factorizable, reescribimos en forma estándar $f(x) = a(x - h)^2 + k$.

### Paso 1: Calcular $h$

$$h = -\frac{b}{2a} = -\frac{4}{2(2)} = -1$$

### Paso 2: Calcular $k$

$$k = f(h) = f(-1) = 2(-1)^2 + 4(-1) - 4 = -6$$

### Paso 3: Reescribir en forma estándar

Con $a = 2$, $h = -1$ y $k = -6$:

$$f(x) = 2(x + 1)^2 - 6$$

### Paso 4: Resolver para los interceptos $x$

$$0 = 2(x + 1)^2 - 6$$
$$6 = 2(x + 1)^2$$
$$3 = (x + 1)^2$$
$$x + 1 = \pm\sqrt{3}$$
$$x = -1 \pm \sqrt{3}$$

Los interceptos $x$ están en $(-1 - \sqrt{3}, 0)$ y $(-1 + \sqrt{3}, 0)$.

### Verificación con la fórmula cuadrática

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{-4 \pm \sqrt{4^2 - 4(2)(-4)}}{2(2)} = \frac{-4 \pm \sqrt{48}}{4} = -1 \pm \sqrt{3} \quad ✔$$
