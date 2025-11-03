Anteriormente conociste las expresiones regulares y un par de símbolos que puedes usar para construir patrones de expresiones regulares. En esta lectura, explorarás símbolos adicionales de expresiones regulares que pueden ser usados en un contexto de ciberseguridad. También aprenderá más sobre el módulo re y su función re.findall().

Conceptos básicos de las expresiones regulares
Una expresión regular (regex) es una secuencia de caracteres que forma un patrón. En Python, puedes usar regex para buscar eficientemente patrones complejos como direcciones IP, correos electrónicos, o IDs de dispositivos dentro de cadenas.

Para acceder a las expresiones regulares y funciones relacionadas en Python, primero debe importar el módulo re. Debe utilizar la siguiente línea de código para importar el módulo re:

import re

Las expresiones regulares se almacenan en Python como cadenas. Luego, estas cadenas se utilizan en las funciones del módulo re para buscar en otras cadenas. Hay muchas funciones en el módulo re, pero explorarás cómo funcionan las expresiones regulares a través de re.findall(). La función re.findall() devuelve una lista de coincidencias con una expresión regular. Requiere dos parámetros. El primero es la cadena que contiene el patrón de la expresión regular, y el segundo es la cadena en la que se desea buscar.

Los patrones que componen una expresión regular están formados por caracteres alfanuméricos y símbolos especiales. Si un patrón de expresión regular está formado sólo por caracteres alfanuméricos, Python revisará la cadena especificada en busca de coincidencias con este patrón y las devolverá. En el siguiente ejemplo, el primer parámetro es un patrón de expresión regular formado únicamente por los caracteres alfanuméricos "ts". El segundo parámetro, "tsnow, tshah, bmoreno", es la cadena que buscará. Puede ejecutar el siguiente código para explorar lo que devuelve:

12
import re
re.findall("ts", "tsnow, tshah, bmoreno")
Restablecer
La salida es una lista de sólo dos elementos, las dos coincidencias con "ts": ['ts', 'ts'].

Si desea hacer algo más que buscar cadenas específicas, debe incorporar símbolos especiales a sus expresiones regulares.

Símbolos de expresiones regulares
Símbolos para tipos de caracteres
Puede utilizar diversos símbolos para formar un patrón para su expresión regular. Algunos de estos símbolos identifican un tipo concreto de carácter. Por ejemplo, \w coincide con cualquier carácter alfanumérico.

Nota: El símbolo \w también coincide con el guión bajo ( _ ).

 Puede ejecutar este código para explorar lo que devuelve re.findall() al aplicar la expresión regular de "\w" al ID de dispositivo de "h32rb17".

12
import re
re.findall("\w", "h32rb17")
Restablecer
Dado que cada carácter de este ID de dispositivo es un carácter alfanumérico, Python devuelve una lista con siete elementos. Cada elemento representa uno de los caracteres del ID de dispositivo.

Estos símbolos coinciden con un único carácter de un tipo específico.

Símbolo

Descripción

Ejemplo Match

\w

Coincide con cualquier carácter alfanumérico (A-z, 0-9) O un guión bajo (_).

En "ID_A17", coincide con I,D,_,A,1,7.

\d

Coincide con cualquier dígito (0-9).

En "ID_A17", coincide con 1,7.

\s

Coincide con cualquier carácter de espacio en blanco (espacio, tabulador, nueva línea).

Coincide con el espacio en "usuario 1".

.

Coincide con cualquier carácter (letras, dígitos, símbolos, espacios), excepto una nueva línea.


\.

Coincide con el punto literal (.). La barra invertida \ es necesaria para escapar del significado especial del punto.


El siguiente código busca en el mismo ID de dispositivo que el ejemplo anterior, pero cambia el patrón de expresión regular a "\d". Cuando lo ejecute, devolverá una lista diferente:

12
import re
re.findall("\d", "h32rb17")
Restablecer
Esta vez, la lista contiene sólo cuatro elementos. Cada elemento es uno de los dígitos numéricos de la cadena.

Símbolos para cuantificar ocurrencias
Otros símbolos cuantifican el número de apariciones de un carácter específico en el patrón. En un patrón de expresión regular, puede añadirlos después de un carácter o de un símbolo que identifique un tipo de carácter para especificar el número de repeticiones que coinciden con el patrón.

Símbolo

Descripción

Ejemplo

+

Una o más repeticiones. (por ejemplo, \d+ coincide con 1,12,12345).


*

Cero, una o más ocurrencias.


{n}

Exactamente n ocurrencias.

\d{4} coincide con cuatro dígitos consecutivos (por ejemplo, 1234).

{n,n}

Entre m (mínimo) y n (máximo) ocurrencias.

\d{1,3} coincide con 1,12 ó 123.

Por ejemplo, el símbolo + representa una o más apariciones consecutivas del carácter o tipo de carácter precedente. Cuando se utiliza con \d+, encuentra coincidencias de uno o más dígitos en una fila, como 1, 12 o 123.

En el siguiente ejemplo, el patrón lo coloca después del símbolo \d para encontrar coincidencias con uno o más dígitos consecutivos:

12
import re
re.findall("\d+", "h32rb17")
Restablecer
Con la expresión regular "\d+", la lista contiene las dos coincidencias de "32" y "17". Observe que + coincide con una secuencia de dígitos diferentes, no sólo con un dígito repetido.

Otro símbolo utilizado para cuantificar el número de ocurrencias es el símbolo *. El símbolo * representa cero, una o más ocurrencias de un carácter específico. El código siguiente sustituye el símbolo + utilizado en el ejemplo anterior por el símbolo *. Puede ejecutarlo para examinar la diferencia:

12
import re
re.findall("\d*", "h32rb17")
Restablecer
Como también coincide con cero apariciones, la lista contiene ahora cadenas vacías para los caracteres que no eran de un solo dígito, así como una cadena vacía al final.

Si desea indicar un número específico de repeticiones permitidas, puede colocar este número entre llaves ({ }) después del carácter o símbolo. En el siguiente ejemplo, el patrón de expresión regular "\d{2}" indica a Python que devuelva todas las coincidencias de exactamente dos dígitos simples en una fila de una cadena de varios ID de dispositivo:

12
import re
re.findall("\d{2}", "h32rb17 k825t0m c2994eh")
Restablecer
Como coincide con dos repeticiones, cuando Python encuentra un dígito único, comprueba si hay otro a continuación. Si lo hay, Python añade los dos dígitos a la lista y pasa al siguiente. Si no, pasa al siguiente dígito sin añadir el primer dígito a la lista.

Nota: Python escanea las cadenas de izquierda a derecha cuando las compara con una expresión regular. Cuando Python encuentra una parte de la cadena que coincide con el primer carácter esperado definido en la expresión regular, continúa comparando los caracteres siguientes con el patrón esperado. Cuando el patrón está completo, comienza este proceso de nuevo en el carácter inmediatamente posterior a la coincidencia. Así, en los casos en los que aparecen tres dígitos seguidos (por ejemplo, 123), \d{2} coincidiría con 12, y el proceso comenzaría de nuevo en el tercer dígito (3).

También puede especificar un intervalo dentro de las llaves separando dos números con una coma. El primer número es el número mínimo de repeticiones y el segundo el número máximo de repeticiones. El siguiente ejemplo devuelve todas las coincidencias que tienen entre una y tres repeticiones de un solo dígito:

12
import re
re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")
Restablecer
La lista devuelta contiene elementos de un dígito como "0", dos dígitos como "32" y tres dígitos como "825".

Construcción de un patrón
Para construir una expresión regular es necesario dividir el patrón buscado en partes más pequeñas y representarlas con los símbolos aprendidos. Considere un ejemplo de una cadena que contiene múltiples piezas de información sobre los empleados de una organización. Para cada empleado, la siguiente cadena contiene su ID de empleado, su nombre de usuario seguido de dos puntos (:), sus intentos de inicio de sesión del día y su departamento:

employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"

Su tarea es extraer el nombre de usuario y los intentos de inicio de sesión, sin el número de identificación del empleado ni el departamento.

Para completar esta tarea con expresiones regulares, debe dividir lo que está buscando en componentes más pequeños. En este caso, esos componentes son el número variable de caracteres de un nombre de usuario, dos puntos, un espacio y un número variable de dígitos simples. Los símbolos de expresión regular correspondientes son \w+, :, \s y \d+ respectivamente. Utilizando estos símbolos como su expresión regular, puede ejecutar el siguiente código para extraer las cadenas:

1234
import re
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))
Restablecer
Nota: Trabajar con expresiones regulares puede conllevar el riesgo de devolver información innecesaria o de excluir cadenas que desea devolver. Por lo tanto, es útil probar las expresiones regulares.

Puntos clave
Las expresiones regulares permiten buscar cadenas de texto que coincidan con patrones específicos. Puede utilizar expresiones regulares importando el módulo re. Este módulo contiene varias funciones, entre ellas re.findall(), que devuelve todas las coincidencias con un patrón en forma de lista. Para formar un patrón, se utilizan caracteres y símbolos. Los símbolos permiten especificar tipos de caracteres (como \d para dígito) y cuantificar cuántas repeticiones consecutivas de un carácter o tipo de carácter pueden darse en el patrón (como \d+ para uno o más dígitos).