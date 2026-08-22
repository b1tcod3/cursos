# Ejemplo 1 de integración: Regla del Trapecio
==============================================

Aproximar la integral sin primitiva elemental:

$$I = \int_0^1 e^{-x^2}\,dx \qquad \text{(valor exacto: } I = 0.7468241328\text{)}$$

Evaluamos la función en los nodos que necesitaremos ($h = 0.25$):

| $x$ | $f(x) = e^{-x^2}$ |
|------|------------|
| $0$    | $1.0000000000$ |
| $0.25$ | $0.9394130628$ |
| $0.50$ | $0.7788007831$ |
| $0.75$ | $0.5697828247$ |
| $1$    | $0.3678794412$ |

## Trapecio simple

Con un único trapecio sobre todo el intervalo, $a = 0$, $b = 1$:

$$T(a,b) = \frac{b-a}{2}\big[f(a) + f(b)\big] = \frac{1}{2}\big[1 + 0.3678794412\big] = \frac{1.3678794412}{2}$$

$$T(a,b) = 0.6839397206$$

El error es enorme:

$$|I - T| = |0.7468241328 - 0.6839397206| \approx 6.29\times10^{-2}$$

La recta no puede seguir la curvatura de la gaussiana: recorta sistemáticamente el área.

## Trapecio compuesto ($n = 4$)

Partimos el intervalo en $n = 4$ subintervalos de ancho $h = \frac{b-a}{n} = 0.25$ y aplicamos la fórmula compuesta:

$$T_4 = \frac{h}{2}\Big[f(x_0) + 2f(x_1) + 2f(x_2) + 2f(x_3) + f(x_4)\Big]$$

Sustituimos los valores (los nodos interiores pesan doble):

$$T_4 = \frac{0.25}{2}\Big[1 + 2(0.9394130628) + 2(0.7788007831) + 2(0.5697828247) + 0.3678794412\Big]$$

Calculamos cada producto:

$$T_4 = 0.125\,\Big[1 + 1.8788261256 + 1.5576015662 + 1.1395656494 + 0.3678794412\Big]$$

Sumamos el contenido del corchete:

$$T_4 = 0.125 \times 5.9438727824$$

$$\boxed{T_4 = 0.7429840978}$$

## Comparación y lectura del error

$$|I - T_4| = |0.7468241328 - 0.7429840978| \approx 3.84\times10^{-3}$$

| Método | Evaluaciones | Resultado | Error absoluto |
|---|---|---|---|
| Trapecio simple | 2 | 0.6839397206 | $6.29\times10^{-2}$ |
| Trapecio compuesto $n=4$ | 5 | 0.7429840978 | $3.84\times10^{-3}$ |

Refinar la malla redujo el error **16 veces** con solo tres evaluaciones nuevas — coherente con el orden global $O(h^2)$: al pasar de $h=1$ a $h=0.25$ (factor 4), el error teórico cae $\approx 4^2 = 16$ veces.
