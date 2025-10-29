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

## 4. Caso Práctico: Extraer una Dirección IP

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

## 5. Caso Práctico 2: Descomponer una Línea de Log

Este es el ejemplo que implementaremos en nuestro script `log_parser.py`. Queremos tomar una línea como `[2025-10-29 22:10:05] - ERROR - Failed login attempt` y extraer sus tres componentes.

Usaremos **grupos de captura `()`** para guardar cada parte que nos interesa.

-   `\[(.*?)\]`: Captura cualquier cosa (`.`) repetida cero o más veces (`*`) de forma no-codiciosa (`?`) dentro de corchetes literales `\[` y `\]`.
-   `- (.*?) -`: Captura el nivel del log.
-   `(.*)`: Captura el resto de la línea como el mensaje.

El patrón final es: `r"\[(.*?)\] - (.*?) - (.*)"`
