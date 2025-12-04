# -*- coding: utf-8 -*-
"""
Módulo de demostración para la guía de depuración.

Contiene funciones con errores intencionados (lógicos y de excepción)
para ilustrar conceptos de depuración en un contexto de ciberseguridad.
"""

# 1. Ejemplo de Error Lógico
def control_acceso_fallido(intentos):
    """
    Simula una política de control de acceso que debería bloquear una IP
    después de 5 intentos fallidos, pero contiene un error lógico.

    Args:
        intentos (int): El número de intentos de login fallidos.

    Returns:
        bool: True si el acceso está permitido, False si está bloqueado.
    """
    # ¡ERROR LÓGICO! La condición debería ser 'intentos >= 5'.
    # Con 'intentos > 5', el bloqueo solo ocurre en el sexto intento,
    # dando al atacante una oportunidad extra.
    if intentos > 5:
        print(f"[!] Acceso denegado. {intentos} intentos registrados. IP bloqueada.")
        return False
    
    print(f"[*] Acceso permitido. {intentos} intentos registrados.")
    return True


# 2. Ejemplo de Excepción (KeyError)
def analizar_ioc(datos_ioc):
    """
    Analiza un diccionario que representa un Indicador de Compromiso (IOC)
    y lanza una alerta si la severidad es 'alta'.

    Esta función es frágil y lanzará una KeyError si el diccionario de entrada
    no contiene la clave 'severidad'.

    Args:
        datos_ioc (dict): Un diccionario con información del IOC.

    Returns:
        str: Un mensaje indicando la acción tomada.
    """
    # El código asume que la clave 'severidad' siempre existirá.
    # Si no existe, Python lanzará una excepción 'KeyError' y el programa se detendrá.
    if datos_ioc['severidad'] == 'alta':
        mensaje = f"ALERTA: IOC de alta severidad detectado: {datos_ioc.get('valor', 'N/A')}"
        print(mensaje)
        return mensaje
    
    mensaje = f"INFO: IOC de severidad normal procesado: {datos_ioc.get('valor', 'N/A')}"
    print(mensaje)
    return mensaje


# 3. Ejemplo de Error de Sintaxis (para demostración, no se puede ejecutar)
# El siguiente bloque de código se deja comentado porque un error de sintaxis
# impediría que el intérprete de Python cargue este módulo.

# def es_ip_privada(ip_address):
#     segmentos_privados = ["10.", "192.168.", "172.16."]
#     for segmento in segmentos_privados
#         if ip_address.startswith(segmento):
#             return True
#     return False

# El error de sintaxis es la falta de dos puntos (:) en la línea del bucle 'for'.
# El intérprete mostraría: SyntaxError: expected ':'
