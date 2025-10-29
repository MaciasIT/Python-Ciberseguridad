import unittest
import os
import sys

# Añadimos el directorio raíz al path para poder importar 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.log_parser import parse_log_line

class TestLogParser(unittest.TestCase):
    """
    Pruebas para el analizador de líneas de log.
    """

    def test_parse_valid_log_line(self):
        """Prueba si una línea de log con formato correcto se analiza bien."""
        log_line = "[2025-10-29 22:10:05] - ERROR - Failed login attempt"
        expected = {'timestamp': '2025-10-29 22:10:05', 'level': 'ERROR', 'message': 'Failed login attempt'}
        self.assertEqual(parse_log_line(log_line), expected)

    def test_parse_info_level(self):
        """Prueba un nivel de log diferente."""
        log_line = "[2025-10-29 22:11:00] - INFO - User 'admin' logged out."
        expected = {'timestamp': '2025-10-29 22:11:00', 'level': 'INFO', 'message': "User 'admin' logged out."}
        self.assertEqual(parse_log_line(log_line), expected)

    def test_parse_invalid_log_line(self):
        """Prueba si una línea sin el formato correcto devuelve None."""
        log_line = "This is not a valid log line"
        self.assertIsNone(parse_log_line(log_line))

    def test_parse_empty_string(self):
        """Prueba si una cadena vacía devuelve None."""
        self.assertIsNone(parse_log_line(""))

if __name__ == '__main__':
    unittest.main()
