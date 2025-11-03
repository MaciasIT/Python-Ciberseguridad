# Proyecto de Python para Ciberseguridad 🐍

¡Bienvenido! Este es un repositorio de aprendizaje para el curso de Ciberseguridad de Google, enfocado en la aplicación de conceptos de Python a problemas de seguridad del mundo real.

## ✨ Estado del Proyecto

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Testing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)
![Methodology](https://img.shields.io/badge/Methodology-TDD-purple.svg)

## 📂 Estructura del Proyecto

El proyecto está organizado de forma clara y profesional para facilitar el aprendizaje y la contribución.

```
.
├── data/              # 🗂️ Archivos de datos de ejemplo (logs, listas, etc.)
├── docs/              # 📄 Documentación y explicaciones en formato Markdown
├── scripts/           # 💻 Scripts de línea de comandos
├── src/               # 🐍 Código fuente de los scripts de Python
├── tests/             # 🧪 Pruebas unitarias para el código fuente
├── .gitignore         # 🙈 Archivos y directorios ignorados por Git
├── diario_consultas.md  # 📖 Índice y resumen de las sesiones
├── main.py            # ▶️ Script principal para ejecutar la lógica
└── README.md          # ⭐ Este archivo
```

## 🧠 Principios y Temas Tratados

Este proyecto se guía por principios de desarrollo profesional y cubre los siguientes temas:

-   **Fundamentos de Python:** Variables, Tipos de Datos, Booleanos, Condicionales y Bucles.
-   **Desarrollo Guiado por Pruebas (TDD):** Usamos el módulo `unittest` para asegurar que nuestro código es robusto y funciona como se espera. ¡Primero la prueba, luego el código!
-   **Documentación Sistemática:** Cada concepto nuevo se documenta en la carpeta `docs`.
-   **Control de Versiones:** Usamos Git para gestionar el historial de cambios del proyecto.

## 💡 Scripts Desarrollados

Aquí están los módulos prácticos que hemos construido:

1.  **Login Tracker (`src/login_tracker.py`):**
    -   Simula el seguimiento de intentos de inicio de sesión y bloquea cuentas tras múltiples fallos para prevenir ataques de fuerza bruta.

2.  **Validador de Contraseñas (`src/password_validator.py`):**
    -   Evalúa la fortaleza de una contraseña basándose en un conjunto de reglas (longitud, caracteres, etc.).

3.  **Analizador de Logs (`src/log_analyzer.py`):**
    -   Procesa logs de texto para extraer información relevante, como IPs en líneas de error.

4.  **Generador de IDs de Empleado (`src/generador_id_empleado.py`):**
    -   Genera IDs únicos para un departamento basándose en reglas específicas.

5.  **Analizador de IPs (`src/ip_analyzer.py`):**
    -   Toma una lista de IPs, elimina duplicados y la compara contra una `blacklist` para encontrar coincidencias maliciosas.

6.  **Parser de Logs con Regex (`src/log_parser.py`):**
    -   Utiliza expresiones regulares para descomponer una línea de log en sus componentes estructurados (timestamp, nivel, mensaje).

7.  **Detector de Patrones (`src/pattern_detector.py`):**
    -   Un potente módulo que utiliza un diccionario de expresiones regulares para encontrar una amplia variedad de Indicadores de Compromiso (IoCs) en texto, como IPs (v4/v6), hashes (MD5, SHA1, SHA256), emails, URLs y más.

8.  **Script Principal (`main.py`):**
    -   Orquesta la ejecución de las funciones de los otros módulos a modo de demostración.

## 💻 Herramientas de Línea de Comandos

El proyecto incluye herramientas de CLI para interactuar con la lógica del programa directamente desde la terminal.

### Detector de Patrones

Puedes usar `scripts/detect_patterns_cli.py` para analizar un archivo de log y generar un reporte de los patrones encontrados.

**Uso:**

```bash
python3 scripts/detect_patterns_cli.py -i <archivo_de_log> [-f <archivo_de_ips_marcadas>] [-o <archivo_de_salida>]
```

**Ejemplo:**

```bash
# Analizar un log y compararlo con una lista de IPs conocidas
python3 scripts/detect_patterns_cli.py -i data/sample_log.txt -f data/flagged.txt
```

## 🧪 Cómo Ejecutar las Pruebas

Para verificar la integridad de todo el código, puedes ejecutar el conjunto de pruebas con este comando:

```bash
python3 -m unittest discover
```
