# Proyecto de Python para Ciberseguridad 🐍

![Python](https://img.shields.io/badge/Python-3.12-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![TDD](https://img.shields.io/badge/Methodology-TDD-purple.svg)

Repositorio de aprendizaje para el curso de Ciberseguridad de Google, enfocado en la aplicación de conceptos de Python a problemas de seguridad a través de la metodología de Desarrollo Guiado por Pruebas (TDD).

## 🚀 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
. 
├── docs/              # Documentación y explicaciones en formato Markdown
├── src/               # Código fuente de los scripts de Python
├── tests/             # Pruebas unitarias para el código fuente
├── .gitignore         # Archivos y directorios ignorados por Git
├── diario_consultas.md  # Índice y resumen de las sesiones
├── GEMINI.md          # Directrices para el asistente de IA
└── README.md          # Este archivo
```

## 📚 Temas Tratados

- **Fundamentos de Python:**
  - Variables y Tipos de Datos
  - Booleanos y Operadores
  - Sentencias Condicionales (`if`/`elif`/`else`)
- **Desarrollo Profesional:**
  - Desarrollo Guiado por Pruebas (TDD) con `unittest`.
  - Estructura de proyectos (`src`, `docs`, `tests`).
  - Logging para auditoría y seguimiento.
  - Control de versiones con Git.

## 🛠️ Scripts Desarrollados

1.  **Login Tracker (`src/login_tracker.py`):**
    - Simula el seguimiento de intentos de inicio de sesión.
    - Implementa un límite de intentos para prevenir ataques de fuerza bruta.
    - Utiliza `logging` para registrar eventos de seguridad críticos.

2.  **Validador de Contraseñas (`src/password_validator.py`):**
    - Evalúa la fortaleza de una contraseña (`Débil`, `Media`, `Fuerte`).
    - Comprueba múltiples criterios usando sentencias condicionales.
    - Incluye una comprobación contra una lista de contraseñas comunes.

## ⚙️ Cómo Ejecutar las Pruebas

Para ejecutar todas las pruebas del proyecto, puedes usar el siguiente comando desde la raíz del directorio:

```bash
python3 -m unittest discover
```
