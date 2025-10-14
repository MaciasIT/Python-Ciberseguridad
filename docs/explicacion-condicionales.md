# Guía Detallada de Sentencias Condicionales en Python

## ¿Qué son las Sentencias Condicionales?

Una sentencia condicional es una estructura que ejecuta un bloque de código solo si se cumple una condición específica. Piensa en ello como una bifurcación en un camino: dependiendo de una señal (la condición), el programa tomará una ruta u otra. Para un analista de seguridad, esto es fundamental para automatizar la toma de decisiones, como "¿Es esta dirección IP maliciosa?" o "¿Ha fallado este intento de login?".

Cuando una condición se cumple, se evalúa como el valor booleano `True`. Si no se cumple, se evalúa como `False`.

### La Estructura: Cabecera y Cuerpo

Toda sentencia condicional consta de dos partes:

1.  **La Cabecera:** Es la primera línea, que contiene la palabra clave (`if`, `elif` o `else`) y la condición a evaluar. **Siempre debe terminar con dos puntos (`:`)**.
    ```python
    # La cabecera completa
    if status_code == 403:
    ```
2.  **El Cuerpo:** Es el bloque de código que se ejecuta si la condición de la cabecera es `True`. En Python, el cuerpo **debe estar indentado** (generalmente con 4 espacios). La indentación es obligatoria y es la forma en que Python sabe qué código pertenece a la condición.
    ```python
    if status_code == 403:
        # Este es el cuerpo, está indentado
        print("Acceso Prohibido (Forbidden).")
        log_critical_event("Intento de acceso a recurso prohibido.")
    ```

---

## Operadores: Las Herramientas para Construir Condiciones

Para que una condición exista, necesitamos operadores que comparen valores y combinen expresiones.

### Operadores de Comparación
Comparan dos valores y devuelven `True` o `False`.

| Operador | Descripción       | Ejemplo (`port=443`, `user_level=5`) |
| :--- | :--- | :--- |
| `==`     | Igual a           | `port == 443` (True)      |
| `!=`     | No igual a        | `port != 80` (True)       |
| `<`      | Menor que         | `user_level < 10` (True)  |
| `>`      | Mayor que         | `port > 1024` (False)     |
| `<=`     | Menor o igual que | `user_level <= 5` (True)  |
| `>=`     | Mayor o igual que | `port >= 443` (True)      |

### Operadores Lógicos
Combinan expresiones booleanas para crear condiciones más complejas.

| Operador | Descripción                               | Ejemplo (`is_admin=False`, `is_editor=True`) |
| :--- | :--- | :--- |
| `and`    | Devuelve `True` si **ambas** son `True`.  | `is_admin and is_editor` (False) |
| `or`     | Devuelve `True` si **alguna** es `True`.  | `is_admin or is_editor` (True)   |
| `not`    | Invierte el valor booleano.               | `not is_admin` (True)            |

### Operadores de Pertenencia
Comprueban si un valor se encuentra dentro de una secuencia (lista, cadena, etc.).

| Operador | Descripción                     | Ejemplo (`ip = "127.0.0.1"`, `blacklist = ["10.0.0.5", "192.168.1.1"]`) |
| :--- | :--- | :--- |
| `in`     | `True` si el valor está presente. | `ip in blacklist` (False) |
| `not in` | `True` si el valor no está.     | `ip not in blacklist` (True) |

---

## Construyendo la Lógica: `if`, `elif` y `else`

### `if`: El Punto de Partida
Es el inicio de toda cadena condicional. Si su condición es `True`, el cuerpo se ejecuta y el resto de la cadena (`elif`/`else`) se ignora.

### `elif`: Condiciones Adicionales
Abreviatura de "else if". Permite comprobar múltiples condiciones en orden. Un `elif` solo se evalúa si el `if` inicial y todos los `elif` anteriores fueron `False`.

### `else`: La Opción por Defecto
Es el bloque que se ejecuta si **ninguna** de las condiciones anteriores (`if` y `elif`) se cumplió. No lleva condición.

#### Ejemplo Práctico: Análisis de Códigos de Estado HTTP

```python
status_code = 404

if status_code == 200:
    print("Petición exitosa (OK).")
elif status_code == 401:
    print("Error de autenticación (Unauthorized).")
elif status_code == 403:
    print("Error de permisos (Forbidden).")
elif status_code == 404:
    print("Recurso no encontrado (Not Found).")
elif status_code >= 500 and status_code < 600:
    print(f"Error del servidor (código {status_code}).")
else:
    print(f"Código de estado no reconocido: {status_code}")

# Salida: Recurso no encontrado (Not Found).
```

### Diferencia Clave: `if` Múltiples vs. `if-elif`

- **Múltiples `if`:** Cada `if` es una pregunta separada. Python las evaluará todas, una por una.
- **Cadena `if-elif-else`:** Es una única pregunta con múltiples respuestas posibles. Python se detiene en la primera que sea `True`.

```python
# Caso 1: if-elif (se detiene en la primera verdadera)
port = 80
if port == 80:
    print("Puerto HTTP") # Se imprime y la cadena termina
elif port < 1024:
    print("Puerto de sistema") # Esta línea NUNCA se ejecuta

# Caso 2: if múltiples (se evalúan todas)
if port == 80:
    print("Puerto HTTP") # Se imprime
if port < 1024:
    print("Puerto de sistema") # Se imprime también
```

---

## Aplicación Práctica

Hemos aplicado estos conceptos en nuestro script [`password_validator.py`](../src/password_validator.py) para decidir la fortaleza de una contraseña basándonos en un conjunto de reglas.

## Puntos Clave para un Analista de Seguridad

- Las condicionales son tu herramienta principal para la automatización basada en reglas.
- La sintaxis es estricta: no olvides el `:` al final de la cabecera y la indentación del cuerpo.
- Usa `if-elif-else` para decisiones mutuamente excluyentes (como nuestro validador de contraseñas).
- Usa operadores lógicos (`and`, `or`) para crear reglas de seguridad complejas y específicas.
- El operador `in` es extremadamente potente para comprobar si un elemento (una IP, un hash, un usuario) está en una lista de elementos conocidos (una blacklist, una lista de administradores, etc.).