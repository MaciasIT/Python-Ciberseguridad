
import unittest
import os
import sys

# Añadimos el directorio 'src' al path para que Python pueda encontrar nuestro módulo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from access_list_updater import update_file

class TestAccessListUpdater(unittest.TestCase):
    """
    Conjunto de pruebas para el script access_list_updater.py.
    """

    def setUp(self):
        """
        Configura el entorno para cada prueba. Crea archivos temporales.
        """
        self.allow_file = 'test_allow_list.txt'
        self.remove_file = 'test_remove_list.txt'
        self.output_file = 'test_output_list.txt'

        # Contenido inicial de la lista de permitidos
        with open(self.allow_file, 'w') as f:
            f.write("""192.168.1.1
10.0.0.1
172.16.0.1
192.168.1.2""")

        # IPs a eliminar
        with open(self.remove_file, 'w') as f:
            f.write("""10.0.0.1
192.168.1.2""")

    def tearDown(self):
        """
        Limpia el entorno después de cada prueba. Elimina los archivos temporales.
        """
        for f in [self.allow_file, self.remove_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_successful_removal(self):
        """
        Prueba que las IPs se eliminan correctamente y el archivo original se sobrescribe.
        """
        result = update_file(self.allow_file, self.remove_file)
        self.assertTrue(result)

        with open(self.allow_file, 'r') as f:
            content = f.read().split()

        expected_content = ['192.168.1.1', '172.16.0.1']
        self.assertEqual(content, expected_content)

    def test_no_removals_needed(self):
        """
        Prueba que el archivo no se modifica si no hay IPs coincidentes.
        """
        # Creamos un archivo de eliminación sin coincidencias
        with open(self.remove_file, 'w') as f:
            f.write("""8.8.8.8
1.1.1.1""")

        result = update_file(self.allow_file, self.remove_file)
        self.assertTrue(result)

        with open(self.allow_file, 'r') as f:
            content = f.read().split()

        original_content = ['192.168.1.1', '10.0.0.1', '172.16.0.1', '192.168.1.2']
        self.assertEqual(content, original_content)

    def test_save_to_new_output_file(self):
        """
        Prueba que la salida se guarda en un nuevo archivo sin modificar el original.
        """
        result = update_file(self.allow_file, self.remove_file, self.output_file)
        self.assertTrue(result)

        # Verificar el nuevo archivo de salida
        with open(self.output_file, 'r') as f:
            content = f.read().split()
        expected_content = ['192.168.1.1', '172.16.0.1']
        self.assertEqual(content, expected_content)

        # Verificar que el archivo original no ha cambiado
        with open(self.allow_file, 'r') as f:
            original_content = f.read().split()
        self.assertNotEqual(original_content, expected_content)

    def test_file_not_found_error(self):
        """
        Prueba que la función devuelve False si un archivo de entrada no existe.
        """
        result = update_file('non_existent_file.txt', self.remove_file)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
