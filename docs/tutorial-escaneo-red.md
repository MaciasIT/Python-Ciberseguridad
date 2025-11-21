# Tutorial: Escaneo de Red y Sockets en Python

En este tutorial, exploraremos cómo Python interactúa con la red a bajo nivel. Aprenderemos sobre **Sockets** para conectar puertos y sobre **Threading** (hilos) para realizar tareas en paralelo, dos conceptos fundamentales para cualquier profesional de ciberseguridad.

## 1. ¿Qué es un Socket?

Un **Socket** es un punto final en un enlace de comunicación bidireccional entre dos programas que se ejecutan en la red. Piensa en él como un "enchufe" virtual.

Para que dos ordenadores hablen, necesitan:
1.  **Dirección IP:** Para saber *dónde* está el otro ordenador.
2.  **Puerto:** Para saber *a qué servicio* (programa) queremos hablar (ej: 80 para web, 22 para SSH).

En Python, la librería `socket` nos da acceso directo a esta funcionalidad.

### Ejemplo de Conexión TCP

```python
import socket

# Crear un socket TCP/IP
# AF_INET = IPv4
# SOCK_STREAM = TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Intentar conectar a Google en el puerto 80
resultado = sock.connect_ex(('google.com', 80))

if resultado == 0:
    print("¡Puerto Abierto!")
else:
    print("Puerto Cerrado o Filtrado")

sock.close()
```

Si `connect_ex` devuelve `0`, significa que el "apretón de manos" (handshake) TCP se completó con éxito. ¡El puerto está abierto!

---

## 2. Escaneo de Red y Paralelismo (Threading)

Cuando queremos escanear una red entera (ej: `192.168.1.1` hasta `192.168.1.254`), tenemos un problema de velocidad.

Si hacemos un `ping` que tarda 1 segundo, y tenemos 254 IPs:
`254 IPs * 1 segundo = 254 segundos (~4 minutos)`

¡Es demasiado lento! Aquí es donde entra el **Threading** (Hilos).

### ¿Qué son los Hilos?

Imagina que eres un camarero.
- **Enfoque Secuencial (Sin hilos):** Tomas nota a la mesa 1, vas a cocina, esperas la comida, la sirves. Luego vas a la mesa 2...
- **Enfoque Paralelo (Con hilos):** Tomas nota a la mesa 1 y envías la comanda. Mientras se cocina, tomas nota a la mesa 2...

En nuestro escáner de red, lanzamos 50 o 100 "camareros" (hilos) a la vez. Cada uno se encarga de hacer ping a una IP diferente simultáneamente.

### Implementación con `concurrent.futures`

Python moderno facilita esto con `ThreadPoolExecutor`:

```python
import concurrent.futures
import subprocess

def hacer_ping(ip):
    # Lógica de ping...
    return True # o False

ips = ["192.168.1.1", "192.168.1.2", ...] # 254 IPs

# Lanzamos 50 hilos a la vez
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(hacer_ping, ips)
```

Gracias a esto, nuestro escáner de red tarda solo unos segundos en revisar toda la subred.

## Conclusión

Con estas herramientas, has pasado de escribir scripts simples a crear herramientas de red performantes.
- **Sockets** te permiten "tocar" puertos y servicios.
- **Threading** te permite escalar tus herramientas para que funcionen rápido en redes grandes.

¡Sigue experimentando!
