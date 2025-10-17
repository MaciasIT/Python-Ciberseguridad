# src/ip_validator.py

def filter_allowed_ips(ip_addresses, allow_list):
    """
    Filtra una lista de direcciones IP, devolviendo solo las que están en una lista de permitidos.

    Args:
        ip_addresses (list): La lista de IPs a verificar.
        allow_list (list): La lista de IPs permitidas.

    Returns:
        list: Una nueva lista que contiene solo las IPs permitidas.
    """
    # Creamos una lista vacía para almacenar las IPs que pasen el filtro.
    allowed_ips_found = []

    # Iteramos sobre cada IP en la lista de direcciones a verificar.
    for ip in ip_addresses:
        # Usamos el operador 'in' para comprobar si la IP actual está en la lista de permitidos.
        if ip in allow_list:
            # Si está, la añadimos a nuestra lista de resultados.
            allowed_ips_found.append(ip)
    
    # Devolvemos la lista con las IPs filtradas.
    return allowed_ips_found

def check_ips_until_fail(ip_addresses, allow_list, on_processed_ip):
    """
    Verifica una lista de IPs y se detiene al encontrar la primera no permitida.

    Args:
        ip_addresses (list): La lista de IPs a verificar.
        allow_list (list): La lista de IPs permitidas.
        on_processed_ip (function): Una función (callback) que se llama por cada IP procesada con éxito.
    """
    # Iteramos sobre cada IP en la lista.
    for ip in ip_addresses:
        # Si la IP no está en la lista de permitidos...
        if ip not in allow_list:
            # ...imprimimos una alerta y rompemos el bucle.
            print(f"Alerta: IP no permitida encontrada: {ip}. Deteniendo el análisis.")
            break
        
        # Si la IP está permitida, llamamos a la función callback para registrar que fue procesada.
        on_processed_ip(ip)
