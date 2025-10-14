# tests/test_password_validator.py
import unittest
import sys
import os

# Añadimos el directorio 'src' a la ruta para poder importar nuestros módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importamos la función que vamos a probar (aún no existe)
from password_validator import validate_password_strength

class TestPasswordValidator(unittest.TestCase):
    """
    Suite de pruebas para el validador de fortaleza de contraseñas.
    """

    def test_short_password_is_weak(self):
        """
        Verifica que una contraseña corta (menos de 8 caracteres) se considera 'Débil'.
        """
        # 1. Preparación (Arrange)
        password = "12345"
        expected_strength = "Débil"

        # 2. Actuación (Act)
        actual_strength = validate_password_strength(password)

        # 3. Afirmación (Assert)
        self.assertEqual(actual_strength, expected_strength, "Una contraseña con menos de 8 caracteres debería ser 'Débil'")

    def test_strong_password_is_strong(self):
        """
        Verifica que una contraseña con longitud, mayúsculas y números es 'Fuerte'.
        """
        # 1. Preparación
        password = "Fuerte123"
        expected_strength = "Fuerte"

        # 2. Actuación
        actual_strength = validate_password_strength(password)

        # 3. Afirmación
        self.assertEqual(actual_strength, expected_strength, "Debería ser 'Fuerte' si tiene >= 8 caracteres, mayúsculas y números")

    def test_medium_password_is_medium(self):
        """
        Verifica que una contraseña que no es ni Débil ni Fuerte es 'Media'.
        """
        # 1. Preparación
        password = "sololetrasminusculas"
        expected_strength = "Media"

        # 2. Actuación
        actual_strength = validate_password_strength(password)

        # 3. Afirmación
        self.assertEqual(actual_strength, expected_strength, "Una contraseña larga pero simple debería ser 'Media'")

    def test_common_password_is_weak(self):
        """
        Verifica que una contraseña común (ej: 'password') es siempre 'Débil'.
        """
        # 1. Preparación
        password = "password"
        expected_strength = "Débil"

        # 2. Actuación
        actual_strength = validate_password_strength(password)

        # 3. Afirmación
        self.assertEqual(actual_strength, expected_strength, "Una contraseña común como 'password' siempre debería ser 'Débil'")

if __name__ == '__main__':
    unittest.main()