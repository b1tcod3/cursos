# Ejemplo 2 de integración: Regla de Simpson 1/3
===============================================

Aproximar la misma integral de referencia:

$$I = \int_0^1 e^{-x^2}\,dx \qquad \text{(valor exacto: } I = 0.7468241328\text{)}$$

Usamos $n = 4$ subintervalos (Simpson 1/3 exige un número **par**), con paso $h = 0.25$. Los valores de la función son los mismos del [Ejemplo 1](./ejemplo-1.md):

| $i$ | $x_i$ | $f(x_i) = e^{-x^2}$ | Peso |
|---|------|------------|------|
| 0 | $0$    | $1.0000000000$ | 1 |
| 1 | $0.25$ | $0.9394130628$ | 4 |
| 2 | $0.50$ | $0.7788007831$ | 2 |
| 3 | $0.75$ | $0.5697828247$ | 4 |
| 4 | $1$    | $0.3678794412$ | 1 |

## Aplicación de la fórmula

La regla compuesta con pesos alternantes 1-4-2-4-1:

$$S_4 = \frac{h}{3}\Big[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + f(x_4)\Big]$$

Sustituimos:

$$S_4 = \frac{0.25}{3}\Big[1 + 4(0.9394130628) + 2(0.7788007831) + 4(0.5697828247) + 0.3678794412\Big]$$

Calculamos cada producto:

- $4f(x_1) = 3.7576522512$
- $2f(x_2) = 1.5576015662$
- $4f(x_3) = 2.2791312988$

Sumamos el contenido del corchete:

$$S_4 = \frac{0.25}{3}\Big[1 + 3.7576522512 + 1.5576015662 + 2.2791312988 + 0.3678794412\Big] = \frac{0.25}{3} \times 8.9622645574$$

$$\boxed{S_4 = 0.7468553798}$$

## Comparación con el trapecio (mismas evaluaciones)

$$|I - S_4| = |0.7468241328 - 0.7468553798| \approx 3.12\times10^{-5}$$

| Método ($n=4$) | Resultado | Error absoluto |
|---|---|---|
| Trapecio compuesto | 0.7429840978 | $3.84\times10^{-3}$ |
| Simpson 1/3 compuesta | 0.7468553798 | $3.12\times10^{-5}$ |

Con **exactamente las mismas cinco evaluaciones** de la función, Simpson reduce el error en más de dos órdenes de magnitud. Esa es la recompensa del grado extra: interpolar parábolas en lugar de rectas no cuesta ni una evaluación adicional.
