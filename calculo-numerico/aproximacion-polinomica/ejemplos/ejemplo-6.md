# Ejemplo de Interpolación Segmentaria Lineal

Construcción de una interpolación lineal a trozos para tres puntos dados.

## Datos

| x_i | f(x_i) |
|-----|--------|
| 0   | 1      |
| 2   | 5      |
| 4   | 3      |

Tenemos $n=2$ intervalos: $[0, 2]$ y $[2, 4]$.

## Tramo 1 ($P_0$ en $[0, 2]$)

Aplicamos la fórmula de la recta punto-pendiente para $i=0$:

$$P_0(x) = 1 + \frac{5 - 1}{2 - 0}(x - 0)$$

$$P_0(x) = 1 + 2x$$

## Tramo 2 ($P_1$ en $[2, 4]$)

Para $i=1$:

$$P_1(x) = 5 + \frac{3 - 5}{4 - 2}(x - 2)$$

$$P_1(x) = 5 - 1(x - 2)$$

$$P_1(x) = 7 - x$$

## Función polinómica a trozos resultante

$$P(x) = 
\begin{cases} 
1 + 2x & \text{si } x \in [0, 2] \\[0.3cm]
7 - x & \text{si } x \in [2, 4] 
\end{cases}$$

Esta función conecta exactamente los puntos dados mediante líneas rectas continuas, demostrando el principio básico sobre el cual se construyen los métodos de splines de mayor grado.
