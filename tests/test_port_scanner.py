import unittest
from unittest.mock import patch, MagicMock
from src.port_scanner import scan_port, scan_ports

class TestPortScanner(unittest.TestCase):

    @patch('src.port_scanner.socket.socket')
    def test_scan_port_open(self, mock_socket_cls):
        # Configurar el mock para simular un puerto abierto (connect_ex devuelve 0)
        mock_socket = MagicMock()
        mock_socket.connect_ex.return_value = 0
        mock_socket_cls.return_value = mock_socket

        result = scan_port('127.0.0.1', 80)
        self.assertTrue(result)
        mock_socket.connect_ex.assert_called_with(('127.0.0.1', 80))

    @patch('src.port_scanner.socket.socket')
    def test_scan_port_closed(self, mock_socket_cls):
        # Configurar el mock para simular un puerto cerrado (connect_ex devuelve != 0)
        mock_socket = MagicMock()
        mock_socket.connect_ex.return_value = 111 # Connection refused
        mock_socket_cls.return_value = mock_socket

        result = scan_port('127.0.0.1', 80)
        self.assertFalse(result)

    @patch('src.port_scanner.scan_port')
    def test_scan_ports(self, mock_scan_port):
        # Simular que el puerto 80 está abierto y el 443 cerrado
        mock_scan_port.side_effect = [True, False]

        target_ip = '192.168.1.1'
        ports_to_scan = [80, 443]

        open_ports = scan_ports(target_ip, ports_to_scan)

        self.assertEqual(open_ports, [80])
        self.assertEqual(mock_scan_port.call_count, 2)

if __name__ == '__main__':
    unittest.main()
