# main.py

# Importamos la función que queremos usar desde nuestro módulo.
from src.log_analyzer import extract_ips_from_log

# --- Simulación de un Entorno Real ---

# 1. Simulamos el contenido de un archivo de log que podríamos haber leído.
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

# 2. Usamos nuestra función para extraer las IPs.
# La función se encargará de procesar el texto y detenerse si hay una alerta crítica.
found_ips = extract_ips_from_log(log_content)

print(f"Análisis completado. Se encontraron {len(found_ips)} intentos de login fallidos antes de una alerta crítica (si la hubo).")

# 3. Contamos los intentos por cada IP.
# Usamos un diccionario para almacenar las cuentas: {'ip': count}
ip_counts = {}
for ip in found_ips:
    # .get(ip, 0) busca la IP en el diccionario. Si no la encuentra, devuelve 0.
    # Luego le sumamos 1 y lo guardamos.
    ip_counts[ip] = ip_counts.get(ip, 0) + 1

# 4. Imprimimos el reporte final.
if ip_counts:
    print("\n--- Reporte de Intentos de Login Fallidos ---")
    # Iteramos sobre el diccionario para mostrar los resultados.
    for ip, count in ip_counts.items():
        print(f"- IP: {ip:<15} | Intentos: {count}")
else:
    print("\nNo se registraron intentos de login fallidos relevantes.")

print("\n--- Fin del script ---")
