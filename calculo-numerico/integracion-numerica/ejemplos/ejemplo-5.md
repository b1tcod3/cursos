# Ejemplo 5 de integración: Cuadratura Gauss-Legendre
====================================================

Aproximar por última vez la integral de referencia, con el método óptimo:

$$I = \int_0^1 e^{-x^2}\,dx \qquad \text{(valor exacto: } I = 0.7468241328\text{)}$$

## Cambio de variable al intervalo canónico

Los nodos y pesos tabulados de Gauss-Legendre viven en $[-1, 1]$. Para llevarlos a $[a, b] = [0, 1]$ usamos:

$$x = \frac{a+b}{2} + \frac{b-a}{2}\,t = \frac{1}{2} + \frac{1}{2}t, \qquad dx = \frac{1}{2}\,dt$$

$$I = \int_0^1 e^{-x^2}\,dx = \frac{1}{2}\int_{-1}^{1} e^{-\left(\frac{1+t}{2}\right)^2}\,dt$$

## Gauss con dos puntos ($n = 2$)

Nodos: las raíces de $P_2(x) = \frac{3x^2-1}{2}$, es decir $t_{1,2} = \pm\frac{1}{\sqrt{3}} = \pm0.5773502692$, ambos con peso $w = 1$.

Mapeamos al intervalo real y evaluamos:

| $t_i$ | $x_i = \frac{1}{2} + \frac{t_i}{2}$ | $f(x_i) = e^{-x_i^2}$ | $w_i$ |
|---|---|---|---|
| $-0.5773502692$ | $0.2113248654$ | $0.9563242988$ | $1$ |
| $+0.5773502692$ | $0.7886751346$ | $0.5368650777$ | $1$ |

$$G_2 = \frac{1}{2}\Big[(1)(0.9563242988) + (1)(0.5368650777)\Big] = \frac{1.4931893765}{2}$$

$$\boxed{G_2 = 0.7465946883}$$

Error: $|I - G_2| \approx 2.29\times10^{-4}$ — **con solo dos evaluaciones**. Comparen: el trapecio simple, también dos evaluaciones, cometió $6.29\times10^{-2}$. Doscientas setenta veces peor.

## Gauss con tres puntos ($n = 3$)

Nodos: raíces de $P_3(x) = \frac{5x^3-3x}{2}$: $t = 0,\ \pm\sqrt{\tfrac{3}{5}} = \pm0.7745966692$. Pesos: $\frac{8}{9},\ \frac{5}{9},\ \frac{5}{9}$.

| $t_i$ | $x_i$ | $f(x_i)$ | $w_i$ |
|---|---|---|---|
| $-0.7745966692$ | $0.1127016654$ | $0.9873786603$ | $\frac{5}{9}$ |
| $0$ | $0.5000000000$ | $0.7788007831$ | $\frac{8}{9}$ |
| $+0.7745966692$ | $0.8872983346$ | $0.4550725899$ | $\frac{5}{9}$ |

$$G_3 = \frac{1}{2}\Big[\frac{5}{9}(0.9873786603) + \frac{8}{9}(0.7788007831) + \frac{5}{9}(0.4550725899)\Big]$$

Calculamos cada producto:

- $\frac{5}{9}(0.9873786603) = 0.5485437002$
- $\frac{8}{9}(0.7788007831) = 0.6922673628$
- $\frac{5}{9}(0.4550725899) = 0.2528181055$

Sumamos y multiplicamos por el factor del cambio de variable:

$$G_3 = \frac{1}{2}\Big[0.5485437002 + 0.6922673628 + 0.2528181055\Big] = \frac{1.4936291685}{2}$$

$$\boxed{G_3 = 0.7468145842}$$

## Lectura del resultado

$$|I - G_3| = |0.7468241328 - 0.7468145842| \approx 9.55\times10^{-6}$$

Comparativa final de la campaña completa sobre esta integral:

| Método | Evaluaciones | Resultado | Error absoluto |
|---|---|---|---|
| Trapecio compuesto ($n=4$) | 5 | 0.7429840978 | $3.84\times10^{-3}$ |
| Simpson 1/3 compuesta ($n=4$) | 5 | 0.7468553798 | $3.12\times10^{-5}$ |
| Simpson 3/8 simple ($n=3$) | 4 | 0.7469923196 | $1.68\times10^{-4}$ |
| Romberg $R_{3,3}$ | 9 | 0.7468240185 | $1.14\times10^{-7}$ |
| **Gauss-Legendre ($n=3$)** | **3** | 0.7468145842 | $9.55\times10^{-6}$ |

Gauss consigue con **tres** evaluaciones lo que a Simpson le toma cinco y al trapecio cientos. La razón es estructural, no suerte: sus nodos no están donde manda la costumbre equiespaciada, sino donde los polinomios de Legendre dictan que la información de $f$ rinde al máximo — grado de precisión $2n - 1 = 5$ con solo tres puntos.
