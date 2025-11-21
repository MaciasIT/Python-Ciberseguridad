# main.py
import time
from pathlib import Path

# --- Importaciones de los módulos de herramientas ---
from src.password_validator import validate_password_strength
from src.log_analyzer import extract_ips_from_log
from src.ip_validator import filter_allowed_ips
from src.login_tracker import LoginTracker
from src.generador_id_empleado import generar_ids_empleado
from src.ip_analyzer import analyze_ips
from src.log_parser import parse_log_line
from src.pattern_detector import analyze_text
from src.port_scanner import scan_ports
from src.network_scanner import scan_network


# --- Funciones para cada opción del menú ---

def run_password_validator():
    """Opción 1: Pide una contraseña y muestra su fortaleza."""
    print("\n--- Validador de Contraseñas ---")
    password = input("Introduce la contraseña a validar: ")
    strength = validate_password_strength(password)
    print(f"-> La fortaleza de la contraseña es: {strength}\n")

def run_log_analyzer():
    """Opción 2: Analiza un bloque de texto de log y extrae IPs con intentos fallidos."""
    print("\n--- Analizador de Logs (Simple) ---")
    log_content = """
[2025-10-14 14:10:05] - ERROR - Failed login attempt from 192.168.1.100
[2025-10-14 14:10:15] - INFO - User 'root' logged in.
[2025-10-14 14:11:20] - ERROR - Failed login attempt from 203.0.113.45
[2025-10-14 14:12:01] - ERROR - Failed login attempt from 192.168.1.100
"""
    print("Analizando el siguiente bloque de log:")
    print("------------------------------------")
    print(log_content.strip())
    print("------------------------------------")
    
    found_ips = extract_ips_from_log(log_content)
    
    if not found_ips:
        print("-> No se encontraron IPs de intentos fallidos relevantes.\n")
        return

    ip_counts = {}
    for ip in found_ips:
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        
    print("\n-> Reporte de Intentos de Login Fallidos:")
    for ip, count in ip_counts.items():
        print(f"- IP: {ip:<15} | Intentos: {count}")
    print("")

def run_ip_validator():
    """Opción 3: Filtra una lista de IPs contra una lista de permitidos."""
    print("\n--- Validador de IPs ---")
    ip_list = ["192.168.1.10", "8.8.8.8", "10.0.0.5", "192.168.1.1"]
    allow_list = ["192.168.1.1", "192.168.1.10"]
    
    print(f"IPs a verificar: {ip_list}")
    print(f"Lista de IPs permitidas: {allow_list}")
    
    allowed_ips = filter_allowed_ips(ip_list, allow_list)
    
    print(f"-> IPs que pasaron el filtro: {allowed_ips}\n")

def run_login_tracker():
    """Opción 4: Simula intentos de login y muestra si una cuenta se bloquea."""
    print("\n--- Rastreador de Logins ---")
    tracker = LoginTracker()
    username = "test_user"
    
    print(f"Simulando intentos de login para el usuario '{username}'...")
    print(f"El máximo de intentos permitidos es: {tracker.MAX_ATTEMPTS}")
    
    for i in range(tracker.MAX_ATTEMPTS + 1):
        print(f"Intento {i + 1}...")
        tracker.record_attempt(username)
        time.sleep(0.5)
        if tracker.is_locked(username):
            print(f"-> ¡Cuenta bloqueada para '{username}'!")
            break
    print("")

def run_id_generator():
    """Opción 5: Genera y muestra IDs de empleado."""
    print("\n--- Generador de IDs de Empleado ---")
    ids = generar_ids_empleado()
    print(f"-> Se generaron {len(ids)} IDs para el departamento de Ventas.")
    print(f"-> Lista de IDs: {ids}\n")

def run_port_scanner():
    """Opción 9: Escanea puertos en una IP objetivo."""
    print("\n--- Escáner de Puertos ---")
    target_ip = input("Introduce la IP a escanear (ej: 127.0.0.1): ")
    
    print("Opciones de puertos:")
    print("1. Puertos comunes (21, 22, 80, 443, 3306, 8080)")
    print("2. Rango personalizado")
    choice = input("Elige una opción (1/2): ")
    
    ports = []
    if choice == "1":
        ports = [21, 22, 80, 443, 3306, 8080]
    elif choice == "2":
        start = int(input("Puerto inicial: "))
        end = int(input("Puerto final: "))
        ports = list(range(start, end + 1))
    else:
        print("Opción no válida. Usando puertos comunes por defecto.")
        ports = [21, 22, 80, 443, 3306, 8080]
        
    print(f"\nEscaneando {target_ip}...")
    open_ports = scan_ports(target_ip, ports)
    
    if open_ports:
        print(f"-> ¡Puertos Abiertos Encontrados!: {open_ports}")
    else:
        print("-> No se encontraron puertos abiertos en el rango seleccionado.")
    print("")

def run_network_scanner():
    """Opción 10: Escanea una red completa en busca de hosts activos."""
    print("\n--- Escáner de Red (Ping Sweep) ---")
    network = input("Introduce el prefijo de red (ej: 192.168.1): ")
    
    # Validación simple
    if network.count('.') != 2 and network.count('.') != 3:
        print("Formato incorrecto. Debe ser tipo '192.168.1' o '10.0.0'")
        return

    # Si el usuario pone 192.168.1. quitamos el último punto
    if network.endswith('.'):
        network = network[:-1]
        
    print(f"\nIniciando barrido de ping en {network}.0/24 ...")
    print("Esto puede tardar unos segundos dependiendo de la red.")
    
    active_hosts = scan_network(network)
    
    if active_hosts:
        print(f"\n-> ¡Hosts Activos Encontrados ({len(active_hosts)})!:")
        for host in active_hosts:
            print(f"   [+] {host}")
    else:
        print("\n-> No se encontraron hosts activos (o el firewall bloquea ICMP).")
    print("")

def run_ip_analyzer_demo():
    """Opción 6: Demostración del analizador de IPs avanzado."""
    print("\n\n--- Demo: Analizador de IPs Avanzado ---")
    raw_ips_from_monitoring = [
        "203.0.113.5", "198.51.100.22", "203.0.113.5",
        "203.0.113.45", "198.51.100.22", "203.0.113.5",
        "192.168.1.101"
    ]
    known_blacklist = ["203.0.113.5", "198.51.100.22", "99.99.99.99"]
    print(f"IPs crudas a analizar: {raw_ips_from_monitoring}")
    print(f"Blacklist conocida: {known_blacklist}")
    malicious_ips = analyze_ips(raw_ips=raw_ips_from_monitoring, blacklist=known_blacklist)
    if malicious_ips:
        print("\n--- ¡ALERTA DE SEGURIDAD! ---\nSe encontraron las siguientes IPs maliciosas:")
        for ip in malicious_ips:
            print(f"- {ip}")
    else:
        print("\n--- Análisis completado ---\nNo se encontraron amenazas.")
    print("\n--- Fin de la demostración ---\n")

def run_log_parser_demo():
    """Opción 7: Demostración del parser de logs con Regex."""
    print("\n\n--- Demo: Parser de Logs con Regex ---")
    log_de_ejemplo = "[2025-10-29 23:55:12] - WARNING - Memory usage exceeded 80%"
    parsed_log = parse_log_line(log_de_ejemplo)
    if parsed_log:
        print("Log analizado con éxito:")
        for key, value in parsed_log.items():
            print(f"  - {key}: {value}")
    else:
        print(f"La línea de log '\"{log_de_ejemplo}\"' no pudo ser analizada.")
    print("\n--- Fin de la demostración de regex ---\n")

def run_pattern_detector_demo():
    """Opción 8: Demostración del detector de patrones IoC."""
    print("\n\n--- Demo: Detector de Patrones de IoCs ---")
    log_file_path = Path("data/sample_log.txt")
    if log_file_path.exists():
        print(f"Leyendo log de ejemplo: {log_file_path}\n")
        log_text = log_file_path.read_text(encoding='utf-8', errors='ignore')
        found_patterns = analyze_text(log_text)
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
    print("\n--- Fin de la demostración del detector de patrones ---\n")


# --- Bucle principal del menú ---

def main():
    """Muestra el menú y gestiona la selección del usuario."""
    
    menu_options = {
        "1": ("Validador de Contraseñas", run_password_validator),
        "2": ("Analizador de Logs (Simple)", run_log_analyzer),
        "3": ("Validador de IPs", run_ip_validator),
        "4": ("Rastreador de Logins", run_login_tracker),
        "5": ("Generador de IDs de Empleado", run_id_generator),
        "6": ("Demo: Analizador de IPs Avanzado", run_ip_analyzer_demo),
        "7": ("Demo: Parser de Logs con Regex", run_log_parser_demo),
        "8": ("Demo: Detector de Patrones IoC", run_pattern_detector_demo),
        "9": ("Escáner de Puertos", run_port_scanner),
        "10": ("Escáner de Red (Ping Sweep)", run_network_scanner),
    }

    while True:
        print("--- Caja de Herramientas de Ciberseguridad ---")
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")
        print("0. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == "0":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        
        selected_option = menu_options.get(choice)
        if selected_option:
            selected_option[1]()
        else:
            print("Opción no válida. Por favor, elige de nuevo.\n")
        
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
