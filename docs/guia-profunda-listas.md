# Guía Profunda sobre Listas en Python

Las listas son una de las estructuras de datos más versátiles y fundamentales en Python. Si bien la [guía general de estructuras de datos](./guia-estructuras-de-datos.md) ofrece una introducción, este documento profundiza en las técnicas y métodos que te darán un control total sobre ellas.

Dominar las listas es esencial en ciberseguridad para manipular colecciones de indicadores de compromiso (IOCs), líneas de logs, listas de usuarios, puertos, etc.

---

## 1. Indexación Avanzada y Slicing (Rebanado)

### Indexación
Recordemos que se accede a los elementos por su posición (índice), comenzando en `0`.

- **Indexación Negativa**: Python permite usar índices negativos para contar desde el final. `-1` es el último elemento, `-2` el penúltimo, y así sucesivamente.

```python
# Lista de IPs detectadas en un ataque de fuerza bruta
attacker_ips = ["203.0.113.5", "198.51.100.22", "203.0.113.45", "198.51.100.8"]

# Obtener la primera IP (la que inició el ataque)
primera_ip = attacker_ips[0] # "203.0.113.5"

# Obtener la última IP detectada
ultima_ip = attacker_ips[-1] # "198.51.100.8"

print(f"El ataque se originó en {primera_ip} y la última IP registrada fue {ultima_ip}.")
```

### Slicing (Rebanado)
El slicing te permite extraer una **sub-lista** (una porción) de tu lista. La sintaxis es `lista[start:stop:step]`.

- `start`: El índice donde empieza el rebanado (incluido). Si se omite, es `0`.
- `stop`: El índice donde termina el rebanado (**no incluido**). Si se omite, es hasta el final.
- `step`: El "paso" o intervalo. Si se omite, es `1`.

```python
log_events = ["user_login", "file_access", "failed_login", "user_logout", "firewall_alert", "system_shutdown"]

# Obtener los primeros 3 eventos
primeros_eventos = log_events[0:3] # o log_events[:3]
# Resultado: ['user_login', 'file_access', 'failed_login']

# Obtener los eventos desde el índice 2 hasta el final
eventos_criticos = log_events[2:]
# Resultado: ['failed_login', 'user_logout', 'firewall_alert', 'system_shutdown']

# Obtener una lista con la secuencia invertida
eventos_invertidos = log_events[::-1]
# Resultado: ['system_shutdown', 'firewall_alert', 'user_logout', 'failed_login', 'file_access', 'user_login']
```

---

## 2. Métodos Principales de una Lista

### Modificación
- `.append(item)`: Añade un elemento al **final** de la lista.
- `.insert(index, item)`: Inserta un elemento en una **posición específica**.
- `.pop(index=-1)`: Elimina y **devuelve** el elemento en un índice. Por defecto, el último.
- `.remove(item)`: Elimina la **primera aparición** de un valor específico.

```python
# Lista de puertos a escanear
ports_to_scan = [80, 443, 8080]

# Añadimos un puerto común al final
ports_to_scan.append(22) # [80, 443, 8080, 22]

# Insertamos un puerto de alta prioridad al principio
ports_to_scan.insert(0, 21) # [21, 80, 443, 8080, 22]

# Procesamos y eliminamos el primer puerto de la lista
puerto_actual = ports_to_scan.pop(0) # puerto_actual = 21, lista = [80, 443, 8080, 22]

# Eliminamos un puerto que resultó ser un falso positivo
ports_to_scan.remove(8080) # [80, 443, 22]
```

### Orden y Búsqueda
- `.sort()`: Ordena la lista **in-place** (modifica la lista original).
- `.reverse()`: Invierte el orden de la lista **in-place**.
- `.index(item)`: Devuelve el índice de la primera aparición de un elemento.
- `.count(item)`: Devuelve cuántas veces aparece un elemento en la lista.

```python
failed_attempts_ips = ["10.0.0.5", "192.168.1.100", "10.0.0.5"]

# Contar cuántos intentos vinieron de una IP específica
num_intentos = failed_attempts_ips.count("10.0.0.5") # 2

# Ordenar la lista para agrupar IPs
failed_attempts_ips.sort() # ["10.0.0.5", "10.0.0.5", "192.168.1.100"]

# Encontrar en qué posición apareció por primera vez una IP tras ordenar
posicion = failed_attempts_ips.index("192.168.1.100") # 2
```

---

## 3. List Comprehensions (Comprensión de Listas)

Es una forma elegante y eficiente de crear listas a partir de otras secuencias. La sintaxis es: `[expresion for item in iterable if condicion]`.

#### Ejemplo: Filtrar logs
Imagina que tienes una lista de líneas de log y solo quieres las que contienen "ERROR".

**Forma tradicional (bucle `for`):**
```python
log_lines = ["[INFO] OK", "[ERROR] Access Denied", "[INFO] User logged out", "[ERROR] Not Found"]
error_lines = []
for line in log_lines:
    if "ERROR" in line:
        error_lines.append(line)
# Resultado: ['[ERROR] Access Denied', '[ERROR] Not Found']
```

**Con List Comprehension (más "Pythónico"):**
```python
log_lines = ["[INFO] OK", "[ERROR] Access Denied", "[INFO] User logged out", "[ERROR] Not Found"]
error_lines = [line for line in log_lines if "ERROR" in line]
# Resultado: ['[ERROR] Access Denied', '[ERROR] Not Found']
```

#### Ejemplo 2: Extraer IPs de los logs de error
Podemos incluso aplicar una transformación al elemento.

```python
# Suponiendo que cada línea de error tiene el formato "[ERROR] From IP: xxx.xxx.xxx.xxx"
error_logs = ["[ERROR] From IP: 203.0.113.5", "[ERROR] From IP: 198.51.100.22"]

# Extraemos solo la IP de cada línea
error_ips = [log.split(": ")[-1] for log in error_logs]
# Resultado: ['203.0.113.5', '198.51.100.22']
```

## Conclusión
- Las listas son colecciones **ordenadas y mutables**.
- El **slicing** es una herramienta potentísima para trabajar con subconjuntos de datos.
- Los **métodos** (`.append`, `.sort`, etc.) te dan un control granular sobre los elementos de la lista.
- Las **List Comprehensions** son la forma preferida y más eficiente de crear listas nuevas a partir de iterables, especialmente cuando necesitas filtrar o transformar datos.
