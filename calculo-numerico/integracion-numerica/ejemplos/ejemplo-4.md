# Ejemplo 4 de integración: Extrapolación de Romberg
===================================================

Aproximar la misma integral de referencia, ahora acelerando el trapecio:

$$I = \int_0^1 e^{-x^2}\,dx \qquad \text{(valor exacto: } I = 0.7468241328\text{)}$$

## Columna 0: trapecios cada vez más finos

La primera columna son trapecios compuestos con $2^i$ subintervalos. Cada fila **recicla** las evaluaciones de la fila anterior: solo los nodos impares nuevos se calculan.

- $R_{0,0}$: un solo trapecio, $h=1$: $\;\frac{1}{2}[f(0)+f(1)] = \frac{1}{2}[1 + 0.3678794412] = 0.6839397206$
- $R_{1,0}$: $h=0.5$, nodo nuevo $f(0.5) = 0.7788007831$:
  $\;R_{1,0} = \frac{R_{0,0}}{2} + h\cdot f(0.5) = 0.3419698603 + 0.3894003916 = 0.7313702518$
- $R_{2,0}$: $h=0.25$, nodos nuevos $f(0.25)$ y $f(0.75)$:
  $\;R_{2,0} = \frac{R_{1,0}}{2} + 0.25\,(0.9394130628 + 0.5697828247) = 0.7429840978$
- $R_{3,0}$: $h=0.125$, nodos nuevos $f(0.125), f(0.375), f(0.625), f(0.875)$:
  $\;R_{3,0} = \frac{R_{2,0}}{2} + 0.125\,(0.9844964370 + 0.8688150563 + 0.6766338462 + 0.4650431881) = 0.7458656148$

## Extrapolación: llenar la tabla

Cada columna aplica la fórmula de Richardson con factor $4^j$:

$$R_{i,j} = \frac{4^{\,j}\, R_{i,j-1} - R_{i-1,j-1}}{4^{\,j}-1}$$

### Primera extrapolación ($j=1$, cancela el término en $h^2$)

$$R_{1,1} = \frac{4\,R_{1,0} - R_{0,0}}{3} = \frac{4(0.7313702518) - 0.6839397206}{3} = \frac{2.2415412866}{3} = 0.7471804289$$

$$R_{2,1} = \frac{4(0.7429840978) - 0.7313702518}{3} = 0.7468553798 \qquad R_{3,1} = \frac{4(0.7458656148) - 0.7429840978}{3} = 0.7468261205$$

Nótese que $R_{2,1}$ reproduce **exactamente** el resultado de Simpson 1/3 del [Ejemplo 2](./ejemplo-2.md): Simpson es Romberg de primera orden.

### Segunda extrapolación ($j=2$, cancela el término en $h^4$)

$$R_{2,2} = \frac{16\,R_{2,1} - R_{1,1}}{15} = \frac{16(0.7468553798) - 0.7471804289}{15} = \frac{11.2025056478}{15} = 0.7468337099$$

$$R_{3,2} = \frac{16(0.7468261205) - 0.7468553798}{15} = 0.7468241699$$

### Tercera extrapolación ($j=3$, cancela el término en $h^6$)

$$R_{3,3} = \frac{64\,R_{3,2} - R_{2,2}}{63} = \frac{64(0.7468241699) - 0.7468337099}{63} = \frac{47.0499131605}{63}$$

$$\boxed{R_{3,3} = 0.7468240185}$$

## Tabla completa

| $i$ | $j=0$ | $j=1$ | $j=2$ | $j=3$ |
|---|---|---|---|---|
| 0 | 0.6839397206 | | | |
| 1 | 0.7313702518 | 0.7471804289 | | |
| 2 | 0.7429840978 | 0.7468553798 | 0.7468337099 | |
| 3 | 0.7458656148 | 0.7468261205 | 0.7468241699 | **0.7468240185** |

## Lectura del resultado

El error final:

$$|I - R_{3,3}| = |0.7468241328 - 0.7468240185| \approx 1.14\times10^{-7}$$

Con las mismas **9 evaluaciones** que consumió la tabla entera, el humilde trapecio simple andaba en $10^{-2}$. Cada paso hacia la derecha ganó aproximadamente dos órdenes de magnitud, tal como promete el orden $O(h^{2j})$ de la columna $j$.

Además, la tabla regala su propio control de calidad sin conocer el valor exacto: la distancia entre diagonales consecutivas estima el error.

$$|R_{3,3} - R_{2,2}| = |0.7468240185 - 0.7468337099| \approx 9.69\times10^{-6}$$

Cuando esta diferencia baje de la tolerancia deseada, el algoritmo puede detenerse solo — así funcionan los integradores adaptativos profesionales.
