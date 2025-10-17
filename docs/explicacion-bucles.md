# Guía Detallada de Bucles en Python (`for` y `while`)

## ¿Qué son las Sentencias Iterativas (Bucles)?

Una sentencia iterativa, o bucle, es una estructura que ejecuta un bloque de código repetidamente. Para un analista de seguridad, los bucles son la principal herramienta para automatizar tareas tediosas y repetitivas, como analizar miles de líneas de un log, escanear un rango de puertos o procesar una lista de archivos en busca de malware.

Python ofrece dos tipos principales de bucles: `for` y `while`.

---

## 1. El Bucle `for`: Iterar sobre una Secuencia

El bucle `for` se utiliza cuando tienes una secuencia de elementos (como una lista, una cadena de texto o las líneas de un archivo) y quieres ejecutar un bloque de código **para cada uno de esos elementos**.

### Estructura del Bucle `for`

```python
# for variable_temporal in secuencia:
#     # Cuerpo del bucle (código que se repite)

# Ejemplo: Iterar sobre una lista de IPs sospechosas
suspicious_ips = ["10.0.0.5", "192.168.1.100", "8.8.8.8"]

for ip in suspicious_ips:
    print(f"Analizando la IP: {ip}")
    # Aquí iría el código para escanear o bloquear la IP
```

- **`for`**: Palabra clave que inicia el bucle.
- **`ip`**: Es la **variable de bucle**. En cada iteración, tomará el valor de uno de los elementos de la secuencia. Es una variable temporal que solo existe dentro del bucle.
- **`in`**: Operador que conecta la variable de bucle con la secuencia.
- **`suspicious_ips`**: La secuencia sobre la que se va a iterar.
- **`:` y la indentación**: Al igual que en los condicionales, la cabecera termina en dos puntos y el cuerpo debe estar indentado.

### La Función `range()`

Si necesitas repetir una acción un número específico de veces, `range()` es tu mejor aliado. Genera una secuencia de números.

```python
# range(stop): Genera números desde 0 hasta stop-1
# Ejemplo: Intentar conectar a un puerto 5 veces
for attempt in range(5): # Genera 0, 1, 2, 3, 4
    print(f"Intento de conexión número {attempt + 1}")
```

---

## 2. El Bucle `while`: Repetir mientras una Condición sea Cierta

El bucle `while` se utiliza cuando quieres repetir un bloque de código **mientras una condición se mantenga como `True`**. No sabes de antemano cuántas veces se ejecutará; solo sabes cuándo debe parar.

### Estructura del Bucle `while`

```python
# # Se inicializa una variable de control fuera del bucle
# while condicion:
#     # Cuerpo del bucle
#     # ¡Importante! Modificar la variable de control para evitar un bucle infinito

# Ejemplo: Procesar eventos de una cola hasta que esté vacía
log_events = ["event1", "event2", "event3"]

while log_events: # Mientras la lista 'log_events' no esté vacía (sea 'Truthy')
    event = log_events.pop(0) # Extrae el primer evento
    print(f"Procesando evento: {event}")

print("Cola de eventos vacía.")
```

- **Variable de control**: En los bucles `while`, la variable que controla la condición (`log_events` en este caso) debe existir *antes* del bucle.
- **Condición**: La expresión que se evalúa en cada iteración. Si es `False`, el bucle termina.
- **Modificación**: Dentro del bucle, algo debe ocurrir que eventualmente haga que la condición sea `False`. En nuestro ejemplo, `log_events.pop(0)` va vaciando la lista, hasta que se convierte en `False`.

---

## 3. `for` vs. `while`: ¿Cuál Elegir?

| Característica      | Bucle `for`                                     | Bucle `while`                                         |
| :------------------ | :---------------------------------------------- | :---------------------------------------------------- |
| **Uso Principal**   | Iterar sobre una secuencia (listas, etc.)       | Repetir hasta que una condición cambie                |
| **Naturaleza**      | **Definida** (sabes cuántos elementos hay)      | **Indefinida** (no sabes cuántas repeticiones hará)   |
| **Gestión**         | Automática (el bucle avanza solo)               | Manual (tú debes cambiar la condición para que pare)  |
| **Riesgo Principal**| Muy bajo (termina cuando la secuencia acaba)    | **Bucle infinito** si la condición nunca cambia       |

### La Regla de Oro

> Si tu lógica se puede expresar como "**para cada elemento en esta colección...**", usa un bucle `for`.
> 
> Si tu lógica es "**sigue haciendo esto hasta que esta situación cambie...**", usa un bucle `while`.

Para la mayoría de tareas de procesamiento de datos en ciberseguridad (analizar logs, IPs, hashes), el bucle `for` es más limpio, seguro y "Pythónico". El bucle `while` es para tareas más dinámicas, de espera o de ejecución continua.

---

## 4. Controlando el Flujo del Bucle: `break` y `continue`

A veces necesitas un control más fino sobre las iteraciones.

### `continue`: Saltar a la Siguiente Iteración

La sentencia `continue` detiene la iteración actual y salta inmediatamente al inicio de la siguiente. Es útil para ignorar elementos de una secuencia que no nos interesan.

```python
# Ejemplo: Analizar solo las líneas de ERROR en un log
for line in log_lines:
    if "ERROR" not in line:
        continue # No es un error, ignora esta línea y pasa a la siguiente
    
    # Este código solo se ejecuta si la línea contiene "ERROR"
    print(f"Error encontrado: {line}")
```

### `break`: Romper el Bucle

La sentencia `break` termina el bucle por completo, sin importar si quedan elementos en la secuencia o si la condición del `while` sigue siendo `True`. Es una salida de emergencia.

```python
# Ejemplo: Dejar de analizar si se detecta un compromiso del sistema
for line in log_lines:
    if "SYSTEM_COMPROMISED" in line:
        print("¡ALERTA CRÍTICA! Sistema comprometido. Análisis detenido.")
        break # Sal del bucle 'for' inmediatamente
    
    # Sigue el análisis normal si no hay alerta crítica
```

---

## 5. Aplicación Práctica: Creando un Script Principal (`main.py`)

Una vez que hemos creado y probado nuestras funciones (nuestra "biblioteca"), necesitamos un script principal que las utilice para realizar una tarea concreta. Este script se encarga de orquestar la lógica:

1.  Importa las funciones necesarias desde `src`.
2.  Prepara los datos de entrada (en nuestro caso, simula el contenido de un log).
3.  Llama a nuestras funciones para procesar los datos.
4.  Realiza análisis adicionales sobre los resultados (como contar IPs).
5.  Presenta un reporte final al usuario.

### Ejemplo de `main.py`

El siguiente código demuestra cómo usar la función `extract_ips_from_log` (definida en `src/log_analyzer.py`) en un script principal.

```python
# main.py

# 1. Importamos la función que queremos usar.
from src.log_analyzer import extract_ips_from_log

# 2. Simulamos el contenido de un archivo de log.
log_content = """
[2025-10-14 14:10:05] - ERROR - Failed login attempt from 192.168.1.100
[2025-10-14 14:10:15] - INFO - User 'root' logged in.
[2025-10-14 14:11:20] - ERROR - Failed login attempt from 203.0.113.45
[2025-10-14 14:12:01] - ERROR - Failed login attempt from 192.168.1.100
[2025-10-14 14:12:30] - ERROR - Failed login attempt from 198.51.100.2
[2025-10-14 14:13:00] - CRITICAL - SYSTEM_COMPROMISED
[2025-10-14 14:14:00] - ERROR - Failed login attempt from 10.0.0.1
"""

print("--- Iniciando análisis del log ---")

# 3. Usamos nuestra función para extraer las IPs.
found_ips = extract_ips_from_log(log_content)

print(f"Análisis completado. Se encontraron {len(found_ips)} intentos de login fallidos.")

# 4. Contamos los intentos por cada IP.
ip_counts = {}
for ip in found_ips:
    ip_counts[ip] = ip_counts.get(ip, 0) + 1

# 5. Imprimimos el reporte final.
if ip_counts:
    print("\n--- Reporte de Intentos de Login Fallidos ---")
    for ip, count in ip_counts.items():
        print(f"- IP: {ip:<15} | Intentos: {count}")
else:
    print("\nNo se registraron intentos de login fallidos relevantes.")

print("\n--- Fin del script ---")
```