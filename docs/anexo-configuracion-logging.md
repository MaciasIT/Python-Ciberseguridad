# Anexo: Configuración Profesional de Logging en Python

En nuestro script [`login_tracker.py`](../src/login_tracker.py), utilizamos `logging.basicConfig()` para ver los logs rápidamente. Sin embargo, como se mencionó, en una aplicación real, la configuración es más compleja y centralizada. Este documento explica por qué y cómo se hace.

## El Problema con `logging.basicConfig()`

`logging.basicConfig()` es una función de conveniencia que configura el *logger raíz* de tu aplicación. Tiene dos limitaciones principales en un proyecto grande:

1.  **Es una configuración global y única:** La primera vez que se llama, establece la configuración para toda la aplicación. Las llamadas posteriores son ignoradas. Si un módulo importado (como nuestra clase) lo llama, puede "secuestrar" la configuración de logging de la aplicación principal, impidiendo que esta establezca su propia configuración.

2.  **Es demasiado simple:** Solo permite una configuración básica (nivel, formato y salida a consola o un único archivo).

## La Solución: Configuración Centralizada

En una aplicación profesional, la configuración del logging se define en **un único lugar**, generalmente en el punto de entrada de la aplicación (ej. `main.py`). Esto le da al desarrollador de la aplicación principal control total sobre cómo se manejan los logs.

La responsabilidad de un módulo o clase reutilizable (como `LoginTracker`) no es *configurar* el logging, sino simplemente *solicitar un logger y usarlo*.

```python
# Dentro de una clase/módulo (la forma correcta)
import logging
log = logging.getLogger(__name__) # Obtenemos un logger específico para este módulo

def alguna_funcion():
    log.info("Esta es una entrada de log.")
    # La aplicación principal decide qué hacer con este mensaje.
```

### ¿Cómo se ve una configuración centralizada?

Se realiza a través de diccionarios (`dictConfig`) o archivos de configuración (`fileConfig`). Esto permite una gran flexibilidad.

#### Ejemplo de `dictConfig` en `main.py`:

```python
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': 'app.log',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        '': {  # Logger raíz
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'src.login_tracker': {  # Logger específico para nuestro módulo
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False, # No enviar logs al logger raíz
        }
    }
}

# Aplicar la configuración al inicio de la aplicación
logging.config.dictConfig(LOGGING_CONFIG)

# Ahora, cuando el módulo login_tracker haga logging, se aplicarán sus reglas específicas.
```

### Puntos Clave de la Configuración Avanzada:

- **Formatters:** Definen el formato del texto del log.
- **Handlers:** Definen a dónde van los logs (consola, archivos, email, etc.).
- **Loggers:** Definen reglas para diferentes partes de tu código. Puedes tener un logger para `src.database` y otro para `src.api`, cada uno con su propio nivel y handlers.

---

En resumen, el `basicConfig` que usamos fue un atajo útil para nuestro ejercicio. La práctica profesional es separar el **uso** del logging de su **configuración**.
