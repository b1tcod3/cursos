# Ejemplo 3 de integración: Regla de Simpson 3/8
===============================================

Aproximar la misma integral de referencia, ahora con la regla cúbica:

$$I = \int_0^1 e^{-x^2}\,dx \qquad \text{(valor exacto: } I = 0.7468241328\text{)}$$

La regla 3/8 interpola un cubo por **cuatro** puntos equiespaciados: usamos $n = 3$ subintervalos con paso $h = \frac{b-a}{n} = \frac{1}{3}$.

| $i$ | $x_i$ | $f(x_i) = e^{-x^2}$ | Peso |
|---|------|------------|------|
| 0 | $0$     | $1.0000000000$ | 1 |
| 1 | $1/3$   | $0.8948393168$ | 3 |
| 2 | $2/3$   | $0.6411803884$ | 3 |
| 3 | $1$     | $0.3678794412$ | 1 |

## Aplicación de la fórmula

La fórmula simple con su factor característico $\frac{3h}{8}$:

$$S_{3/8} = \frac{3h}{8}\Big[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)\Big]$$

Como $3h = 3\cdot\frac{1}{3} = 1$, el factor exterior se simplifica a $\frac{1}{8}$:

$$S_{3/8} = \frac{1}{8}\Big[1 + 3(0.8948393168) + 3(0.6411803884) + 0.3678794412\Big]$$

Calculamos los productos:

- $3f(x_1) = 2.6845179504$
- $3f(x_2) = 1.9235411652$

Sumamos:

$$S_{3/8} = \frac{1}{8}\Big[1 + 2.6845179504 + 1.9235411652 + 0.3678794412\Big] = \frac{1}{8} \times 5.9759385568$$

$$\boxed{S_{3/8} = 0.7469923196}$$

## Análisis: precisión y papel de la regla

$$|I - S_{3/8}| = |0.7468241328 - 0.7469923196| \approx 1.68\times10^{-4}$$

| Método | Evaluaciones | Resultado | Error absoluto |
|---|---|---|---|
| Simpson 3/8 simple ($n=3$) | 4 | 0.7469923196 | $1.68\times10^{-4}$ |
| Simpson 1/3 compuesta ($n=4$) | 5 | 0.7468553798 | $3.12\times10^{-5}$ |

Con una evaluación menos, Simpson 3/8 queda detrás de Simpson 1/3: su constante de error es ocho veces mayor ($\frac{1}{80}$ contra $\frac{1}{180}$ en términos de $(b-a)^5 f^{(4)}(\xi)$). Su valor no está en competir sola, sino como **pieza de empalme**: cuando el número de subintervalos no es par (por ejemplo $n=5$: un tramo 3/8 + dos tramos 1/3), permite cerrar la partición sin desperdiciar nodos.
