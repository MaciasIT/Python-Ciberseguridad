
import argparse
import logging
import sys

# --- Configuración del Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def update_file(allow_list_path, remove_list_path, output_path=None):
    """
    Lee una lista de IPs permitidas, elimina las que se encuentran en una lista de
    eliminación y escribe la lista actualizada de vuelta a un archivo.
    """
    try:
        logging.info(f"Leyendo la lista de permitidos desde: {allow_list_path}")
        with open(allow_list_path, 'r') as f:
            allow_ips = f.read().split()

        logging.info(f"Leyendo la lista de eliminación desde: {remove_list_path}")
        with open(remove_list_path, 'r') as f:
            remove_ips = f.read().split()

    except FileNotFoundError as e:
        logging.error(f"Error: Archivo no encontrado - {e.filename}")
        return False
    except IOError as e:
        logging.error(f"Error al leer el archivo: {e}")
        return False

    remove_ips_set = set(remove_ips)
    original_ip_count = len(allow_ips)

    updated_allow_ips = [ip for ip in allow_ips if ip not in remove_ips_set]

    removed_count = original_ip_count - len(updated_allow_ips)

    if removed_count > 0:
        logging.info(f"Se eliminaron {removed_count} dirección(es) IP.")

        if output_path is None:
            output_path = allow_list_path

        try:
            logging.info(f"Escribiendo la lista actualizada en: {output_path}")
            with open(output_path, 'w') as f:
                f.write('\n'.join(updated_allow_ips))
            logging.info("Archivo actualizado con éxito.")
        except IOError as e:
            logging.error(f"Error al escribir en el archivo: {e}")
            return False
    else:
        logging.info("No fue necesario eliminar ninguna dirección IP. El archivo no ha cambiado.")

    return True

def main():
    """
    Función principal para analizar los argumentos de la línea de comandos y ejecutar el proceso.
    """
    parser = argparse.ArgumentParser(
        description="Actualiza una lista de IPs permitidas eliminando las especificadas.",
        epilog="Ejemplo: python3 access_list_updater.py -a allow.txt -r remove.txt"
    )
    parser.add_argument(
        "-a", "--allow-list",
        required=True,
        help="Ruta al archivo con la lista de IPs permitidas."
    )
    parser.add_argument(
        "-r", "--remove-list",
        required=True,
        help="Ruta al archivo con las IPs a eliminar."
    )
    parser.add_argument(
        "-o", "--output",
        help="Opcional: Ruta al archivo de salida. Si no se proporciona, se sobrescribe el archivo de permitidos."
    )

    args = parser.parse_args()

    success = update_file(args.allow_list, args.remove_list, args.output)

    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
