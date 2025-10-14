# Guía Detallada sobre Variables en Python

## 1. ¿Qué es una Variable?

Imagina una variable como una **caja con una etiqueta**. Dentro de esa caja, guardas un dato. La etiqueta es el **nombre de la variable** y te permite acceder al dato cuando lo necesites.

Técnicamente, una variable es un nombre simbólico que actúa como una referencia a un objeto que vive en la memoria del ordenador.

### Relevancia en Ciberseguridad

En ciberseguridad, las variables son omnipresentes para almacenar información dinámica durante el análisis o la ejecución de un script:

-   `ip_address = "192.168.1.100"` (Para almacenar una IP a analizar)
-   `login_attempts = 3` (Para contar intentos de acceso)
-   `file_hash = "a1b2c3d4..."` (Para guardar el hash de un archivo sospechoso)
-   `is_vulnerable = True` (Para registrar el estado de un sistema)

## 2. Asignación y Tipado Dinámico

En Python, una variable se crea en el momento en que le asignas un valor con el operador (`=`). No necesitas declarar su tipo de antemano. Python es un lenguaje de **tipado dinámico**, lo que significa que infiere el tipo de dato automáticamente.

```python
port = 443              # Python sabe que es un entero (int)
protocol = "HTTPS"      # Python sabe que es una cadena (str)
is_encrypted = True     # Python sabe que es un booleano (bool)
```

Puedes incluso cambiar el tipo de dato de una variable reasignándole un valor diferente.

## 3. Reglas y Convenciones para Nombrar Variables (PEP 8)

#### Reglas (Obligatorias)

1.  Solo puede contener letras (a-z, A-Z), números (0-9) y guiones bajos (`_`).
2.  No puede empezar con un número.
3.  No puede ser una [palabra reservada de Python](https://docs.python.org/es/3/reference/lexical_analysis.html#keywords) (como `if`, `for`, `while`).

#### Convenciones (Buenas Prácticas Esenciales)

1.  **`snake_case`**: Los nombres de variables deben estar en minúsculas, con palabras separadas por guiones bajos. Esto es crucial para la legibilidad.
2.  **Nombres Descriptivos**: El nombre debe describir el dato. Durante un incidente de seguridad, no hay tiempo para descifrar qué significa `x` o `tmp`.
3.  **Sensibilidad a Mayúsculas**: `user`, `User` y `USER` son tres variables distintas.
4.  **Constantes**: Si un valor no debe cambiar (como un número máximo de intentos), la convención es escribir el nombre de la variable en mayúsculas.

```python
# MAL 👎 (difícil de leer y entender)
x = "8.8.8.8"
n = 3

# BIEN 👍 (claro y descriptivo)
target_ip = "8.8.8.8"
max_retries = 3
```

## 4. Asignación Múltiple

Puedes asignar valores a varias variables en una sola línea:

```python
# Asignar diferentes valores
ip, port = "127.0.0.1", 8080

# Asignar el mismo valor
# Útil para inicializar contadores
successful_connections = failed_connections = 0
```

## Puntos Clave para un Analista de Seguridad

-   **Claridad ante todo**: Usa nombres descriptivos. Tu código puede ser revisado por otros en una situación de emergencia.
-   **Consistencia**: Sigue la convención `snake_case` para mantener el código limpio.
-   **Usa Constantes**: Para valores fijos (IPs de servidores DNS, umbrales, etc.), usa mayúsculas para indicar que no deben ser modificados.
