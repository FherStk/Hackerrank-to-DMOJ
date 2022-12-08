![image](1613563726-2ffd5674a4-robotkeyboard.jpg)

Estamos diseñando un robot que sea capaz de escribir usando un teclado.

Para hacerlo más sencillo, hemos diseñado un teclado en el que todas las
teclas están en la misma fila:

![image](1613564182-402650a000-laptop-keyboard-computer-isolated-black-key-button-vector-28503589.jpg)

El orden de las teclas es el siguiente:

    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"

El robot recibe órdenes de desplazarse a izquierda o derecha, y pulsa
una tecla en cada movimiento. Es posible que alguna orden de
desplazamiento pudiera provocar que el dedo del robot se situase fuera
del teclado. En esos casos, el robot no pulsará ninguna tecla, pero su
dedo no se moverá más allá de los límites del teclado, quedando sobre la
letra `Q` o `M` según el caso.

Dadas las órdenes de desplazamiento del dedo del robot, indica el texto
que escribirá. La posición inicial del robot es `0`, correspondiente a
la letra `Q`.

**Input Format**

El primer número  indica el número de órdenes de movimiento.

A continuación vienen las  órdenes de movimiento: un número positivo
para las órdenes de desplazamiento a la derecha, y negativo para la
izquierda.

**Constraints**

\-

**Output Format**

Se imprimirá el texto final escrito por el robot.

**Sample Input 0**

    4
    16 -6 12 -12

**Sample Output 0**

    JAVA

**Sample Input 1**

    5
    10 -7 0 7 -5 

**Sample Output 1**

    ARRAY

**Sample Input 2**

    8
    11 -7 -50 3 4 50 -1 -10

**Sample Output 2**

    STRING

**Sample Input 3**

    7
    -50 0 6 -50 2 1 2

**Sample Output 3**

    QUERY

**Sample Input 4**

    10
    50 50 0 -50 -50 10 -3 50 50 -1

**Sample Output 4**

    MAIN
