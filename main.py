# main.py
import argparse
import sys
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
from src.access_control import update_server_access_list
from src.access_list_updater import update_file as update_access_list


# --- Funciones para cada opción del menú ---

def run_password_validator(args):
    """Opción 1: Pide una contraseña y muestra su fortaleza."""
    print("\n--- Validador de Contraseñas ---")
    password = input("Introduce la contraseña a validar: ")
    strength = validate_password_strength(password)
    print(f"-> La fortaleza de la contraseña es: {strength}\n")

def run_log_analyzer(args):
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

def run_ip_validator(args):
    """Opción 3: Filtra una lista de IPs contra una lista de permitidos."""
    print("\n--- Validador de IPs ---")
    ip_list = ["192.168.1.10", "8.8.8.8", "10.0.0.5", "192.168.1.1"]
    allow_list = ["192.168.1.1", "192.168.1.10"]
    
    print(f"IPs a verificar: {ip_list}")
    print(f"Lista de IPs permitidas: {allow_list}")
    
    allowed_ips = filter_allowed_ips(ip_list, allow_list)
    
    print(f"-> IPs que pasaron el filtro: {allowed_ips}\n")

def run_login_tracker(args):
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

def run_id_generator(args):
    """Opción 5: Genera y muestra IDs de empleado."""
    print("\n--- Generador de IDs de Empleado ---")
    ids = generar_ids_empleado()
    print(f"-> Se generaron {len(ids)} IDs para el departamento de Ventas.")
    print(f"-> Lista de IDs: {ids}\n")

def run_port_scanner(args):
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

def run_network_scanner(args):
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

def run_ip_analyzer_demo(args):
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

def run_log_parser_demo(args):
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

def run_pattern_detector_demo(args):
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


def run_access_control(args):
    """Opción 11: Actualiza la lista de control de acceso (Allow List)."""
    print("\n--- Control de Acceso (Actualizar Allow List) ---")
    file_path = input("Introduce la ruta del archivo (ej: data/allow_list.txt): ")
    
    # Si el usuario no pone nada, sugerimos el archivo por defecto
    if not file_path:
        file_path = "data/allow_list.txt"
        print(f"Usando archivo por defecto: {file_path}")

    ips_input = input("Introduce las IPs a eliminar separadas por espacio: ")
    ips_to_remove = ips_input.split()
    
    if not ips_to_remove:
        print("No se introdujeron IPs. Operación cancelada.")
        return

    try:
        update_server_access_list(file_path, ips_to_remove)
        print("-> Lista actualizada correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    print("")

def handle_update_ips(args):
    print("--- Ejecutando el Actualizador de Listas de Acceso ---")
    success = update_access_list(args.allow_list, args.remove_list, args.output)
    if not success:
        print("La operación falló. Revisa los logs para más detalles.")
        sys.exit(1)
    print("--- Operación completada ---")


def main():
    parser = argparse.ArgumentParser(
        description="Herramienta Central de Ciberseguridad - Proyecto Curso Python",
        epilog="Usa 'python3 main.py <comando> --help' para más información sobre un comando específico."
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Comandos disponibles")

    # Subcomando para 'update-ips'
    parser_update = subparsers.add_parser("update-ips", help="Actualiza una lista de IPs permitidas.")
    parser_update.add_argument("-a", "--allow-list", required=True, help="Ruta al archivo con la lista de IPs permitidas.")
    parser_update.add_argument("-r", "--remove-list", required=True, help="Ruta al archivo con las IPs a eliminar.")
    parser_update.add_argument("-o", "--output", help="Opcional: Ruta al archivo de salida.")
    parser_update.set_defaults(func=handle_update_ips)

    # Subcomandos para las demostraciones
    parser_demo_log = subparsers.add_parser("demo-log-analyzer", help="Ejecuta la demo del analizador de logs.")
    parser_demo_log.set_defaults(func=run_log_analyzer)

    parser_demo_ip = subparsers.add_parser("demo-ip-analyzer", help="Ejecuta la demo del analizador de IPs.")
    parser_demo_ip.set_defaults(func=run_ip_analyzer_demo)

    parser_demo_parser = subparsers.add_parser("demo-log-parser", help="Ejecuta la demo del parser de logs con regex.")
    parser_demo_parser.set_defaults(func=run_log_parser_demo)

    parser_demo_ioc = subparsers.add_parser("demo-ioc-detector", help="Ejecuta la demo del detector de IoCs.")
    parser_demo_ioc.set_defaults(func=run_pattern_detector_demo)
    
    parser_demo_pass = subparsers.add_parser("demo-pass-validator", help="Ejecuta la demo del validador de contraseñas.")
    parser_demo_pass.set_defaults(func=run_password_validator)
    
    parser_demo_ip_val = subparsers.add_parser("demo-ip-validator", help="Ejecuta la demo del validador de IPs.")
    parser_demo_ip_val.set_defaults(func=run_ip_validator)
    
    parser_demo_login = subparsers.add_parser("demo-login-tracker", help="Ejecuta la demo del rastreador de logins.")
    parser_demo_login.set_defaults(func=run_login_tracker)
    
    parser_demo_id = subparsers.add_parser("demo-id-generator", help="Ejecuta la demo del generador de IDs.")
    parser_demo_id.set_defaults(func=run_id_generator)
    
    parser_port_scan = subparsers.add_parser("port-scan", help="Escanea puertos en una IP objetivo.")
    parser_port_scan.set_defaults(func=run_port_scanner)
    
    parser_net_scan = subparsers.add_parser("network-scan", help="Escanea una red en busca de hosts activos.")
    parser_net_scan.set_defaults(func=run_network_scanner)
    
    parser_access_control = subparsers.add_parser("access-control", help="Actualiza la lista de control de acceso.")
    parser_access_control.set_defaults(func=run_access_control)
    

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
