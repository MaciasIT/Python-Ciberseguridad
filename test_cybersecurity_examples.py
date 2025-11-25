import unittest
from cybersecurity_examples import (
    filter_ips_from_log,
    extract_usernames,
    hex_to_int
)

class TestCybersecurityExamples(unittest.TestCase):

    def test_filter_ips_from_log(self):
        """Prueba la extracción de IPs de líneas de log."""
        logs = [
            'INFO: Conexión exitosa desde 192.168.1.100',
            'WARN: Intento de acceso fallido desde 10.0.0.5 a las 14:30',
            'ERROR: Host 256.0.0.1 no válido',
            'DEBUG: Paquete recibido de 8.8.8.8'
        ]
        expected_ips = ['192.168.1.100', '10.0.0.5', '8.8.8.8']
        self.assertEqual(filter_ips_from_log(logs), expected_ips)

    def test_extract_usernames(self):
        """Prueba la extracción de nombres de usuario de emails."""
        emails = [
            'john.doe@example.com',
            'admin@internal.net',
            'invalid-email',
            'jane_doe@example.com'
        ]
        expected_users = ['john.doe', 'admin', 'jane_doe']
        self.assertEqual(extract_usernames(emails), expected_users)

    def test_hex_to_int(self):
        """Prueba la conversión de cadenas hexadecimales a enteros."""
        hex_values = ['0x1a', '0xff', '0x100', '0x0']
        expected_ints = [26, 255, 256, 0]
        self.assertEqual(hex_to_int(hex_values), expected_ints)

if __name__ == '__main__':
    unittest.main()
