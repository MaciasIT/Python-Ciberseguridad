"""
Módulo de Control de Acceso
===========================

Este módulo proporciona funcionalidades para gestionar listas de control de acceso (ACLs)
basadas en archivos de texto. Permite automatizar la tarea de revocar accesos eliminando
direcciones IP específicas de una lista autorizada.

Funciones principales:
    - update_server_access_list: Actualiza un archivo de lista blanca eliminando IPs prohibidas.
"""

import os
from typing import List

def update_server_access_list(file_path: str, ips_to_remove: List[str]) -> None:
    """
    Actualiza un archivo de lista de acceso (allow list) eliminando las direcciones IP especificadas.

    Esta función lee un archivo que contiene direcciones IP (separadas por espacios o saltos de línea),
    filtra aquellas que están presentes en la lista `ips_to_remove`, y sobrescribe el archivo original
    con la lista actualizada.

    Args:
        file_path (str): La ruta absoluta o relativa al archivo de texto que contiene la lista de IPs permitidas.
        ips_to_remove (List[str]): Una lista de cadenas, donde cada cadena es una dirección IP que debe ser revocada.

    Raises:
        FileNotFoundError: Si el archivo especificado en `file_path` no existe.
        IOError: Si ocurre un error al leer o escribir en el archivo.

    Example:
        >>> update_server_access_list("data/allow_list.txt", ["192.168.1.1", "10.0.0.5"])
    """
    
    # Verificación de seguridad básica: asegurar que el archivo existe antes de intentar abrirlo
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo de lista de acceso no se encontró: {file_path}")

    # Paso 1: Leer el contenido del archivo
    # Usamos 'with' para garantizar que el archivo se cierre correctamente incluso si hay errores.
    with open(file_path, "r") as file:
        content = file.read()

    # Paso 2: Convertir el contenido en una lista
    # .split() sin argumentos divide por cualquier espacio en blanco (espacios, tabs, newlines).
    # Esto maneja robustamente archivos con diferentes formatos de espaciado.
    ip_addresses = content.split()

    # Paso 3: Filtrar las IPs (Lógica Core)
    # IMPORTANTE: Usamos una "List Comprehension" para crear una NUEVA lista.
    # Esto evita el error común de modificar una lista mientras se itera sobre ella,
    # lo cual puede causar que se salten elementos.
    #
    # Convertimos ips_to_remove a un set para búsquedas O(1) mucho más rápidas si la lista es grande.
    remove_set = set(ips_to_remove)
    
    updated_ips = [ip for ip in ip_addresses if ip not in remove_set]

    # Paso 4: Reconstruir el contenido del archivo
    # Unimos las IPs con un espacio simple. 
    # Nota: Si se prefiere mantener un formato de una IP por línea, cambiar " " por "\n".
    new_content = " ".join(updated_ips)

    # Paso 5: Sobrescribir el archivo con la lista actualizada
    with open(file_path, "w") as file:
        file.write(new_content)

    print(f"Proceso completado. Se eliminaron {len(ip_addresses) - len(updated_ips)} direcciones IP del archivo.")
