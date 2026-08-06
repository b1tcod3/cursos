# Ejemplo 6: División de polinomios en un problema de aplicación

El volumen de un sólido rectangular está dado por el polinomio $3x^4 - 3x^3 - 33x^2 + 54x$. El largo del sólido es $3x$ y el ancho es $x - 2$. Encuentra la altura $h$ del sólido.

## Solución

### Paso 1: Plantear la ecuación

$$V = l \cdot w \cdot h \quad \Rightarrow \quad 3x^4 - 3x^3 - 33x^2 + 54x = 3x \cdot (x - 2) \cdot h$$

### Paso 2: Dividir ambos lados entre $3x$

$$\frac{3x \cdot (x - 2) \cdot h}{3x} = \frac{3x^4 - 3x^3 - 33x^2 + 54x}{3x}$$
$$(x - 2)h = x^3 - x^2 - 11x + 18$$

### Paso 3: Dividir con división sintética

Despejamos $h$:

$$h = \frac{x^3 - x^2 - 11x + 18}{x - 2}$$

Con $k = 2$ y coeficientes $1$, $-1$, $-11$, $18$:

| Operación | Resultado |
|-----------|-----------|
| Bajar | $1$ |
| $1 \cdot 2$ | $2$ |
| $-1 + 2$ | $1$ |
| $1 \cdot 2$ | $2$ |
| $-11 + 2$ | $-9$ |
| $-9 \cdot 2$ | $-18$ |
| $18 + (-18)$ | $0$ (resto) |

### Resultado

La altura del sólido es:

$$h = x^2 + x - 9$$
