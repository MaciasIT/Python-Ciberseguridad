#!/usr/bin/env python3
"""
detect_patterns_cli.py
Interfaz de línea de comandos para el detector de patrones de IoCs.
"""

import argparse
import sys
from pathlib import Path

# Añadimos el directorio padre al path para poder importar 'src'
# Esto es necesario para ejecutar el script directamente.
sys.path.append(str(Path(__file__).resolve().parent.parent))

try:
    from src.pattern_detector import analyze_text, load_flagged_list, generate_report
except ImportError:
    print("Error: No se pudo importar el módulo 'pattern_detector' desde 'src'.")
    print("Asegúrate de que el entorno y el PYTHONPATH están configurados correctamente.")
    sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="detect_patterns_cli.py",
        description="Detecta patrones comunes (IoCs) en archivos de log."
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        help="Archivo de log de entrada (ej: data/sample_log.txt)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        required=False,
        help="Archivo de reporte de salida (opcional)"
    )
    parser.add_argument(
        "-f", "--flagged",
        type=Path,
        required=False,
        help="Archivo con IPs marcadas, una por línea (ej: data/flagged.txt)"
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: El archivo de entrada no se encuentra en '{args.input}'")
        sys.exit(1)

    print(f"--- Analizando archivo: {args.input} ---")
    
    text = args.input.read_text(encoding='utf-8', errors='ignore')
    results = analyze_text(text)

    flagged_ips = []
    if args.flagged:
        if not args.flagged.exists():
            print(f"Advertencia: El archivo de IPs marcadas no se encuentra en '{args.flagged}'")
        else:
            flagged_ips = load_flagged_list(args.flagged)

    report = generate_report(results, flagged=flagged_ips)

    print(report)

    if args.output:
        args.output.write_text(report, encoding='utf-8')
        print(f"\n--- Reporte guardado en: {args.output} ---")

if __name__ == '__main__':
    main()
