# Ejemplo 2: División larga de un polinomio de tercer grado

Divide:

$$6x^3 + 11x^2 - 31x + 15 \quad \text{entre} \quad 3x - 2$$

## Solución

### Paso 1: Dividir los términos principales

$$\frac{6x^3}{3x} = 2x^2$$

$$2x^2(3x - 2) = 6x^3 - 4x^2$$

Restando: $(6x^3 + 11x^2) - (6x^3 - 4x^2) = 15x^2$. Bajamos $-31x$.

### Paso 2: Continuar

$$\frac{15x^2}{3x} = 5x \qquad 5x(3x - 2) = 15x^2 - 10x$$

Restando: $(15x^2 - 31x) - (15x^2 - 10x) = -21x$. Bajamos $15$.

### Paso 3: Último término

$$\frac{-21x}{3x} = -7 \qquad -7(3x - 2) = -21x + 14$$

Restando: $15 - 14 = 1$.

### Resultado

El cociente es $2x^2 + 5x - 7$ y el resto es $1$:

$$\frac{6x^3 + 11x^2 - 31x + 15}{3x - 2} = 2x^2 + 5x - 7 + \frac{1}{3x - 2}$$

### Verificación

$$(3x - 2)(2x^2 + 5x - 7) + 1 = 6x^3 + 15x^2 - 21x - 4x^2 - 10x + 14 + 1 = 6x^3 + 11x^2 - 31x + 15 \quad ✔$$

> **Identificación:** dividendo $6x^3 + 11x^2 - 31x + 15$, divisor $3x - 2$, cociente $2x^2 + 5x - 7$, resto $1$.
