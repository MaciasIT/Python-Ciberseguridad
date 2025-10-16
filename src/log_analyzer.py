# src/log_analyzer.py

def extract_ips_from_log(log_data):
    """
    Analiza una cadena de texto multilínea que simula un log y extrae las IPs.

    Args:
        log_data (str): El contenido del log.

    Returns:
        list: Una lista de las direcciones IP encontradas en el log.
    """
    ip_list = []

    for line in log_data.strip().splitlines():
        # Regla de seguridad crítica: si el sistema está comprometido, paramos todo.
        if "SYSTEM_COMPROMISED" in line:
            break # Sale del bucle for inmediatamente.

        # Si la línea no es relevante, la saltamos y continuamos con la siguiente.
        if "Failed login attempt from" not in line:
            continue

        # Si hemos llegado hasta aquí, es porque la línea SÍ es relevante.
        words = line.split()
        ip = words[-1]
        ip_list.append(ip)
    
    return ip_list

def process_log_queue(log_queue):
    """
    Procesa una "cola" (lista) de eventos de log uno por uno.

    Args:
        log_queue (list): Una lista de cadenas, donde cada una es una línea de log.
                          Esta lista será modificada (vaciada) en el proceso.

    Returns:
        list: Una lista de las direcciones IP encontradas.
    """
    ip_list = []

    # El bucle se ejecuta mientras la lista 'log_queue' no esté vacía.
    # En Python, una lista no vacía se evalúa como True.
    while log_queue:
        # .pop(0) extrae y elimina el primer elemento de la lista (como en una cola).
        line = log_queue.pop(0)

        if "Failed login attempt from" in line:
            words = line.split()
            ip = words[-1]
            ip_list.append(ip)
    
    return ip_list
