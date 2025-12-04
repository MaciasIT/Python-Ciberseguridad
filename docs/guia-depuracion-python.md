# Guía de Depuración en Python para Ciberseguridad 🐛

La depuración (o *debugging*) es el proceso de identificar, analizar y corregir errores o fallos (*bugs*) en el código. En el ámbito de la ciberseguridad, un simple error puede tener consecuencias graves, como crear una vulnerabilidad de seguridad, impedir el análisis de un incidente o generar falsos negativos.

Comprender los tipos de errores y saber cómo solucionarlos es una habilidad fundamental para cualquier profesional de la seguridad que trabaje con código.

## Tipos de Errores en Python

En Python, podemos clasificar los errores en tres categorías principales:

### 1. Errores de Sintaxis (SyntaxError)

Son los más sencillos de identificar. Ocurren cuando el código no sigue las reglas gramaticales del lenguaje Python. El intérprete de Python detiene la ejecución y señala la línea exacta donde se encuentra el error.

**Ejemplo en Ciberseguridad:**

Imagina un script simple para comprobar si un puerto está en una lista de puertos peligrosos conocidos. Un error de sintaxis podría impedir que se ejecute.

```python
# Código con error: falta el dos puntos (:) al final del if
def es_puerto_peligroso(puerto):
    puertos_peligrosos = [21, 22, 23, 25, 80]
    if puerto in puertos_peligrosos
        return True
    return False
```

**Mensaje de Error:**

```
  File "<stdin>", line 3
    if puerto in puertos_peligrosos
                                    ^
SyntaxError: expected ':'
```

**Solución:** El mensaje de error es claro. Añadir los dos puntos (`:`) al final de la declaración `if` soluciona el problema.

### 2. Errores Lógicos (Logical Errors)

Estos son los errores más peligrosos y difíciles de detectar. El programa se ejecuta sin fallar, pero produce un resultado incorrecto porque la lógica del programador es defectuosa. En ciberseguridad, un error lógico puede crear una vulnerabilidad silenciosa.

**Ejemplo en Ciberseguridad:**

Un sistema de control de acceso debe bloquear una dirección IP después de 5 intentos de inicio de sesión fallidos. Un error lógico podría permitir más intentos de los debidos.

```python
# Lógica incorrecta: debería ser >= 5 para bloquear en el quinto intento
def verificar_intentos_login(intentos):
    if intentos > 5:  # ¡ERROR LÓGICO!
        print("IP bloqueada por exceso de intentos.")
        return False
    print("Acceso permitido.")
    return True

# El atacante prueba por quinta vez y el sistema no lo bloquea
verificar_intentos_login(5) # Devuelve "Acceso permitido."
```

**Problema:** La condición `intentos > 5` solo se cumple a partir del sexto intento. Un atacante tiene un intento extra para un ataque de fuerza bruta. La condición correcta sería `intentos >= 5`.

**Solución:** Estos errores se detectan mediante pruebas exhaustivas (TDD) y revisiones de código. Usar `print()` para inspeccionar el valor de las variables en puntos clave también ayuda a localizarlos.

### 3. Excepciones (Exceptions)

Una excepción ocurre cuando el código es sintácticamente correcto, pero se produce un error durante su ejecución que el intérprete no puede manejar. Por ejemplo, intentar dividir por cero o acceder a un archivo que no existe.

**Ejemplo en Ciberseguridad:**

Un script analiza un archivo de logs en formato JSON que proviene de una API de inteligencia de amenazas. Si un registro de un Indicador de Compromiso (IOC) no contiene un campo esperado, el programa fallará.

```python
# El script espera que cada IOC tenga la clave 'severidad'
def analizar_ioc(datos_ioc):
    # Si 'severidad' no existe, se lanzará una KeyError
    if datos_ioc['severidad'] == 'alta':
        print(f"ALERTA: IOC de alta severidad detectado: {datos_ioc['valor']}")

# Un IOC malformado de la API
ioc_incompleto = {"tipo": "ip", "valor": "198.51.100.10"}

# Esto detendrá el script por completo
analizar_ioc(ioc_incompleto)
```

**Mensaje de Error:**

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in analizar_ioc
KeyError: 'severidad'
```

**Solución:** El código debe ser más robusto. Se pueden usar bloques `try...except` para manejar estas situaciones sin que el programa se detenga, o verificar la existencia de las claves antes de usarlas con `datos_ioc.get('severidad')`.

## Técnicas Clave de Depuración

1.  **Leer el Mensaje de Error (Traceback):** Es la primera fuente de información. Te dice el tipo de error y la línea donde ocurrió.
2.  **Insertar `print()`:** La técnica más simple y a menudo más rápida. Coloca `print()` en tu código para ver el valor de las variables en diferentes puntos y entender dónde se desvía la lógica.
3.  **Usar un Depurador:** Herramientas como `pdb` (Python Debugger) o los depuradores integrados en los IDEs (VSCode, PyCharm) te permiten ejecutar el código línea por línea, inspeccionar variables en tiempo real y establecer *breakpoints* (puntos de interrupción) para detener la ejecución en lugares específicos.

## Conclusión

Los errores son una parte normal del desarrollo. En ciberseguridad, la diferencia radica en que las consecuencias pueden ser mucho más graves. Aprender a identificar el tipo de error y aplicar la técnica de depuración adecuada es crucial para escribir código seguro, robusto y fiable.
