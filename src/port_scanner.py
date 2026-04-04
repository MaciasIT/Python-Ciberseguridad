import socket
import ipaddress

def validate_ip(ip):
    """Validate if the input is a valid IP address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def scan_port(ip, port, timeout=0.5):
    """
    Intenta conectar a una IP y puerto específicos para verificar si está abierto.
    
    Args:
        ip (str): La dirección IP objetivo.
        port (int): El número de puerto a verificar.
        timeout (float): Tiempo máximo de espera en segundos.
        
    Returns:
        bool: True si el puerto está abierto, False si está cerrado o filtrado.
    """
    if not validate_ip(ip):
        return False
    
    if not (1 <= port <= 65535):
        return False

    try:
        # Crear un socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # connect_ex devuelve 0 si la operación tiene éxito
        result = sock.connect_ex((ip, port))
        
        sock.close()
        
        return result == 0
    except Exception:
        return False

def scan_ports(ip, ports):
    """
    Escanea una lista de puertos en una IP objetivo.
    
    Args:
        ip (str): La dirección IP objetivo.
        ports (list): Lista de enteros representando los puertos a escanear.
        
    Returns:
        list: Lista de puertos que se encontraron abiertos.
    """
    if not validate_ip(ip):
        print(f"Error: IP inválida: {ip}")
        return []

    open_ports = []
    
    print(f"Iniciando escaneo en {ip}...")
    
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
            
    return open_ports
