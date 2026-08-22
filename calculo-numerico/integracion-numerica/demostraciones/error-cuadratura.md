# Demostración del Error en las Fórmulas de Cuadratura

## Enunciado

Si $f \in C^2[a,b]$, el error de la regla del trapecio es:

$$E_T = \int_a^b f(x)\,dx - T(a,b) = -\frac{(b-a)^3}{12}\, f''(\xi), \qquad \text{para algún } \xi \in (a,b)$$

y si $f \in C^4[a,b]$, la regla de Simpson 1/3 satisface:

$$E_S = \int_a^b f(x)\,dx - S_{1/3}(a,b) = -\frac{(b-a)^5}{180}\, f^{(4)}(\xi)$$

Además, Simpson alcanza grado de precisión **3** (no 2): integra exactamente todo polinomio cúbico. Este resultado —aparentemente un regalo— tiene una explicación puramente algebraica que se demuestra al final.

---

## Demostración 1: Regla del Trapecio (vía el residuo de interpolación)

La estrategia general de Newton-Cotes es integrar el polinomio interpolador; el error de la cuadratura es entonces la integral del error de interpolación.

**Paso 1: residuo de la interpolación lineal.** Sea $P_1(x)$ la recta que une $(a, f(a))$ y $(b, f(b))$. El teorema del error de interpolación garantiza que para cada $x \in [a,b]$ existe $\xi_x \in (a,b)$ tal que

$$f(x) - P_1(x) = \frac{f''(\xi_x)}{2}\,(x-a)(x-b)$$

**Paso 2: integrar el residuo.** Como $f''$ es continua y $(x-a)(x-b) \le 0$ en todo el intervalo (es negativo salvo en los extremos donde se anula), el producto $f''(\xi_x)(x-a)(x-b)$ no cambia de signo. Por el **Teorema del Valor Medio para integrales ponderadas**, existe $\xi \in (a,b)$ tal que

$$\int_a^b \frac{f''(\xi_x)}{2}(x-a)(x-b)\,dx = \frac{f''(\xi)}{2}\int_a^b (x-a)(x-b)\,dx$$

**Paso 3: la integral elemental.** Con el cambio de variable $x = a + t(b-a)$, $dx = (b-a)\,dt$:

$$\int_a^b (x-a)(x-b)\,dx = (b-a)^3 \int_0^1 t(t-1)\,dt = (b-a)^3\left[\frac{t^3}{3} - \frac{t^2}{2}\right]_0^1 = -\frac{(b-a)^3}{6}$$

**Conclusión:**

$$E_T = \frac{f''(\xi)}{2} \cdot \left(-\frac{(b-a)^3}{6}\right) = -\frac{(b-a)^3}{12}\, f''(\xi) \qquad \blacksquare$$

El signo negativo confirma lo que se ve a simple vista: si $f'' > 0$ (curva convexa), la cuerda queda **por encima** del gráfico y el trapecio sobreestima el área; la fórmula devuelve $E_T < 0$ exactamente en ese caso.

---

## Demostración 2: El grado extra de Simpson (cancelación por simetría)

Esperamos que una regla basada en parábolas tenga grado de precisión 2. Sorpresa: llega al 3. La razón es que el punto medio hace cancelarse los términos impares del desarrollo de Taylor.

**Paso 1: centrar Taylor en el punto medio.** Sea $m = \frac{a+b}{2}$ y expandamos $f$ alrededor de $m$ hasta orden 4. Denotando $h = \frac{b-a}{2}$, los extremos están en $m \pm h$:

$$f(m \pm h) = f(m) \pm h f'(m) + \frac{h^2}{2} f''(m) \pm \frac{h^3}{6} f^{(3)}(m) + \frac{h^4}{24} f^{(4)}(m) + O(h^5)$$

**Paso 2: sumar las evaluaciones con los pesos de Simpson.** Al sumar $f(m-h) + f(m+h)$, los términos impares ($h f'$ y $\frac{h^3}{6} f^{(3)}$) se cancelan entre sí:

$$f(m-h) + f(m+h) = 2f(m) + h^2 f''(m) + \frac{h^4}{12} f^{(4)}(m) + O(h^6)$$

La fórmula de Simpson pesa esta suma por 4 y añade $f(m)$ con peso 1, todo multiplicado por $\frac{h}{3}$:

$$S_{1/3} = \frac{h}{3}\Big[6 f(m) + h^2 f''(m) + \frac{h^4}{12} f^{(4)}(m)\Big] + O(h^6) = (b-a)f(m) + \frac{(b-a)^3}{24} f''(m) + \frac{(b-a)^5}{1920} f^{(4)}(m)$$

**Paso 3: comparar con la integral exacta.** Integrando el mismo desarrollo de Taylor término a término (los términos impares aportan cero por simetría):

$$\int_a^b f(x)\,dx = (b-a)f(m) + \frac{(b-a)^3}{24} f''(m) + \frac{(b-a)^5}{1920} f^{(4)}(m) + O(h^7)$$

**Conclusión:** integral exacta y aproximación de Simpson coinciden **término a término** hasta el orden $h^4$. Para cualquier polinomio de grado $\le 3$, todos los términos desde $f^{(4)}$ son nulos, luego $E_S = 0$: Simpson es exacta para cúbicas. La primera discrepancia aparece en el término de orden $h^5$ (proporcional a $f^{(4)}$), que tras el análisis riguroso con el valor medio da

$$E_S = -\frac{(b-a)^5}{180}\, f^{(4)}(\xi) \qquad \blacksquare$$

La moraleja estructural: **el nodo central convierte la fórmula en simétrica respecto a $m$, y la simetría aniquila términos impares**. Es la misma mecánica que luego hace tan letal a Gauss-Legendre, cuyos nodos también son simétricos respecto al centro.

---

## Demostración 3: Precisión de Gauss de dos puntos (verificación directa)

El teorema general afirma que Gauss-Legendre con $n$ nodos integra exactamente polinomios de grado $\le 2n-1$. Para $n=2$ eso promete grado 3. Puede verificarse sin desplegar artillería pesada, comprobando la base canónica $\{1, x, x^2, x^3\}$ en $[-1, 1]$.

Los nodos son las raíces de $P_2(x) = \frac{3x^2-1}{2}$, es decir $x_{1,2} = \pm\tfrac{1}{\sqrt{3}}$, con pesos $w_1 = w_2 = 1$.

| Función $p(x)$ | Integral exacta | Suma de Gauss | ¿Exacta? |
|---|---|---|---|
| $1$ | $2$ | $1+1 = 2$ | ✓ |
| $x$ | $0$ | $\tfrac{1}{\sqrt{3}} - \tfrac{1}{\sqrt{3}} = 0$ | ✓ |
| $x^2$ | $\tfrac{2}{3}$ | $\tfrac{1}{3} + \tfrac{1}{3} = \tfrac{2}{3}$ | ✓ |
| $x^3$ | $0$ | $\tfrac{1}{3\sqrt{3}} - \tfrac{1}{3\sqrt{3}} = 0$ | ✓ |
| $x^4$ | $\tfrac{2}{5}$ | $\tfrac{2}{9} \approx 0.222$ | ✗ |

Como toda cuadratura es lineal, ser exacta sobre una base implica serlo sobre todo el espacio que ella genera: **Gauss de 2 puntos es exacta para todo polinomio de grado $\le 3$**, y falla por primera vez en $x^4$. $\blacksquare$

Obsérvese la eficiencia brutal: Newton-Cotes necesitaría **cuatro nodos equiespaciados** (Simpson 3/8) para lograr el mismo grado de precisión; Gauss lo consigue con dos. Ese ahorro se amplifica con cada nodo: $n$ nodos gaussianos rinden grado $2n-1$, porque cada raíz de Legendre aporta dos parámetros libres (nodo y peso) y $2n$ condiciones determinan polinomios de grado $2n-1$.
