import re


def filter_ips_from_log(log_lines):
    """
    Extrae todas las direcciones IPv4 válidas de una lista de líneas de log.
    Valida que cada octeto esté en el rango de 0 a 255.

    Args:
        log_lines (list): Una lista de cadenas, donde cada cadena es una línea de log.

    Returns:
        list: Una lista de cadenas que contienen solo las direcciones IP válidas encontradas.
    """
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    valid_ips = []

    # Primero, encontramos todas las cadenas que parecen IPs
    potential_ips = [ip for line in log_lines for ip in ip_pattern.findall(line)]

    # Segundo, validamos cada IP encontrada
    for ip in potential_ips:
        octets = ip.split('.')
        # Verificamos que cada octeto sea un número entre 0 y 255
        if len(octets) == 4 and all(0 <= int(octet) <= 255 for octet in octets):
            valid_ips.append(ip)

    return valid_ips


def extract_usernames(emails):
    """
    Extrae los nombres de usuario de una lista de direcciones de correo electrónico,
    ignorando las que no tienen un formato válido (sin '@').

    Args:
        emails (list): Una lista de cadenas con direcciones de correo electrónico.

    Returns:
        list: Una lista de cadenas con los nombres de usuario.
    """
    return [email.split('@')[0] for email in emails if '@' in email]

def hex_to_int(hex_strings):
    """
    Convierte una lista de cadenas hexadecimales a una lista de enteros.

    Args:
        hex_strings (list): Una lista de cadenas que representan valores hexadecimales (ej. '0x1a').

    Returns:
        list: Una lista de enteros correspondientes.
    """
    return [int(h, 16) for h in hex_strings]
