# tests/test_ip_validator.py
import unittest
from unittest.mock import patch
import sys
import os

# Añadimos el directorio 'src' a la ruta para poder importar nuestros módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importamos las funciones que vamos a probar
from ip_validator import filter_allowed_ips, check_ips_until_fail

class TestIpValidator(unittest.TestCase):
    """
    Suite de pruebas para el validador de direcciones IP.
    """

    def setUp(self):
        """Este método se ejecuta antes de cada prueba."""
        self.allow_list = ["192.168.86.232", "192.168.205.12"]
        self.ip_addresses = ["192.168.86.232", "192.168.142.245", "192.168.205.12"]

    def test_filter_allowed_ips(self):
        """
        Verifica que la función filtra correctamente las IPs permitidas.
        """
        # 1. Preparación (Arrange)
        # Nota: La lista de IPs de prueba es diferente a la de setUp para este test específico.
        test_ips = ["192.168.142.245", "192.168.86.232", "192.168.131.147", "192.168.205.12"]
        expected_allowed_ips = ["192.168.86.232", "192.168.205.12"]

        # 2. Actuación (Act)
        actual_allowed_ips = filter_allowed_ips(test_ips, self.allow_list)

        # 3. Afirmación (Assert)
        self.assertEqual(actual_allowed_ips, expected_allowed_ips, "La lista de IPs permitidas no coincide con la esperada.")

    def test_check_ips_until_fail_stops_on_denied(self):
        """
        Verifica que la función se detiene al encontrar la primera IP no permitida.
        """
        # Creamos una lista para registrar las IPs que la función procesa.
        processed_ips = []

        # La función que probaremos aceptará otra función (un 'callback') para registrar su progreso.
        def record_processed_ip(ip):
            processed_ips.append(ip)

        # Actuación: Ejecutamos la función.
        check_ips_until_fail(self.ip_addresses, self.allow_list, record_processed_ip)

        # Afirmación: Verificamos que solo la primera IP (que está permitida) fue procesada.
        # No debería haber procesado la segunda IP, que no está en la lista de permitidos.
        self.assertEqual(processed_ips, ["192.168.86.232"])

if __name__ == '__main__':
    unittest.main()
