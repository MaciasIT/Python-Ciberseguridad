"""
Módulo para analizar listas de direcciones IP.
"""

def analyze_ips(raw_ips: list[str], blacklist: list[str]) -> list[str]:
    """
    Analiza una lista de IPs, la compara con una blacklist y devuelve las coincidencias.

    El proceso es:
    1. Elimina duplicados de la lista de IPs en crudo.
    2. Compara la lista de IPs únicas con la blacklist.
    3. Devuelve una lista ordenada de las IPs que aparecen en ambas.

    Args:
        raw_ips: Una lista de strings, donde cada string es una dirección IP.
                 Puede contener duplicados.
        blacklist: Una lista de strings con las IPs maliciosas conocidas.

    Returns:
        Una lista de strings ordenada y sin duplicados con las IPs de raw_ips
        que también están en la blacklist.
    """
    # 1. Eliminar duplicados
    unique_ips = list(set(raw_ips))

    # 2. Encontrar las IPs que están en la blacklist usando una list comprehension
    malicious_ips_found = [ip for ip in unique_ips if ip in blacklist]

    # 3. Ordenar la lista de resultados
    malicious_ips_found.sort()

    return malicious_ips_found
