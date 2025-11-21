# Guía de Herramientas de Ciberseguridad

Este documento sirve como una guía centralizada para las herramientas de ciberseguridad desarrolladas en este proyecto. Cada sección describe una herramienta, su propósito, su relevancia en el ámbito de la ciberseguridad y un ejemplo básico de uso.

---

## 1. Validador de Contraseñas (`password_validator.py`)

### ¿Qué hace?
Este script evalúa la fortaleza de una contraseña basándose en criterios como longitud, presencia de mayúsculas, minúsculas, números y caracteres especiales.

### ¿Por qué es importante en ciberseguridad?
La validación de contraseñas es fundamental para prevenir ataques de fuerza bruta y de diccionario. Al exigir contraseñas robustas, se reduce significativamente la superficie de ataque de un sistema, protegiendo las cuentas de usuario de accesos no autorizados.

### ¿Cómo se usa?
```python
from src.password_validator import validate_password_strength

password = "MiContraseñaSegura123!"
strength = validate_password_strength(password)
print(f"La fortaleza de la contraseña es: {strength}")
```

---

## 2. Analizador de Logs (`log_analyzer.py`)

### ¿Qué hace?
Este script procesa bloques de texto de logs para extraer información relevante, como direcciones IP asociadas a intentos de login fallidos.

### ¿Por qué es importante en ciberseguridad?
El análisis de logs es una práctica esencial para la detección de intrusiones y la respuesta a incidentes. Permite identificar patrones de actividad sospechosa, como múltiples intentos de login fallidos desde una misma IP, lo que podría indicar un ataque de fuerza bruta o un escaneo de credenciales.

### ¿Cómo se usa?
```python
from src.log_analyzer import extract_ips_from_log

log_content = """
[2025-10-14 14:10:05] - ERROR - Failed login attempt from 192.168.1.100
[2025-10-14 14:10:15] - INFO - User 'root' logged in.
"""
found_ips = extract_ips_from_log(log_content)
print(f"IPs con intentos fallidos: {found_ips}")
```

---

## 3. Validador de IPs (`ip_validator.py`)

### ¿Qué hace?
Este script filtra una lista de direcciones IP, permitiendo solo aquellas que se encuentran en una "lista blanca" (allow list) predefinida.

### ¿Por qué es importante en ciberseguridad?
La validación de IPs es una medida de seguridad perimetral que ayuda a controlar el acceso a recursos sensibles. Al permitir solo IPs conocidas y de confianza, se reduce el riesgo de accesos desde fuentes no autorizadas, siendo una capa de defensa contra ataques externos.

### ¿Cómo se usa?
```python
from src.ip_validator import filter_allowed_ips

ip_list = ["192.168.1.10", "8.8.8.8"]
allow_list = ["192.168.1.10"]
allowed_ips = filter_allowed_ips(ip_list, allow_list)
print(f"IPs permitidas: {allowed_ips}")
```

---

## 4. Rastreador de Logins (`login_tracker.py`)

### ¿Qué hace?
Este script simula y rastrea intentos de login para un usuario, bloqueando la cuenta si se excede un número máximo de intentos fallidos.

### ¿Por qué es importante en ciberseguridad?
El rastreo de logins y el bloqueo de cuentas son mecanismos cruciales para mitigar ataques de fuerza bruta y de relleno de credenciales. Al limitar los intentos de login, se dificulta que los atacantes adivinen contraseñas o utilicen credenciales robadas para acceder a las cuentas.

### ¿Cómo se usa?
```python
from src.login_tracker import LoginTracker

tracker = LoginTracker()
username = "usuario_ejemplo"
tracker.record_attempt(username)
if tracker.is_locked(username):
    print(f"La cuenta de {username} está bloqueada.")
```

---

## 5. Generador de IDs de Empleado (`generador_id_empleado.py`)

### ¿Qué hace?
Este script genera una lista de IDs de empleado únicos para el departamento de Ventas, siguiendo un patrón numérico específico (números divisibles por 5 en un rango determinado).

### ¿Por qué es importante en ciberseguridad?
La generación controlada y predecible de IDs es relevante para la gestión de identidades y accesos. Un esquema de IDs bien definido facilita la auditoría, la implementación de políticas de control de acceso basadas en roles (RBAC) y la detección de IDs anómalos o no autorizados, lo que contribuye a la integridad del sistema de gestión de usuarios.

### ¿Cómo se usa?
```python
from src.generador_id_empleado import generar_ids_empleado

ids = generar_ids_empleado()
print(f"IDs generados: {ids}")
```

---

## 6. Lector de Logs Simples (`lector_logs_simples.py`)

### ¿Qué hace?
Este script lee un archivo de texto (como un log) línea por línea y busca todas las ocurrencias de un término de búsqueda específico, como "ERROR" o "admin".

### ¿Por qué es importante en ciberseguridad?
Es una herramienta fundamental para el análisis forense y el monitoreo de sistemas. Permite a un analista filtrar rápidamente terabytes de datos de logs para encontrar evidencia de un compromiso, errores críticos del sistema o actividad de un usuario específico. Es el primer paso en cualquier investigación de incidentes basada en logs.

### ¿Cómo se usa?
```python
from src.lector_logs_simples import analizar_log_simple

# La ruta al archivo que quieres analizar
archivo_log = "data/simple_log.txt"
# El término que te interesa encontrar
palabra_clave = "ERROR"

analizar_log_simple(archivo_log, palabra_clave)
```

---

## 7. Escáner de Puertos (`port_scanner.py`)

### ¿Qué hace?
Este módulo permite verificar si un puerto específico (o una lista de puertos) está abierto en una dirección IP objetivo. Utiliza la librería `socket` de Python para intentar establecer una conexión TCP.

### ¿Por qué es importante en ciberseguridad?
El escaneo de puertos es una de las primeras fases en una prueba de penetración (pentesting) o auditoría de seguridad. Permite identificar qué servicios están corriendo en un servidor (ej: web en puerto 80, SSH en puerto 22) y, por tanto, qué vectores de ataque podrían estar disponibles. También es útil para administradores que quieren verificar que sus firewalls están bloqueando correctamente el tráfico no deseado.

### ¿Cómo se usa?
```python
from src.port_scanner import scan_ports

target_ip = "192.168.1.1"
common_ports = [22, 80, 443]

open_ports = scan_ports(target_ip, common_ports)
print(f"Puertos abiertos encontrados: {open_ports}")
```

---

## 8. Escáner de Red (`network_scanner.py`)

### ¿Qué hace?
Este script realiza un "Ping Sweep" (barrido de ping) para descubrir qué dispositivos están activos en una subred completa (ej: 192.168.1.0/24). Utiliza `subprocess` para ejecutar el comando ping del sistema operativo y `threading` para escanear múltiples IPs simultáneamente, reduciendo drásticamente el tiempo de ejecución.

### ¿Por qué es importante en ciberseguridad?
El descubrimiento de hosts es vital para tener un inventario real de la red. Un atacante lo usa para saber qué máquinas atacar; un defensor (Blue Team) lo usa para detectar dispositivos no autorizados (Shadow IT) conectados a la red corporativa.

### ¿Cómo se usa?
```python
from src.network_scanner import scan_network

# Escanear la red 192.168.1.x
active_hosts = scan_network("192.168.1")

print(f"Dispositivos activos: {active_hosts}")
```

