# tests/test_login_tracker.py
import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Ahora importaremos una clase que aún no hemos creado.
from login_tracker import LoginTracker

class TestLoginTracker(unittest.TestCase):
    """
    Suite de pruebas para la clase LoginTracker.
    """

    def setUp(self): 
        """
        Este método especial se ejecuta ANTES de cada prueba.
        Crea una nueva instancia de LoginTracker para asegurar que las pruebas estén aisladas entre sí.
        """
        self.tracker = LoginTracker()
        self.username = "j.doe"

    def test_record_and_get_attempts(self):
        """
        Verifica que los intentos de un usuario se registran y recuperan correctamente.
        """
        # Actuación: Registramos dos intentos para un usuario.
        self.tracker.record_attempt(self.username)
        self.tracker.record_attempt(self.username)

        # Afirmación: Verificamos que el número de intentos es 2.
        self.assertEqual(self.tracker.get_attempts(self.username), 2)

    def test_lockout_after_max_attempts(self):
        """
        Verifica que un usuario es bloqueado después de superar el número máximo de intentos.
        """
        # Actuación: Simulamos N intentos fallidos, donde N es el máximo permitido.
        # Usamos un bucle para registrar el número máximo de intentos.
        for _ in range(self.tracker.MAX_ATTEMPTS):
            self.tracker.record_attempt(self.username)

        # Afirmación: El usuario aún no debería estar bloqueado.
        self.assertFalse(self.tracker.is_locked(self.username),
                         f"El usuario no debería estar bloqueado con solo {self.tracker.MAX_ATTEMPTS} intentos.")

        # Actuación: Un intento más debería bloquear al usuario.
        self.tracker.record_attempt(self.username)

        # Afirmación: Ahora el usuario SÍ debe estar bloqueado.
        self.assertTrue(self.tracker.is_locked(self.username),
                        "El usuario debería estar bloqueado después de superar los intentos máximos.")

    @patch('login_tracker.logging')
    def test_logging_on_failed_attempt(self, mock_logging):
        """Verifica que se registra un log de advertencia en cada intento fallido."""
        # Actuación
        self.tracker.record_attempt(self.username)
        # Afirmación
        mock_logging.warning.assert_called_with(f"Intento de login fallido para el usuario: {self.username}")

    @patch('login_tracker.logging')
    def test_logging_on_account_lockout(self, mock_logging):
        """Verifica que se registra un log CRÍTICO cuando una cuenta se bloquea."""
        # Actuación: Superamos el límite de intentos para provocar el bloqueo.
        for _ in range(self.tracker.MAX_ATTEMPTS + 1):
            self.tracker.record_attempt(self.username)

        # Afirmación: Verificamos que se llamó al log crítico con el mensaje esperado.
        mock_logging.critical.assert_called_with(f"Cuenta bloqueada por exceso de intentos para el usuario: {self.username}")

if __name__ == '__main__':
    unittest.main()