# Tutorial Práctico: Procesando Listas de IPs

Ahora que hemos explorado la teoría en la [Guía Profunda sobre Listas](./guia-profunda-listas.md), vamos a aplicar esas habilidades en un escenario práctico y comñn en ciberseguridad: analizar una lista de direcciones IP extraídas de un log.

## El Escenario

Un script de monitoreo nos ha entregado una lista "en crudo" de direcciones IP que han mostrado un comportamiento sospechoso. La lista contiene duplicados. Nuestra misión es:

1.  Limpiar la lista para tener solo IPs ónicas.
2.  Comparar estas IPs ónicas contra una `blacklist` de atacantes conocidos.
3.  Generar un reporte final con las IPs maliciosas que hemos encontrado en nuestros logs.

---

### Paso 1: La Lista de IPs en Crudo

Empezamos con la lista que nos ha llegado. Fíjate que hay varias IPs repetidas.

```python
# Lista extraída de un log de accesos fallidos
raw_ips = [
    "203.0.113.5",
    "198.51.100.22",
    "203.0.113.5",
    "203.0.113.45",
    "198.51.100.22",
    "203.0.113.5",
    "192.168.1.101" # Una IP interna, probablemente un falso positivo
]
```

### Paso 2: Eliminando Duplicados (El Truco del `set`)

Como vimos en la guía de estructuras de datos, los conjuntos (`set`) solo almacenan elementos ónicos. La forma más "pythónica" y eficiente de eliminar duplicados de una lista es convertirla a un conjunto y luego de nuevo a una lista.

```python
# Convertimos la lista a un conjunto para eliminar duplicados
unique_ips_set = set(raw_ips)

# Convertimos el conjunto de vuelta a una lista para poder ordenarla y usarla después
unique_ips = list(unique_ips_set)

# Opcional: Ordenamos la lista para que sea más fácil de leer
unique_ips.sort()

print(f"IPs ónicas encontradas: {unique_ips}")
# Salida: IPs ónicas encontradas: ['192.168.1.101', '198.51.100.22', '203.0.113.45', '203.0.113.5']
```

### Paso 3: La Blacklist y la Magia de las List Comprehensions

Ahora tenemos nuestra lista limpia. El siguiente paso es compararla con nuestra `blacklist` de atacantes conocidos. Para esta tarea, una **list comprehension** es la herramienta perfecta: es concisa, legible y eficiente.

```python
# Blacklist de IPs conocidas por actividades maliciosas
blacklist = ["203.0.113.5", "198.51.100.22", "99.99.99.99"]

# Usamos una list comprehension para filtrar nuestras IPs ónicas
# La lógica es: "Crea una nueva lista con las IPs que estén tanto en nuestra
# lista de ónicas como en la blacklist"
malicious_ips_found = [ip for ip in unique_ips if ip in blacklist]
```

La línea `[ip for ip in unique_ips if ip in blacklist]` es el corazón de nuestro análisis. Reemplaza un bucle `for` completo en una sola línea.

### Paso 4: Generando el Reporte Final

Finalmente, presentamos los resultados. Usamos un condicional para mostrar un mensaje diferente si hemos encontrado amenazas o no.

```python
if malicious_ips_found: # Si la lista no está vacía (es "Truthy")
    print("\n--- ¡ALERTA DE SEGURIDAD! ---")
    print("Se encontraron las siguientes IPs maliciosas en los logs:")
    for ip in malicious_ips_found:
        print(f"- {ip}")
else:
    print("\n--- Análisis completado ---")
    print("No se encontraron IPs de la blacklist en los logs.")
```

---

## Código Completo del Script

Aquí tienes el script completo para que lo pruebes.

```python
# main_analyzer.py

# 1. Datos iniciales
raw_ips = [
    "203.0.113.5", "198.51.100.22", "203.0.113.5",
    "203.0.113.45", "198.51.100.22", "203.0.113.5",
    "192.168.1.101"
]

blacklist = ["203.0.113.5", "198.51.100.22", "99.99.99.99"]

print("--- Iniciando análisis de IPs ---")

# 2. Limpiar duplicados
unique_ips = list(set(raw_ips))
unique_ips.sort()

print(f"IPs ónicas a analizar: {unique_ips}")

# 3. Filtrar contra la blacklist
malicious_ips_found = [ip for ip in unique_ips if ip in blacklist]

# 4. Generar el reporte
if malicious_ips_found:
    print("\n--- ¡ALERTA DE SEGURIDAD! ---")
    print("Se encontraron las siguientes IPs maliciosas en los logs:")
    for ip in malicious_ips_found:
        print(f"- {ip}")
else:
    print("\n--- Análisis completado ---")
    print("No se encontraron IPs de la blacklist en los logs.")

print("\n--- Fin del script ---")
```

## Conclusión

¡Felicidades! Has completado un ciclo de análisis de datos muy realista. En este tutorial has aprendido a:

-   Usar el truco de `list(set(lista))` para obtener elementos ónicos.
-   Aplicar una **list comprehension** para filtrar datos de una lista basándote en otra.
-   Estructurar un script simple para generar un reporte final.

Estos patrones son la base para tareas mucho más complejas de análisis de logs y threat intelligence.
