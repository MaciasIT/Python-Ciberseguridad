# -*- coding: utf-8 -*-
"""
Pruebas para el módulo de demostración de depuración (debugging_showcase).

Estas pruebas están diseñadas para ilustrar cómo el Desarrollo Guiado por Pruebas (TDD)
actúa como una herramienta fundamental para detectar errores lógicos y excepciones.
"""

import unittest
from src.debugging_showcase import control_acceso_fallido, analizar_ioc

class TestDebuggingShowcase(unittest.TestCase):

    def test_error_logico_en_control_de_acceso(self):
        """
        Esta prueba está diseñada para FALLAR y así demostrar el error lógico.
        
        La política de seguridad dicta que el acceso debe ser bloqueado en el 5º intento.
        La prueba comprueba que `control_acceso_fallido(5)` devuelve False (acceso bloqueado).
        Sin embargo, debido al error lógico (`> 5` en lugar de `>= 5`), la función
        devolverá True, haciendo que esta prueba falle y revele la vulnerabilidad.
        """
        print("\nEjecutando prueba de error lógico... (se espera que falle)")
        # La aserción correcta según los requisitos de seguridad
        self.assertFalse(
            control_acceso_fallido(5),
            "FALLO DE SEGURIDAD: El sistema debería bloquear en el 5º intento, pero no lo hizo."
        )

    def test_excepcion_al_analizar_ioc_incompleto(self):
        """
        Verifica que la función `analizar_ioc` lanza una excepción `KeyError`
        cuando recibe un diccionario sin la clave 'severidad'.
        
        Esto demuestra cómo las pruebas pueden asegurar que el código maneja
        correctamente los datos inesperados o malformados, previniendo caídas
        inesperadas del programa.
        """
        print("\nEjecutando prueba de manejo de excepción...")
        ioc_incompleto = {"tipo": "ip", "valor": "198.51.100.10"}
        
        # Verificamos que al llamar a la función con datos incompletos,
        # se lanza la excepción esperada (KeyError).
        with self.assertRaises(KeyError) as contexto:
            analizar_ioc(ioc_incompleto)
        
        # Opcionalmente, podemos verificar el mensaje de la excepción
        self.assertEqual(str(contexto.exception), "'severidad'")
        print("Prueba de excepción superada: KeyError capturada correctamente.")

if __name__ == '__main__':
    unittest.main()
