# Guía Detallada de Estructuras de Datos en Python

## ¿Qué es una Estructura de Datos?

Una estructura de datos es una forma especializada de organizar, almacenar y gestionar datos para que puedan ser accedidos y modificados eficientemente. Elegir la estructura correcta es crucial para escribir código limpio y de alto rendimiento.

Para un analista de seguridad, dominar las estructuras de datos significa poder modelar y resolver problemas complejos: desde contar la frecuencia de IPs en un log hasta almacenar las características de una pieza de malware.

---

## 1. Listas (`list`)

- **¿Qué son?** Colecciones ordenadas y mutables de elementos. Son el "caballo de batalla" de las colecciones en Python.
- **Características Clave:**
    - **Ordenadas:** Los elementos mantienen el orden en que fueron añadidos.
    - **Mutables:** Puedes añadir, eliminar o modificar elementos después de su creación.
    - **Permiten Duplicados:** Un mismo elemento puede aparecer varias veces.
- **Sintaxis:** Se definen con corchetes `[]`.

```python
# Lista de IPs a investigar
ips_a_escanear = ["192.168.1.1", "10.0.0.5", "192.168.1.1"]

# Añadir una nueva IP
ips_a_escanear.append("8.8.8.8")

# Eliminar la segunda IP
ips_a_escanear.pop(1)
```

### Casos de Uso en Ciberseguridad
- Almacenar una lista de puertos a escanear en un host.
- Guardar las líneas de un log que coinciden con un patrón de ataque.
- Mantener una lista de nombres de usuario que han fallado al iniciar sesión.

---

## 2. Tuplas (`tuple`)

- **¿Qué son?** Colecciones ordenadas e **inmutables** de elementos.
- **Características Clave:**
    - **Ordenadas:** Los elementos mantienen su orden.
    - **Inmutables:** Una vez creadas, no se pueden modificar. ¡Esto es clave para la integridad de los datos!
    - **Permiten Duplicados.**
- **Sintaxis:** Se definen con paréntesis `()`.

```python
# Registro de un evento de seguridad: (timestamp, ip, puerto, protocolo)
evento_critico = ("2025-10-14T10:00:00Z", "203.0.113.5", 443, "TCP")

# Intentar modificarla daría un error:
# evento_critico[1] = "192.168.1.1"  # TypeError!
```

### Casos de Uso en Ciberseguridad
- Almacenar registros que no deben cambiar, como un evento de log (IP, fecha, acción).
- Usar como claves en un diccionario (las listas no pueden ser claves por ser mutables).
- Guardar coordenadas o datos de configuración fijos, como una lista de IPs de servidores DNS de confianza.

---

## 3. Diccionarios (`dict`)

- **¿Qué son?** Colecciones desordenadas (en versiones antiguas de Python) de pares **clave-valor**.
- **Características Clave:**
    - **Clave-Valor:** Cada elemento es un par donde una clave única apunta a un valor.
    - **Mutables:** Puedes añadir, modificar o eliminar pares clave-valor.
    - **Claves Únicas:** No puede haber dos claves iguales.
- **Sintaxis:** Se definen con llaves `{}`.

```python
# Mapeo de CVEs a su puntuación de severidad (CVSS)
cve_severities = {
    "CVE-2021-44228": 9.8, # Log4Shell
    "CVE-2017-5638": 10.0, # Apache Struts
}

# Acceder a un valor por su clave
log4shell_score = cve_severities["CVE-2021-44228"]

# Añadir una nueva entrada
cve_severities["CVE-2014-0160"] = 5.0 # Heartbleed
```

### Casos de Uso en Ciberseguridad
- **El más importante:** Crear perfiles de atacantes (IP -> {país, intentos, última actividad}).
- Mapear hashes de archivos a nombres de malware conocidos.
- Contar la frecuencia de cada dirección IP en un log.

---

## 4. Conjuntos (`set`)

- **¿Qué son?** Colecciones desordenadas de elementos **únicos**.
- **Características Clave:**
    - **Desordenados:** No garantizan ningún orden.
    - **Únicos:** No permiten elementos duplicados. Si añades un elemento que ya existe, no ocurre nada.
    - **Mutables:** Puedes añadir o eliminar elementos.
- **Sintaxis:** Se definen con llaves `{}` o con `set()`.

```python
# Lista de IPs con duplicados
ips_con_duplicados = ["1.1.1.1", "2.2.2.2", "1.1.1.1"]

# Crear un conjunto para obtener IPs únicas
ips_unicas = set(ips_con_duplicados)
# ips_unicas ahora es {"1.1.1.1", "2.2.2.2"}

# Comprobación de pertenencia (muy rápida)
if "1.1.1.1" in ips_unicas:
    print("La IP ya ha sido registrada.")
```

### Casos de Uso en Ciberseguridad
- **Eliminar duplicados** de una lista de indicadores de compromiso (IOCs).
- **Comprobación de pertenencia ultra-rápida:** Verificar si una IP está en una blacklist de millones de entradas es mucho más rápido con un conjunto que con una lista.
- **Operaciones de conjuntos:** Encontrar qué IPs de tus logs (`set_A`) también están en una blacklist conocida (`set_B`) usando la intersección (`set_A.intersection(set_B)`).

---

## Tabla Comparativa Rápida

| Característica | `list` (Lista) | `tuple` (Tupla) | `dict` (Diccionario) | `set` (Conjunto) |
| :--- | :--- | :--- | :--- | :--- |
| **Sintaxis** | `[1, 2]` | `(1, 2)` | `{"a": 1, "b": 2}` | `{1, 2}` |
| **Orden** | **Ordenada** | **Ordenada** | Desordenada* | **Desordenada** |
| **Mutabilidad** | **Mutable** | **Inmutable** | **Mutable** | **Mutable** |
| **Duplicados** | **Permitidos** | **Permitidos** | Claves únicas | **No permitidos** |
| **Uso Típico** | Colección flexible | Datos que no deben cambiar | Mapeo clave-valor | Elementos únicos, tests de pertenencia |

*Nota: Desde Python 3.7, los diccionarios mantienen el orden de inserción, pero no debes confiar en ello como su característica principal.*
