import unittest
from src.ip_analyzer import analyze_ips

class TestIpAnalyzer(unittest.TestCase):
    """
    Pruebas para la función de análisis de IPs.
    """

    def test_analyze_ips_scenario_1(self):
        """
        Prueba un escenario básico:
        - Una lista de IPs en crudo con duplicados.
        - Una blacklist.
        - Debería devolver una lista ordenada y sin duplicados de las IPs maliciosas encontradas.
        """
        # 1. Arrange (Preparar)
        raw_ips = [
            "203.0.113.5",
            "198.51.100.22",
            "203.0.113.5",
            "203.0.113.45",
            "198.51.100.22",
            "203.0.113.5",
            "192.168.1.101"
        ]
        blacklist = ["203.0.113.5", "198.51.100.22", "99.99.99.99"]

        # El resultado esperado es una lista de las IPs que están en ambas listas,
        # sin duplicados y ordenada.
        expected_result = ["198.51.100.22", "203.0.113.5"]

        # 2. Act (Actuar)
        actual_result = analyze_ips(raw_ips, blacklist)

        # 3. Assert (Afirmar)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
