# Tutorial Práctico: Creando un Script de Control de Acceso

En este tutorial, simularemos el trabajo de un analista de seguridad para crear un script que valide un intento de inicio de sesión. Usaremos este escenario para explorar en profundidad cómo las sentencias condicionales (`if`, `elif`, `else`) y los operadores (`or`, `and`, `in`) nos permiten construir una lógica de seguridad robusta.

## Parte 1: Validación del Sistema Operativo con `if-elif-else`

Nuestra primera tarea es verificar si el sistema operativo de un usuario requiere una actualización. Las reglas son:
- `OS 2` está actualizado.
- `OS 1` y `OS 3` necesitan una actualización.

#### Paso 1: La condición `if` básica
Comenzamos con el caso más simple: comprobar si el sistema está actualizado.

```python
system = "OS 2"

# Si el sistema es "OS 2", no se necesita actualización.
if system == "OS 2":
    print("Sistema actualizado. No se necesita ninguna acción.")
```

#### Paso 2: Añadiendo `else` para el caso alternativo
¿Qué pasa si no es "OS 2"? Necesitamos un mensaje alternativo. Para eso usamos `else`.

```python
system = "OS 1"

if system == "OS 2":
    print("Sistema actualizado.")
else:
    # Este bloque se ejecuta si la condición del 'if' es False.
    print("¡Actualización necesaria!")
```

#### Paso 3: Siendo más específicos con `elif`
El `else` anterior es demasiado genérico. ¿Qué pasa si el sistema es "OS 4", un sistema desconocido? Para manejar casos específicos, usamos `elif` (else if).

```python
system = "OS 4"

if system == "OS 2":
    print("Sistema actualizado.")
elif system == "OS 1":
    print("¡Actualización necesaria para OS 1!")
elif system == "OS 3":
    print("¡Actualización necesaria para OS 3!")
else:
    print(f"El sistema '{system}' no es reconocido.")
```

#### Paso 4: Refactorizando con el operador `or`
Podemos hacer el código más conciso. Dado que la acción para "OS 1" y "OS 3" es la misma, podemos combinar sus condiciones con el operador `or`.

```python
system = "OS 1"

if system == "OS 2":
    print("Sistema actualizado.")
# Si el sistema es "OS 1" O es "OS 3"...
elif system == "OS 1" or system == "OS 3":
    print("¡Actualización necesaria!")
else:
    print(f"El sistema '{system}' no es reconocido.")
```
Esta es la versión final y más limpia de nuestro validador de sistema operativo.

---

## Parte 2: Validación de Usuario con Listas y el Operador `in`

Ahora, debemos verificar si un intento de login pertenece a un usuario autorizado.

#### El Mal Enfoque (No Escalable)
Si tenemos pocos usuarios, podríamos sentir la tentación de hacer esto:

```python
approved_user1 = "elarson"
approved_user2 = "bmoreno"
username = "bmoreno"

# ¡Funciona, pero es repetitivo y difícil de mantener!
if username == approved_user1 or username == approved_user2:
    print("Usuario autorizado.")
```

#### La Solución Pythónica y Escalable
La práctica profesional es usar una **lista** para agrupar a los usuarios y el operador `in` para comprobar si el `username` está **en** la lista.

```python
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "tshah"

# Comprueba si el valor de 'username' existe dentro de la lista 'approved_list'
if username in approved_list:
    print("Acceso permitido: Usuario autorizado.")
else:
    print("Acceso denegado: Usuario no autorizado.")
```
Este código es más limpio, legible y fácil de actualizar.

---

## Parte 3: Combinando Condiciones con `and`

Nuestra última regla de seguridad es: **un usuario solo puede iniciar sesión si está autorizado Y lo hace en horario laboral.**

Para esto, combinamos las dos comprobaciones anteriores en una única sentencia `if` usando el operador `and`.

```python
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"

# Variable booleana que representa si es horario laboral
organization_hours = True 

# La condición 'and' solo es True si AMBAS partes son True
if (username in approved_list) and (organization_hours):
    print("Login exitoso. ¡Bienvenido!")
else:
    print("Intento de login fallido. Usuario no autorizado o fuera del horario permitido.")
```
Fíjate cómo usamos los paréntesis `()` para agrupar las condiciones y mejorar la legibilidad, aunque en este caso no son estrictamente necesarios.

## Conclusión

A través de este tutorial, hemos construido un script de control de acceso realista. Hemos aprendido a:
- Usar `if`, `elif` y `else` para crear flujos de decisión.
- Refinar la lógica con el operador `or` para agrupar condiciones.
- Escribir código escalable usando listas y el operador `in`.
- Combinar diferentes reglas de negocio en una sola condición con el operador `and`.

Estos son los bloques de construcción fundamentales para escribir scripts de automatización y análisis en ciberseguridad.
