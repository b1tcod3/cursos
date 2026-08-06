# Ejercicio 5: Escribir una fórmula para una función polinómica

> Este ejercicio originalmente pide analizar la gráfica de la Figura 5.51, que no está disponible en estas notas. Se propone una práctica análoga con los mismos pasos.

Escribe una fórmula para la función polinómica que tiene interceptos en $x = -1$ y $x = 4$ (pasando linealmente por ambos) y en $x = 3$ (rebotando), y cuyo intercepto $y$ está en $(0, 6)$.

<details>
<summary>Ver respuesta</summary>

Los interceptos dan los factores $x + 1$, $x - 3$ y $x - 4$, con multiplicidad 2 en $x = 3$:

$$f(x) = a(x + 1)(x - 3)^2(x - 4)$$

Usamos el intercepto $y$ para hallar $a$:

$$f(0) = a(1)(9)(-4) = -36a = 6 \implies a = -\frac{1}{6}$$

La fórmula es:

$$f(x) = -\frac{1}{6}(x + 1)(x - 3)^2(x - 4)$$
</details>
