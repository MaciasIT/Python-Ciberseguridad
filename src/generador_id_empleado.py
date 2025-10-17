# -*- coding: utf-8 -*-

"""
Este script genera IDs de empleado únicos para el departamento de Ventas
basándose en un conjunto de reglas específicas.
"""

# Iniciamos el primer número a evaluar, que es el límite inferior del rango.
id_actual = 5000

# Creamos una lista vacía para almacenar los IDs que ya han sido generados.
# Esto nos ayudará a asegurar que no haya duplicados, aunque en este caso
# el bucle garantiza la unicidad al ser secuencial.
ids_generados = []

print("Generando IDs de empleado para el departamento de Ventas...")

# Usamos un bucle '''while''' para iterar mientras el número de ID sea menor o igual a 5150.
# Esto nos permite recorrer todo el rango de números especificado.
while id_actual <= 5150:
    # Verificamos si el número actual es divisible por 5.
    # El operador de módulo (%) nos da el resto de una división.
    # Si el resto es 0, significa que el número es divisible exactamente.
    if id_actual % 5 == 0:
        # Si es divisible por 5, lo consideramos un ID de empleado válido.
        # Lo añadimos a nuestra lista de IDs generados.
        ids_generados.append(id_actual)
        
        # Mostramos el nuevo ID generado en la consola.
        print(f"Nuevo ID de empleado creado: {id_actual}")
    
    # Incrementamos el número actual en 1 para evaluar el siguiente número
    # en la próxima iteración del bucle.
    id_actual += 1

print("\nProceso completado.")
print(f"Total de IDs generados: {len(ids_generados)}")
print("IDs finales:", ids_generados)
