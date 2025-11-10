# -*- coding: utf-8 -*-

"""
Este script genera IDs de empleado únicos para el departamento de Ventas
basándose en un conjunto de reglas específicas.
"""

def generar_ids_empleado():
    """
    Genera una lista de IDs de empleado únicos para el departamento de Ventas.
    
    Estos IDs son números enteros en el rango de 5000 a 5150 (ambos inclusive)
    que son divisibles por 5. La generación de IDs predecibles y con un formato
    específico es crucial en ciberseguridad para:
    - Facilitar la auditoría y el seguimiento de accesos.
    - Implementar políticas de control de acceso basadas en roles (RBAC)
      donde ciertos rangos de IDs pueden corresponder a diferentes niveles
      de privilegio.
    - Detectar anomalías o intentos de creación de IDs fuera de las políticas.

    Returns:
        list[int]: Una lista de números enteros, donde cada entero es un ID de empleado.
                   La lista estará ordenada de forma ascendente.
    """
    # Iniciamos el primer número a evaluar, que es el límite inferior del rango.
    id_actual = 5000
    ids_generados = []

    # Iteramos a través del rango de IDs potenciales (5000 a 5150).
    # Este enfoque asegura que todos los posibles IDs dentro del rango definido
    # sean evaluados, lo cual es importante para mantener la integridad
    # y la previsibilidad en la asignación de identificadores.
    while id_actual <= 5150:
        # Verificamos si el número actual es divisible por 5.
        # La divisibilidad por 5 actúa como una regla de negocio para la
        # asignación de IDs, lo que podría indicar una segmentación
        # o categorización específica dentro del sistema de gestión de empleados.
        # En ciberseguridad, estas reglas ayudan a definir patrones esperados
        # y a detectar desviaciones.
        if id_actual % 5 == 0:
            # Si cumple la condición, el ID se considera válido y se añade a la lista.
            # La unicidad y el cumplimiento de las reglas son fundamentales
            # para evitar colisiones de IDs y asegurar que cada empleado
            # tenga una identidad digital clara y auditable.
            ids_generados.append(id_actual)
        
        # Incrementamos para evaluar el siguiente número en la secuencia.
        id_actual += 1
    
    return ids_generados

# Este bloque solo se ejecuta si el script es llamado directamente (ej: python generador_id_empleado.py)
# No se ejecutará si es importado desde otro módulo.
if __name__ == "__main__":
    print("Generando IDs de empleado para el departamento de Ventas...")
    
    # Llamamos a la función que contiene la lógica.
    lista_ids = generar_ids_empleado()
    
    # Imprimimos los resultados.
    for id_empleado in lista_ids:
        print(f"Nuevo ID de empleado creado: {id_empleado}")

    print("\nProceso completado.")
    print(f"Total de IDs generados: {len(lista_ids)}")
    print("IDs finales:", lista_ids)
