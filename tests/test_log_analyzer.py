# tests/test_log_analyzer.py
import unittest
import sys
import os

# Añadimos el directorio 'src' a la ruta para poder importar nuestros módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importamos las funciones que vamos a probar
from log_analyzer import extract_ips_from_log, process_log_queue

class TestLogAnalyzer(unittest.TestCase):
    """
    Suite de pruebas para el analizador de logs.
    """

    def test_extract_ips_from_log(self):
        """
        Verifica que la función extrae correctamente una lista de IPs de un log.
        """
        # 1. Preparación (Arrange)
        # Simulamos un archivo de log con una cadena de texto multilínea.
        sample_log = """
        [2025-10-14 10:00:01] - INFO - User 'admin' logged in successfully.
        [2025-10-14 10:05:15] - ERROR - Failed login attempt from 192.168.1.100
        [2025-10-14 10:05:18] - ERROR - Failed login attempt from 10.0.0.5
        [2025-10-14 10:06:00] - WARNING - High CPU usage detected.
        [2025-10-14 10:07:21] - ERROR - Failed login attempt from 192.168.1.100
        """
        expected_ips = ["192.168.1.100", "10.0.0.5", "192.168.1.100"]

        # 2. Actuación (Act)
        actual_ips = extract_ips_from_log(sample_log)

        # 3. Afirmación (Assert)
        self.assertEqual(actual_ips, expected_ips, "La lista de IPs extraídas no coincide con la esperada.")

    def test_stops_on_system_compromised(self):
        """
        Verifica que el bucle se detiene con 'break' si encuentra una alerta crítica.
        """
        # 1. Preparación
        sample_log = """
        [2025-10-14 11:00:00] - ERROR - Failed login attempt from 192.168.1.100
        [2025-10-14 11:01:00] - CRITICAL - SYSTEM_COMPROMISED
        [2025-10-14 11:02:00] - ERROR - Failed login attempt from 8.8.8.8
        """
        # La IP 8.8.8.8 no debería ser incluida porque está después de la alerta crítica.
        expected_ips = ["192.168.1.100"]

        # 2. Actuación
        actual_ips = extract_ips_from_log(sample_log)

        # 3. Afirmación
        self.assertEqual(actual_ips, expected_ips, "El análisis debería detenerse al encontrar SYSTEM_COMPROMISED.")

    def test_process_log_queue_with_while(self):
        """
        Verifica que la función con bucle 'while' procesa una cola de logs.
        """
        # 1. Preparación
        log_queue = [
            "[2025-10-14 12:00:00] - ERROR - Failed login attempt from 1.1.1.1",
            "[2025-10-14 12:01:00] - INFO - Service started.",
            "[2025-10-14 12:02:00] - ERROR - Failed login attempt from 2.2.2.2"
        ]
        expected_ips = ["1.1.1.1", "2.2.2.2"]

        # 2. Actuación
        actual_ips = process_log_queue(log_queue)

        # 3. Afirmación
        self.assertEqual(actual_ips, expected_ips)
        # Verificamos también que la cola original ha sido vaciada.
        self.assertEqual(len(log_queue), 0, "La cola de logs debería estar vacía después de procesarla.")

if __name__ == '__main__':
    unittest.main()