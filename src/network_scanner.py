import subprocess
import platform
import concurrent.futures
import ipaddress

def validate_network_prefix(prefix):
    """Validate if the input is a valid network prefix (e.g., '192.168.1')."""
    try:
        # Intentar validar como una red /24
        ipaddress.ip_network(f"{prefix}.0/24", strict=False)
        return True
    except ValueError:
        return False

def ping_ip(ip):
    """
    Envía un ping a una dirección IP para verificar si está activa.
    
    Args:
        ip (str): La dirección IP a verificar.
        
    Returns:
        bool: True si la IP responde, False en caso contrario.
    """
    # Determinar el parámetro correcto para el número de paquetes según el SO
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Construir el comando: ping -c 1 -W 1 <ip>
    # -W 1 establece un timeout de 1 segundo para no esperar demasiado
    command = ['ping', param, '1', '-W', '1', ip]
    
    try:
        # Ejecutar el comando suprimiendo la salida (stdout y stderr)
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # returncode 0 significa éxito
        return result.returncode == 0
    except Exception:
        return False

def scan_network(network_prefix, max_workers=50):
    """
    Escanea una red completa (x.x.x.1-254) usando hilos para mayor velocidad.
    
    Args:
        network_prefix (str): Los primeros 3 octetos de la red (ej: "192.168.1").
        max_workers (int): Número máximo de hilos simultáneos.
        
    Returns:
        list: Lista de IPs activas encontradas.
    """
    if not validate_network_prefix(network_prefix):
        print(f"Error: Prefijo de red inválido: {network_prefix}")
        return []

    active_hosts = []
    
    # Generar la lista de IPs a escanear (del 1 al 254)
    ips_to_scan = [f"{network_prefix}.{i}" for i in range(1, 255)]
    
    print(f"Escaneando red {network_prefix}.0/24 con {max_workers} hilos...")
    
    # Usar ThreadPoolExecutor para ejecutar los pings en paralelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Mapear cada IP a la función ping_ip
        # future_to_ip es un diccionario {future: ip}
        future_to_ip = {executor.submit(ping_ip, ip): ip for ip in ips_to_scan}
        
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                if future.result():
                    active_hosts.append(ip)
                    # Opcional: Imprimir en tiempo real
                    # print(f"[+] Host encontrado: {ip}")
            except Exception as exc:
                pass
                
    # Ordenar la lista de IPs resultante (opcional, pero útil)
    # Una forma simple de ordenar IPs es por su último octeto
    active_hosts.sort(key=lambda ip: int(ip.split('.')[-1]))
    
    return active_hosts
