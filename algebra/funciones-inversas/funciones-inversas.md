# Funciones inversas y funciones radicales

Una función que no sea inyectiva (uno-a-uno) no tiene inversa. Al **restringir el dominio** de una función para que sea inyectiva, creamos una nueva función que sí tiene inversa.

## Restringir el dominio

**Definición (uno-a-uno).** Una función es uno-a-uno si cada valor de salida ($y$) corresponde exactamente a un valor de entrada ($x$). Gráficamente, ninguna recta horizontal corta la gráfica más de una vez.

Las funciones cuadráticas no son uno-a-uno en todo su dominio, por lo que se restringe su dominio a un lado del vértice (donde la función es creciente o decreciente).

### Algoritmo: restringir el dominio y encontrar la inversa

Dada una función polinomial que no es uno-a-uno:

1. **Restringir el dominio** determinando un dominio sobre el cual la función original sea uno-a-uno.
2. Reemplazar $f(x)$ por $y$.
3. Intercambiar $x$ y $y$.
4. Despejar $y$ y renombrar como $f^{-1}(x)$.
5. **Revisar la fórmula** de $f^{-1}(x)$: las salidas de la inversa deben corresponder al dominio restringido de la función original (elegir el signo $+$ o $-$ adecuado).

**Nota sobre los roles de $x$ y $y$.** Al intercambiar roles, el dominio de la función original se convierte en el rango de la inversa. Por eso, si la original se restringió a $x \geq a$, la inversa debe cumplir $f^{-1}(x) \geq a$.

## Inversa de una función cuadrática

Si la cuadrática no está en forma de vértice, primero se reescribe en esa forma para leer las coordenadas del vértice y decidir la restricción. Luego se aplica el algoritmo anterior.

## Inversa de una función radical

Las funciones inversas de polinomios suelen ser funciones radicales. Y al revés: si queremos la inversa de una función radical, el **dominio de la respuesta se restringe al rango de la función original**, porque el rango de la original es limitado.

### Algoritmo: inversa de una función radical

1. Determinar el **rango de la función original**.
2. Reemplazar $f(x)$ por $y$ y despejar $x$.
3. Si es necesario, restringir el dominio de la inversa al rango de la función original.

## Funciones inversas en aplicaciones

En problemas del mundo real **no se intercambian las variables**; en lugar de ello, se cambia cuál variable se considera independiente. Por ejemplo, si $V = f(r)$, se despeja $r$ en términos de $V$ directamente.

## Dominio de una función radical compuesta con otras

Una raíz cuadrada solo está definida cuando la cantidad bajo el radical es no negativa. Cuando hay una función racional dentro del radical, se debe resolver $\frac{\text{numerador}}{\text{denominador}} \geq 0$. El signo de una función racional puede cambiar en los interceptos $x$ y en las asíntotas verticales.

Para hallar el dominio: se ubican los puntos críticos (interceptos $x$ y asíntotas verticales), se determinan los intervalos y se prueban valores en cada uno.

## Inversa de una función racional

Es útil cuando la función racional es cociente de funciones lineales (por ejemplo, en problemas de concentraciones). Se despeja la variable independiente en términos de la dependiente, usando el mismo método algebraico.

## Ejemplos

- [[ejemplos/ejemplo-1]] — Restringir el dominio: $f(x) = (x-4)^2$ con $x \geq 4$ o $x \leq 4$
- [[ejemplos/ejemplo-2]] — Inversa de una cuadrática sin restricción especificada: $f(x) = (x-2)^2 - 3$
- [[ejemplos/ejemplo-3]] — Inversa de una función radical: $f(x) = \sqrt{x-4}$
- [[ejemplos/ejemplo-4]] — Aplicación con una función cúbica (volumen de un cono)
- [[ejemplos/ejemplo-5]] — Dominio de una función radical compuesta: $f(x) = \sqrt{\frac{(x+2)(x-3)}{x-1}}$
- [[ejemplos/ejemplo-6]] — Inversa de una función racional (concentración de ácido)

## Ejercicios

- [[ejercicios/ejercicio-1]] — Inversa de $f(x) = x^2 + 1$ con $x \geq 0$
- [[ejercicios/ejercicio-2]] — Inversa de $f(x) = \sqrt{2x + 3}$
- [[ejercicios/ejercicio-3]] — Inversa de $f(x) = \frac{x+3}{x-2}$
