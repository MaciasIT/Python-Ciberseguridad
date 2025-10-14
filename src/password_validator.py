# src/password_validator.py

# Lista de contraseñas comunes que siempre se considerarán débiles.
# En una aplicación real, esta lista sería mucho más grande.
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "12345678"]

def validate_password_strength(password):
    """
    Valida la fortaleza de una contraseña basado en su longitud y composición.
    
    Args:
        password (str): La contraseña a validar.
        
    Returns:
        str: El nivel de fortaleza ("Débil", "Media", "Fuerte").
    """
    # Criterio 1: ¿Es una contraseña común?
    # Usamos .lower() para que no distinga mayúsculas (ej: "Password" también sea débil)
    if password.lower() in COMMON_PASSWORDS:
        return "Débil"

    # Criterio 2: ¿Es demasiado corta?
    if len(password) < 8:
        return "Débil"

    # Criterios para "Fuerte": longitud, mayúsculas y números
    has_upper = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
            
    if len(password) >= 8 and has_upper and has_digit:
        return "Fuerte"
    
    # Si no es ni Débil ni Fuerte, es Media
    return "Media"