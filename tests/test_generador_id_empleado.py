# tests/test_generador_id_empleado.py
import unittest
import sys
import os

# Añadimos el directorio 'src' a la ruta para poder importar nuestros módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importamos la función que vamos a probar
from generador_id_empleado import generar_ids_empleado

class TestGeneradorIdEmpleado(unittest.TestCase):
    """
    Suite de pruebas para el generador de IDs de empleado.
    """

    def setUp(self):
        """Este método se ejecuta antes de cada prueba para generar los IDs."""
        self.ids_generados = generar_ids_empleado()

    def test_numero_de_ids_generados(self):
        """
        Verifica que la función genera la cantidad correcta de IDs.
        
        El rango es de 5000 a 5150, inclusive. Los números divisibles por 5 en este
        rango son 31 en total. ( (5150 - 5000) / 5 + 1 )
        """
        # 1. Preparación (Arrange)
        cantidad_esperada = 31

        # 2. Actuación (Act)
        cantidad_real = len(self.ids_generados)

        # 3. Afirmación (Assert)
        self.assertEqual(cantidad_real, cantidad_esperada, 
                         f"Se esperaban {cantidad_esperada} IDs, pero se generaron {cantidad_real}.")

    def test_contenido_y_rango_de_ids(self):
        """
        Verifica que todos los IDs generados son correctos, están en el rango
        y son divisibles por 5.
        """
        # 1. Preparación (Arrange)
        id_inicial_esperado = 5000
        id_final_esperado = 5150

        # 2. Afirmación (Assert)
        # Verifica el primer y último elemento
        self.assertEqual(self.ids_generados[0], id_inicial_esperado, "El primer ID generado no es el esperado.")
        self.assertEqual(self.ids_generados[-1], id_final_esperado, "El último ID generado no es el esperado.")

        # Verifica que todos los IDs en la lista son divisibles por 5
        for id_empleado in self.ids_generados:
            self.assertEqual(id_empleado % 5, 0, 
                             f"El ID {id_empleado} no es divisible por 5, pero debería serlo.")
            self.assertTrue(5000 <= id_empleado <= 5150,
                            f"El ID {id_empleado} está fuera del rango esperado [5000, 5150].")

if __name__ == '__main__':
    unittest.main()
