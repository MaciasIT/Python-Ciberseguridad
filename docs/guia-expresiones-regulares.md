# Guía de Expresiones Regulares (Regex)

Las expresiones regulares (regex) son un "mini-lenguaje" increíblemente potente que vive dentro de otros lenguajes de programación. Su único propósito es buscar y manipular texto basándose en patrones. Para un analista de ciberseguridad, dominar las regex es una habilidad fundamental.

## 1. ¿Por qué son Esenciales en Ciberseguridad?

-   **Análisis de Logs:** Para extraer información específica (IPs, timestamps, mensajes de error) de miles de líneas de logs de firewalls, servidores web, etc.
-   **Validación de Datos:** Para asegurar que una entrada de usuario (ej. un nombre de usuario) cumple con una política de seguridad.
-   **Inteligencia de Amenazas (Threat Intelligence):** Para buscar Indicadores de Compromiso (IOCs) como hashes de malware, dominios, emails, etc., en grandes volúmenes de texto.
-   **Desarrollo de Firmas:** Para escribir firmas para Sistemas de Detección de Intrusos (IDS) o reglas YARA.

## 2. El Módulo `re` de Python

Python nos da el módulo `re` para trabajar con regex. Las funciones más comunes son:

-   `re.search(patron, texto)`: Busca el patrón en cualquier parte del texto. Devuelve un objeto "match" en la primera coincidencia, o `None` si no encuentra nada.
-   `re.findall(patron, texto)`: Encuentra **todas** las coincidencias del patrón y las devuelve como una lista de strings.
-   `re.compile(patron)`: "Pre-compila" un patrón que vas a usar muchas veces. Esto mejora el rendimiento.

## 3. Sintaxis Esencial de Regex

| Símbolo   | Descripción                                       | Ejemplo                               | Coincidencia de Ejemplo                |
| :-------- | :------------------------------------------------ | :------------------------------------ | :------------------------------------- |
| `.`       | Cualquier carácter (excepto nueva línea)          | `h.t`                                 | `hat`, `hot`, `h8t`                    |
| `^`       | Inicio de la cadena de texto                      | `^root`                               | `root login` (pero no `sudo root`)     |
| `$`       | Fin de la cadena de texto                         | `denied$`                             | `access denied` (pero no `denied `)    |
| `*`       | Cero o más repeticiones del carácter anterior     | `ab*c`                                | `ac`, `abc`, `abbbc`                   |
| `+`       | Una o más repeticiones del carácter anterior      | `ab+c`                                | `abc`, `abbbc` (pero no `ac`)          |
| `?`       | Cero o una repetición del carácter anterior       | `colou?r`                             | `color`, `colour`                      |
| `\d`      | Cualquier dígito (0-9)                            | `\d\d\d`                               | `123`, `987`                           |
| `\w`      | Cualquier carácter alfanumérico (a-z, A-Z, 0-9, `_`) | `\w+`                                | `user_123`, `admin`                    |
| `\s`      | Cualquier carácter de espacio en blanco           | `ip\s+address`                        | `ip address`, `ip   address`           |
| `[abc]`   | Un solo carácter que sea `a`, `b`, o `c`          | `gr[ae]y`                             | `gray`, `grey`                         |
| `(abc)`   | Agrupa una expresión. Permite capturar el texto.  | `(ERROR):\s(.*)`                     | Captura `ERROR` y el mensaje que sigue |

## 4. Conceptos Avanzados

### 4.1. Búsquedas "Greedy" vs. "Non-Greedy" (Codiciosas vs. No Codiciosas)

Por defecto, los cuantificadores como `*` y `+` son **"greedy" (codiciosos)**. Esto significa que intentan abarcar la mayor cantidad de texto posible.

-   **Ejemplo Greedy:** Si aplicas el patrón `<.*>` al texto `<tag1>contenido</tag1>`, el resultado será `<tag1>contenido</tag1>`. El `.*` abarca todo desde el primer `<` hasta el último `>`.

A veces, este no es el comportamiento deseado. Para hacerlo **"non-greedy" (no codicioso)**, simplemente añade un `?` después del cuantificador.

-   **Ejemplo Non-Greedy:** Con el patrón `<.*?>` sobre el mismo texto, obtendrás dos coincidencias: `<tag1>` y `</tag1>`. El `.*?` abarca la menor cantidad de texto posible.

### 4.2. Aserciones (Lookaheads & Lookbehinds)

Las aserciones son una de las características más potentes de las regex. Permiten comprobar si un patrón está (o no está) seguido o precedido por otro patrón, **sin que este último forme parte de la coincidencia final**. Son "asonciones de ancho cero" (zero-width assertions).

| Símbolo         | Descripción                               | Ejemplo                                   | Coincidencia de Ejemplo                                       |
| :-------------- | :---------------------------------------- | :---------------------------------------- | :------------------------------------------------------------ |
| `(?=patron)`    | **Lookahead Positivo:** Asegura que lo que sigue coincide con `patron`. | `Isaac (?=Asimov)`                        | Coincide con `Isaac ` solo si va seguido de `Asimov`.         |
| `(?!patron)`    | **Lookahead Negativo:** Asegura que lo que sigue **no** coincide con `patron`. | `Error (?!404)`                           | Coincide con `Error ` si no va seguido de `404`.              |
| `(?<=patron)`   | **Lookbehind Positivo:** Asegura que lo que precede coincide con `patron`. | `(?<=HTTP/1.1\s)200`                      | Coincide con `200` solo si está precedido por `HTTP/1.1 `.    |
| `(?<!patron)`   | **Lookbehind Negativo:** Asegura que lo que precede **no** coincide con `patron`. | `(?<![a-z])\d+`                           | Coincide con números que no estén precedidos por una letra.   |

### 4.3. Banderas de Compilación (Compilation Flags)

Las banderas (o "flags") modifican el comportamiento de una expresión regular. Se pueden usar directamente en la función `re.compile()` o en las funciones `re.search()`, `re.findall()`, etc.

-   `re.IGNORECASE` o `re.I`: Ignora las diferencias entre mayúsculas y minúsculas. `re.findall('error', 'Error: 404', re.I)` encontrará 'Error'.
-   `re.MULTILINE` o `re.M`: Hace que `^` y `$` coincidan con el inicio y fin de cada línea, no solo del string completo.
-   `re.DOTALL` o `re.S`: Permite que el `.` (punto) coincida también con el carácter de nueva línea (`\n`).

## 5. Caso Práctico: Extraer una Dirección IP

Una dirección IPv4 consiste en cuatro números (de 1 a 3 dígitos cada uno) separados por puntos.

-   Un número de 1 a 3 dígitos se puede representar como `\d{1,3}`.
-   Un punto literal se debe "escapar" con una barra: `\.`

El patrón completo sería: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

```python
import re

log_line = "[2025-10-29] - ALERT - Suspicious connection from 192.168.1.101 to target 8.8.8.8"

# Definimos el patrón para una IP
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Usamos findall para encontrar todas las IPs en la línea
found_ips = re.findall(ip_pattern, log_line)

print(f"IPs encontradas: {found_ips}")
# Salida: IPs encontradas: ['192.168.1.101', '8.8.8.8']
```

## 6. Caso Práctico 2: Descomponer una Línea de Log

Este es el ejemplo que implementaremos en nuestro script `log_parser.py`. Queremos tomar una línea como `[2025-10-29 22:10:05] - ERROR - Failed login attempt` y extraer sus tres componentes.

Usaremos **grupos de captura `()`** para guardar cada parte que nos interesa.

-   `\[(.*?)\]`: Captura cualquier cosa (`.`) repetida cero o más veces (`*`) de forma no-codiciosa (`?`) dentro de corchetes literales `\[` y `\]`.
-   `- (.*?) -`: Captura el nivel del log.
-   `(.*)`: Captura el resto de la línea como el mensaje.

El patrón final es: `r"\\[(.*?)\\] - (.*?) - (.*)"`

## 7. Caso Práctico 3: Extracción de CVEs y Nombres de Host

Un **CVE (Common Vulnerabilities and Exposures)** es un identificador único para una vulnerabilidad de seguridad. Su formato es `CVE-AÑO-NUMERO`. Un nombre de host válido sigue ciertas reglas (letras, números, guiones).

```python
import re

reporte = """
Informe de Vulnerabilidades:
Se ha detectado la vulnerabilidad CVE-2021-44228 en el host 'srv-log4j.example.com'.
También se encontró CVE-2022-12345 en 'web-app.prod'. El sistema antiguo 'legacy.local' no parece afectado.
Se recomienda parchear CVE-2021-44228 inmediatamente.
"""

# Patrón para CVEs: CVE, guión, 4 dígitos (año), guión, 4 o más dígitos (número)
cve_pattern = r"CVE-\d{4}-\d{4,}"

# Patrón para nombres de host: secuencias de letras, números y guiones, separadas por puntos.
# Usamos un lookbehind negativo para no capturar 'CVE-2021-44228' como un hostname.
hostname_pattern = r"(?<!CVE-)\b([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"


cves_encontrados = re.findall(cve_pattern, reporte)
hosts_afectados = re.findall(hostname_pattern, reporte)

print(f"CVEs encontrados: {list(set(cves_encontrados))}") # Usamos set para eliminar duplicados
print(f"Hosts afectados: {hosts_afectados}")

# Salida:
# CVEs encontrados: ['CVE-2021-44228', 'CVE-2022-12345']
# Hosts afectados: ['srv-log4j.example.com', 'web-app.prod']
```

## 🧠 Tabla de Expresiones Regulares Útiles en Ciberseguridad

| Tipo de dato o uso                  | Patrón (Regex)                                       | Ejemplo de coincidencia                | Explicación                                                     |
| :---------------------------------- | :--------------------------------------------------- | :------------------------------------- | :-------------------------------------------------------------- |
| Dirección IP (IPv4)                 | `\b\d{1,3}(\.\d{1,3}){3}\b`                           | `192.168.0.10`                         | Detecta 4 grupos de 1 a 3 dígitos separados por puntos.         |
| Dirección IP (IPv6)                 | `([a-fA-F0-9:]+:+)+[a-fA-F0-9]+`                     | `fe80::1ff:fe23:4567:890a`              | Coincide con direcciones IPv6 en formato hexadecimal.           |
| Dirección MAC                       | `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})`             | `00:1A:2B:3C:4D:5E`                    | Detección de direcciones MAC con separadores `:` o `-`.         |
| Correo electrónico                  | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`      | `user@mail.com`                        | Detecta direcciones de correo válidas.                          |
| URL o dominio                       | `https?://[^\s/$.?#].[^\s]*`                          | `https://malware.com/path`             | Detecta enlaces HTTP y HTTPS.                                   |
| Nombre de usuario (alfanumérico)    | `\b[a-zA-Z0-9_]{3,16}\b`                              | `admin_123`                            | Coincide con nombres de usuario típicos en logs.                |
| Fechas (YYYY-MM-DD)                 | `\d{4}-\d{2}-\d{2}`                                   | `2025-11-04`                           | Detecta fechas en formato ISO estándar.                         |
| Horas (HH:MM:SS)                    | `\b\d{1,2}:\d{2}:\d{2}\b`                              | `18:34:21`                             | Coincide con tiempos en formato de 24 horas.                    |
| Códigos hash (MD5)                  | `\b[a-fA-F0-9]{32}\b`                                 | `5d41402abc4b2a76b9719d911017c592`      | Identifica hashes MD5 en archivos o logs.                       |
| Códigos hash (SHA-1)                | `\b[a-fA-F0-9]{40}\b`                                 | `da39a3ee5e6b4b0d3255bfef95601890afd80709` | Detecta hashes SHA-1.                                           |
| Códigos hash (SHA-256)              | `\b[a-fA-F0-9]{64}\b`                                 | `9c56cc51b374c3...`                     | Detecta hashes SHA-256, comunes en malware.                     |
| Dirección IPv4 no válida (detección) | `\d{1,3}(\.\d{1,3}){3}(?!\d)`                         | `192.168.300.999`                      | Detecta direcciones con números fuera de rango (para validación). |
| Número de puerto                    | `\b\d{1,5}\b`                                         | `8080`, `443`                          | Detecta posibles puertos TCP/UDP.                               |
| Palabras clave sospechosas          | `(?i)(admin\|root\|hack\|attack\|malware)`            | `User 'admin' logged in`               | Detecta palabras clave comunes sin distinguir mayúsculas/minúsculas. |