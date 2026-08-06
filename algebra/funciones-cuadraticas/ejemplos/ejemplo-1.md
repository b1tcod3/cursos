# Ejemplo 1: Encontrar el máximo ingreso

El precio unitario de un artículo afecta su oferta y demanda. Un periódico local tiene actualmente 84 000 suscriptores con una tarifa trimestral de \$30. La investigación de mercado sugiere que si los dueños suben el precio a \$32, perderían 5 000 suscriptores. Suponiendo que las suscripciones están linealmente relacionadas con el precio, ¿qué precio debería cobrar el periódico por una suscripción trimestral para **maximizar su ingreso**?

## Solución

### Paso 1: Escribir una ecuación cuadrática para la función de ingreso

El ingreso se calcula multiplicando el precio por suscripción por el número de suscriptores (cantidad):

$$Ingreso = pQ$$

Buscamos la relación lineal entre $p$ y $Q$. Con los puntos $(30, 84\,000)$ y $(32, 79\,000)$:

$$m = \frac{79\,000 - 84\,000}{32 - 30} = \frac{-5\,000}{2} = -2\,500$$

Se pierden 2 500 suscriptores por cada dólar de aumento. Resolvemos para el intercepto $b$:

$$84\,000 = -2\,500(30) + b \implies b = 159\,000$$

La relación lineal es $Q = -2\,500p + 159\,000$. Sustituimos en el ingreso:

$$Ingreso = pQ = p(-2\,500p + 159\,000) = -2\,500p^2 + 159\,000p$$

### Paso 2: Encontrar el vértice

$$h = -\frac{159\,000}{2(-2\,500)} = 31.8$$

### Paso 3: Determinar el valor de $y$ del vértice

$$Ingreso_{máx} = -2\,500(31.8)^2 + 159\,000(31.8) = 2\,528\,100$$

### Respuesta

El periódico debería cobrar **\$31.80** por suscripción para maximizar su ingreso, obteniendo **\$2 528 100**.
