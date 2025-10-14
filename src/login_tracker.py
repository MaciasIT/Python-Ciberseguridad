# src/login_tracker.py
import logging

# Realizamos una configuración básica del logging a nivel de módulo.
# Esto asegura que los mensajes de log se muestren en la consola.
# En una aplicación real, esta configuración sería más compleja y centralizada.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LoginTracker:
    """
    Una clase para rastrear los intentos de inicio de sesión y bloquear usuarios.
    """
    # Constante que define el número máximo de intentos fallidos permitidos.
    MAX_ATTEMPTS = 3

    def __init__(self):
        """
        Inicializador de la clase.
        Crea un diccionario vacío para almacenar los intentos por usuario.
        La estructura será: {'username': {'attempts': count, 'locked': False}}
        """
        self.user_attempts = {}

    def record_attempt(self, username):
        """
        Registra un intento de inicio de sesión para un usuario específico.

        Si el usuario no existe en nuestro registro, lo añade.
        Si el usuario ya existe, incrementa su contador de intentos.
        """
        # Si es la primera vez que vemos a este usuario, lo inicializamos.
        if username not in self.user_attempts:
            self.user_attempts[username] = {'attempts': 0, 'locked': False}
        
        # No registrar más intentos si la cuenta ya está bloqueada.
        if self.user_attempts[username]['attempts'] > self.MAX_ATTEMPTS:
            returnsi

        # Incrementamos el contador de intentos.
        self.user_attempts[username]['attempts'] += 1
        logging.warning(f"Intento de login fallido para el usuario: {username}")

        # Comprobar si este intento causa el bloqueo y registrarlo.
        if self.user_attempts[username]['attempts'] > self.MAX_ATTEMPTS:
            logging.critical(f"Cuenta bloqueada por exceso de intentos para el usuario: {username}")

    def get_attempts(self, username):
        """
        Devuelve el número de intentos para un usuario.
        Si el usuario no existe, devuelve 0.
        """
        return self.user_attempts.get(username, {'attempts': 0})['attempts']

    def is_locked(self, username):
        """
        Comprueba si una cuenta de usuario está bloqueada.
        Un usuario está bloqueado si ha superado el número máximo de intentos.
        """
        # Si el usuario no existe, no está bloqueado.
        if username not in self.user_attempts:
            return False
            
        # Comprueba si los intentos superan el máximo permitido.
        return self.user_attempts[username]['attempts'] > self.MAX_ATTEMPTS