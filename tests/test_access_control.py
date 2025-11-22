import unittest
import os
import tempfile
from src.access_control import update_server_access_list

class TestAccessControl(unittest.TestCase):
    """
    Pruebas unitarias para el módulo de control de acceso.
    """

    def setUp(self):
        """
        Configuración previa a cada prueba.
        Creamos un archivo temporal con datos de prueba para no afectar archivos reales.
        """
        # Datos de prueba iniciales
        self.initial_ips = "192.168.1.1 192.168.1.2 192.168.1.3 192.168.1.4 192.168.1.5"
        
        # Crear un archivo temporal
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.test_file.write(self.initial_ips)
        self.test_file.close() # Cerramos para que la función pueda abrirlo

    def tearDown(self):
        """
        Limpieza después de cada prueba.
        Eliminamos el archivo temporal.
        """
        os.remove(self.test_file.name)

    def test_remove_single_ip(self):
        """Prueba la eliminación de una única IP."""
        ips_to_remove = ["192.168.1.3"]
        update_server_access_list(self.test_file.name, ips_to_remove)

        with open(self.test_file.name, 'r') as f:
            content = f.read()
        
        expected_content = "192.168.1.1 192.168.1.2 192.168.1.4 192.168.1.5"
        self.assertEqual(content, expected_content)

    def test_remove_multiple_ips(self):
        """Prueba la eliminación de múltiples IPs, incluyendo adyacentes (caso crítico)."""
        # Este caso fallaría con el código original del lab debido al bug de iteración
        ips_to_remove = ["192.168.1.2", "192.168.1.3"] 
        update_server_access_list(self.test_file.name, ips_to_remove)

        with open(self.test_file.name, 'r') as f:
            content = f.read()
        
        expected_content = "192.168.1.1 192.168.1.4 192.168.1.5"
        self.assertEqual(content, expected_content)

    def test_remove_non_existent_ip(self):
        """Prueba que intentar eliminar una IP que no existe no rompe nada."""
        ips_to_remove = ["10.0.0.1"] # No está en la lista
        update_server_access_list(self.test_file.name, ips_to_remove)

        with open(self.test_file.name, 'r') as f:
            content = f.read()
        
        # El contenido no debe cambiar
        self.assertEqual(content, self.initial_ips)

    def test_file_not_found(self):
        """Prueba que se lance la excepción correcta si el archivo no existe."""
        with self.assertRaises(FileNotFoundError):
            update_server_access_list("archivo_fantasma.txt", [])

if __name__ == '__main__':
    unittest.main()
