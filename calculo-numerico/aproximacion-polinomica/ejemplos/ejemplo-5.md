# Ejemplo de Nodos de Chebyshev

Cálculo de la mejor ubicación para 3 nodos (polinomio de grado $n=2$) en el intervalo $[-1, 1]$.

## Datos

- Grado del polinomio: $n = 2$
- Número de nodos: $n + 1 = 3$
- Intervalo: $[a, b] = [-1, 1]$

## Cálculo de los nodos

Se aplica la fórmula $x_k = \cos\left( \frac{2k + 1}{2(n+1)} \pi \right)$ para $k = 0, 1, 2$:

- $k = 0$: $x_0 = \cos\left( \frac{2(0) + 1}{2(3)} \pi \right) = \cos\left( \frac{\pi}{6} \right) = \frac{\sqrt{3}}{2} \approx 0.8660$

- $k = 1$: $x_1 = \cos\left( \frac{2(1) + 1}{2(3)} \pi \right) = \cos\left( \frac{\pi}{2} \right) = 0$

- $k = 2$: $x_2 = \cos\left( \frac{2(2) + 1}{2(3)} \pi \right) = \cos\left( \frac{5\pi}{6} \right) = -\frac{\sqrt{3}}{2} \approx -0.8660$

## Tabla de nodos

| $k$ | Ángulo $\theta_k$ | Nodo $x_k$ (exacto) | Nodo $x_k$ (decimal) |
|-----|-------------------|---------------------|----------------------|
| 0   | $\pi/6$           | $\frac{\sqrt{3}}{2}$ | 0.8660              |
| 1   | $\pi/2$           | $0$                  | 0.0000              |
| 2   | $5\pi/6$          | $-\frac{\sqrt{3}}{2}$ | -0.8660            |

## Uso en la interpolación

Una vez obtenidos los nodos $x_k$ (o sus equivalentes mapeados $t_k$ para otro intervalo), **no se usa una "fórmula de Chebyshev"** para construir el polinomio. Los nodos se ingresan a los métodos clásicos — Lagrange o Newton — junto con sus evaluaciones $f(x_k)$ para generar el polinomio interpolador. La ventaja está únicamente en la elección de las coordenadas $x$.
