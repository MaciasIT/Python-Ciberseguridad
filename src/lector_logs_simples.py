# src/lector_logs_simples.py

"""
Este script demuestra cómo leer un archivo de texto línea por línea,
buscar un patrón simple y extraer datos estructurados con .split().
"""

def analizar_log_simple(ruta_archivo, termino_busqueda):
    """
    Lee un archivo de log, busca líneas que contienen un término específico
    y extrae información estructurada de ellas usando .split().

    En ciberseguridad, esta es una técnica básica para el "triaje" de logs,
    donde un analista busca rápidamente palabras clave como "ERROR", "Failed",
    o "Denied" para encontrar eventos de interés y extraer el mensaje asociado.

    Args:
        ruta_archivo (str): La ruta al archivo de log.
        termino_busqueda (str): La palabra o término a buscar en cada línea.
    """
    print(f"--- Analizando el archivo '{ruta_archivo}' ---")
    print(f"Buscando líneas que contengan: '{termino_busqueda}'\n")
    
    lineas_encontradas = 0

    try:
        # Usamos 'with open()' para asegurar que el archivo se cierre correctamente.
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            # Iteramos sobre el archivo línea por línea.
            for numero_linea, linea in enumerate(f, 1):
                # Buscamos si el término de búsqueda está en la línea (ignorando mayúsculas/minúsculas).
                if termino_busqueda.lower() in linea.lower():
                    lineas_encontradas += 1
                    print(f"  [+] Coincidencia en línea {numero_linea}: {linea.strip()}")
                    
                    # Intentamos extraer más detalles usando .split()
                    partes = linea.strip().split(' - ')
                    if len(partes) == 3:
                        # Si la línea tiene el formato esperado, extraemos sus partes.
                        timestamp = partes[0]
                        log_level = partes[1]
                        message = partes[2]
                        print(f"    - Nivel: {log_level}")
                        print(f"    - Mensaje: {message}\n")
                    else:
                        # Si no, lo indicamos.
                        print("    - (La línea no tiene el formato esperado para extraer detalles)\n")
    
    except FileNotFoundError:
        print(f"¡ERROR! El archivo '{ruta_archivo}' no fue encontrado.")
        print("Por favor, asegúrate de que el archivo existe en la ruta correcta.")
        return
    
    except Exception as e:
        print(f"¡ERROR! Ocurrió un error inesperado al leer el archivo: {e}")
        return

    print(f"--- Análisis completado ---")
    if lineas_encontradas > 0:
        print(f"Se encontraron {lineas_encontradas} línea(s) con el término '{termino_busqueda}'.")
    else:
        print(f"No se encontraron líneas con el término '{termino_busqueda}'.")


# Este bloque se ejecuta solo si el script es llamado directamente.
if __name__ == "__main__":
    archivo_log = "data/simple_log.txt"
    
    print("--- PRIMER ANÁLISIS: BUSCANDO ERRORES ---")
    palabra_clave_error = "ERROR"
    analizar_log_simple(archivo_log, palabra_clave_error)

    print("\n" + "="*50 + "\n")

    print("--- SEGUNDO ANÁLISIS: BUSCANDO ADVERTENCIAS (WARNINGS) ---")
    palabra_clave_warning = "WARNING"
    analizar_log_simple(archivo_log, palabra_clave_warning)

    print("\n" + "="*50 + "\n")

    print("--- DEMOSTRACIÓN DE .join() ---")
    partes_ruta = ["var", "log", "apache2", "access.log"]
    ruta_reconstruida = "/".join(partes_ruta)
    print(f"Partes: {partes_ruta}")
    print(f"Ruta reconstruida con '.join()': /{ruta_reconstruida}")
    print("\n" + "="*50 + "\n")
