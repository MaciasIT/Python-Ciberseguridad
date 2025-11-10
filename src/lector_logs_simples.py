# src/lector_logs_simples.py

"""
Este script demuestra cómo leer un archivo de texto línea por línea
y buscar un patrón simple.
"""

def analizar_log_simple(ruta_archivo, termino_busqueda):
    """
    Lee un archivo de log y muestra las líneas que contienen un término específico.

    En ciberseguridad, esta es una técnica básica para el "triaje" de logs,
donde un analista busca rápidamente palabras clave como "ERROR", "Failed",
"Denied" para encontrar eventos de interés.

    Args:
        ruta_archivo (str): La ruta al archivo de log.
        termino_busqueda (str): La palabra o término a buscar en cada línea.
    """
    print(f"--- Analizando el archivo '{ruta_archivo}' ---")
    print(f"Buscando líneas que contengan: '{termino_busqueda}'\n")
    
    lineas_encontradas = 0

    try:
        # Usamos 'with open()' para asegurar que el archivo se cierre correctamente.
        # Especificamos 'encoding="utf-8"' como buena práctica.
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            # Iteramos sobre el archivo línea por línea.
            # Es la forma más eficiente en memoria para leer archivos grandes.
            for numero_linea, linea in enumerate(f, 1):
                # Buscamos si el término de búsqueda está en la línea (ignorando mayúsculas/minúsculas).
                if termino_busqueda.lower() in linea.lower():
                    print(f"  [Línea {numero_linea}]: {linea.strip()}")
                    lineas_encontradas += 1
    
    except FileNotFoundError:
        print(f"¡ERROR! El archivo '{ruta_archivo}' no fue encontrado.")
        print("Por favor, asegúrate de que el archivo existe en la ruta correcta.")
        return # Salimos de la función si el archivo no existe. 
    
    except Exception as e:
        print(f"¡ERROR! Ocurrió un error inesperado al leer el archivo: {e}")
        return

    print(f"\n--- Análisis completado ---")
    if lineas_encontradas > 0:
        print(f"Se encontraron {lineas_encontradas} línea(s) con el término '{termino_busqueda}'.")
    else:
        print(f"No se encontraron líneas con el término '{termino_busqueda}'.")


# Este bloque se ejecuta solo si el script es llamado directamente.
if __name__ == "__main__":
    # Definimos la ruta al archivo de log y el término que queremos buscar.
    # En un script real, estos valores podrían venir de argumentos de línea de comandos.
    archivo_log = "data/simple_log.txt"
    palabra_clave = "ERROR"
    
    analizar_log_simple(archivo_log, palabra_clave)

    print("\n" + "="*40 + "\n")

    # Segundo ejemplo: buscar una palabra clave diferente.
    palabra_clave_2 = "admin"
    analizar_log_simple(archivo_log, palabra_clave_2)
