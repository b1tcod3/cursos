# Ejemplo de Splines Cúbicos (Spline Natural)

Construcción de un Spline Natural para tres puntos dados.

## Datos

| x_i | f(x_i) |
|-----|--------|
| 0   | 1      |
| 1   | 2      |
| 2   | 0      |

Tenemos $n=2$ intervalos: $[0, 1]$ y $[1, 2]$.

## Cálculo del sistema tridiagonal

Por ser un Spline Natural, $c_0 = 0$ y $c_2 = 0$.

Para el nodo interior $c_1$, la ecuación del sistema es:

$$h_0 c_0 + 2(h_0 + h_1)c_1 + h_1 c_2 = 3\left( \frac{a_2 - a_1}{h_1} - \frac{a_1 - a_0}{h_0} \right)$$

Sustituyendo los valores ($h_0 = 1$, $h_1 = 1$, $a_0 = 1$, $a_1 = 2$, $a_2 = 0$):

$$1(0) + 2(1 + 1)c_1 + 1(0) = 3\left( \frac{0 - 2}{1} - \frac{2 - 1}{1} \right)$$

$$4c_1 = 3(-2 - 1)$$

$$4c_1 = -9 \quad \implies \quad c_1 = -2.25$$

## Coeficientes del Tramo 1 ($S_0$ en $[0, 1]$)

- $a_0 = f(0) = 1$
- $c_0 = 0$

$$b_0 = \frac{f(x_1) - f(x_0)}{h_0} - \frac{h_0(2c_0 + c_1)}{3} = \frac{2 - 1}{1} - \frac{1(0 - 2.25)}{3} = 1 - (-0.75) = 1.75$$

$$d_0 = \frac{c_1 - c_0}{3h_0} = \frac{-2.25 - 0}{3(1)} = -0.75$$

$$S_0(x) = 1 + 1.75x - 0.75x^3$$

## Coeficientes del Tramo 2 ($S_1$ en $[1, 2]$)

- $a_1 = f(1) = 2$
- $c_1 = -2.25$

$$b_1 = \frac{f(x_2) - f(x_1)}{h_1} - \frac{h_1(2c_1 + c_2)}{3} = \frac{0 - 2}{1} - \frac{1(-4.5 + 0)}{3} = -2 - (-1.5) = -0.5$$

$$d_1 = \frac{c_2 - c_1}{3h_1} = \frac{0 - (-2.25)}{3(1)} = 0.75$$

$$S_1(x) = 2 - 0.5(x - 1) - 2.25(x - 1)^2 + 0.75(x - 1)^3$$

## Función polinómica resultante a trozos

$$S(x) = 
\begin{cases} 
1 + 1.75x - 0.75x^3 & \text{si } x \in [0, 1] \\[0.3cm]
2 - 0.5(x - 1) - 2.25(x - 1)^2 + 0.75(x - 1)^3 & \text{si } x \in [1, 2] 
\end{cases}$$

Este conjunto de ecuaciones describe una curva perfectamente suave que interpola los puntos dados, evitando las oscilaciones abruptas.
