# Ejercicio 2: División sintética

Usa división sintética para dividir:

$$3x^4 + 18x^3 - 3x + 40 \quad \text{entre} \quad x + 7$$

<details>
<summary>Ver respuesta</summary>

El divisor es $x + 7$, así que $k = -7$. Nota que no hay término en $x^2$, así que usamos el coeficiente $0$. Con los coeficientes $3$, $18$, $0$, $-3$, $40$:

| Operación | Resultado |
|-----------|-----------|
| Bajar | $3$ |
| $3 \cdot (-7)$ | $-21$ |
| $18 + (-21)$ | $-3$ |
| $-3 \cdot (-7)$ | $21$ |
| $0 + 21$ | $21$ |
| $21 \cdot (-7)$ | $-147$ |
| $-3 + (-147)$ | $-150$ |
| $-150 \cdot (-7)$ | $1050$ |
| $40 + 1050$ | $1090$ (resto) |

$$3x^3 - 3x^2 + 21x - 150 + \frac{1090}{x + 7}$$
</details>
