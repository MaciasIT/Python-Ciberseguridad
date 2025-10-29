import re
from typing import Dict, Optional

# Pre-compilamos la expresión regular para mayor eficiencia, ya que se usará muchas veces.
# El patrón usa grupos de captura () para extraer las partes que nos interesan.
LOG_REGEX = re.compile(
    r"^\[(.*?)\]\s+-\s+(.*?)\s+-\s+(.*)$"
)

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Analiza una sola línea de log y la descompone en sus partes.

    Args:
        line: La línea de log a analizar.

    Returns:
        Un diccionario con 'timestamp', 'level' y 'message' si la línea
        coincide con el patrón. En caso contrario, devuelve None.
    """
    match = LOG_REGEX.search(line)

    if not match:
        return None

    return {
        'timestamp': match.group(1),
        'level': match.group(2),
        'message': match.group(3)
    }
