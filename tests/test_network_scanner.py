import unittest
from unittest.mock import patch, MagicMock
from src.network_scanner import ping_ip, scan_network

class TestNetworkScanner(unittest.TestCase):

    @patch('src.network_scanner.subprocess.run')
    def test_ping_ip_success(self, mock_run):
        # Simular que ping devuelve código 0 (éxito)
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_run.return_value = mock_result
        
        self.assertTrue(ping_ip("192.168.1.1"))

    @patch('src.network_scanner.subprocess.run')
    def test_ping_ip_failure(self, mock_run):
        # Simular que ping devuelve código 1 (fallo)
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_run.return_value = mock_result
        
        self.assertFalse(ping_ip("192.168.1.999"))

    @patch('src.network_scanner.ping_ip')
    def test_scan_network(self, mock_ping_ip):
        # Simular una red pequeña donde solo la .1 y la .5 responden
        # El side_effect debe cubrir las llamadas. 
        # Como scan_network escanea 254 IPs, necesitamos una función dinámica
        
        def side_effect(ip):
            if ip.endswith(".1") or ip.endswith(".5"):
                return True
            return False
            
        mock_ping_ip.side_effect = side_effect
        
        # Ejecutar scan
        active_hosts = scan_network("192.168.1", max_workers=10)
        
        self.assertIn("192.168.1.1", active_hosts)
        self.assertIn("192.168.1.5", active_hosts)
        self.assertNotIn("192.168.1.2", active_hosts)

if __name__ == '__main__':
    unittest.main()
