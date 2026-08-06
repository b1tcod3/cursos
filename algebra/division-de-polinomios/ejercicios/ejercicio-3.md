# Ejercicio 3: División de polinomios en una aplicación

El área de un rectángulo está dada por $3x^3 + 14x^2 - 23x + 6$. El ancho del rectángulo está dado por $x + 6$. Encuentra una expresión para el **largo** del rectángulo.

<details>
<summary>Ver respuesta</summary>

El largo es el área dividida por el ancho:

$$\text{Largo} = \frac{3x^3 + 14x^2 - 23x + 6}{x + 6}$$

Dividiendo: $3x^2(x + 6) = 3x^3 + 18x^2$; resto $-4x^2 - 23x$. Luego $-4x(x + 6) = -4x^2 - 24x$; resto $x + 6$. Finalmente $1(x + 6) = x + 6$; resto $0$.

El largo del rectángulo es:

$$3x^2 - 4x + 1$$

**Verificación:** $(x + 6)(3x^2 - 4x + 1) = 3x^3 - 4x^2 + x + 18x^2 - 24x + 6 = 3x^3 + 14x^2 - 23x + 6 \quad ✔$
</details>
