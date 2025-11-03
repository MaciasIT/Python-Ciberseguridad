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


# =====================================================================
#  DEMOSTRACIÓN DEL NUEVO MÓDULO: IP ANALYZER
# =====================================================================

# 1. Importamos la nueva función
from src.ip_analyzer import analyze_ips

print("\n\n--- Iniciando demostración del analizador de IPs ---")

# 2. Datos de entrada
raw_ips_from_monitoring = [
    "203.0.113.5", "198.51.100.22", "203.0.113.5",
    "203.0.113.45", "198.51.100.22", "203.0.113.5",
    "192.168.1.101"
]
known_blacklist = ["203.0.113.5", "198.51.100.22", "99.99.99.99"]

print(f"IPs crudas a analizar: {raw_ips_from_monitoring}")
print(f"Blacklist conocida: {known_blacklist}")

# 3. Usar la función para encontrar IPs maliciosas
malicious_ips = analyze_ips(raw_ips=raw_ips_from_monitoring, blacklist=known_blacklist)

# 4. Generar el reporte
if malicious_ips:
    print("\n--- ¡ALERTA DE SEGURIDAD! ---\nSe encontraron las siguientes IPs maliciosas:")
    for ip in malicious_ips:
        print(f"- {ip}")
else:
    print("\n--- Análisis completado ---\nNo se encontraron amenazas.")

    print("\n--- Fin de la demostración ---")





# =====================================================================

#  DEMOSTRACIÓN DEL PARSER DE LOGS CON REGEX

# =====================================================================

from src.log_parser import parse_log_line



print("\n\n--- Iniciando demostración del parser de logs ---")



log_de_ejemplo = "[2025-10-29 23:55:12] - WARNING - Memory usage exceeded 80%"



parsed_log = parse_log_line(log_de_ejemplo)



if parsed_log:

    print("Log analizado con éxito:")

    for key, value in parsed_log.items():

        print(f"  - {key}: {value}")

else:

    print(f"La línea de log '\"{log_de_ejemplo}\"' no pudo ser analizada.")



print("\n--- Fin de la demostración de regex ---")

# =====================================================================
#  DEMOSTRACIÓN DEL DETECTOR DE PATRONES (IoCs)
# =====================================================================

from pathlib import Path
from src.pattern_detector import analyze_text

print("\n\n--- Iniciando demostración del detector de patrones de IoCs ---")

# 1. Leemos el contenido de un archivo de log de ejemplo
log_file_path = Path("data/sample_log.txt")
if log_file_path.exists():
    print(f"Leyendo log de ejemplo: {log_file_path}\n")
    log_text = log_file_path.read_text(encoding='utf-8', errors='ignore')

    # 2. Usamos el analizador para encontrar todos los patrones
    found_patterns = analyze_text(log_text)

    # 3. Mostramos un resumen de los resultados más interesantes
    print("--- Resumen de IoCs Encontrados ---")
    
    if found_patterns.get("ipv4_strict"):
        print(f"\n[+] IPs encontradas: {found_patterns['ipv4_strict']}")
    
    if found_patterns.get("email"):
        print(f"[+] Emails encontrados: {found_patterns['email']}")

    if found_patterns.get("md5"):
        print(f"[+] Hashes MD5: {found_patterns['md5']}")

    if found_patterns.get("sha1"):
        print(f"[+] Hashes SHA1: {found_patterns['sha1']}")

    if found_patterns.get("url"):
        print(f"[+] URLs encontradas: {found_patterns['url']}")

else:
    print(f"No se encontró el archivo de log de ejemplo en '{log_file_path}'. Saltando demostración.")

print("\n--- Fin de la demostración del detector de patrones ---")


