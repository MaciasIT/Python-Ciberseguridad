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
