En Java els arrays es poden inicialitzar amb la següent notació:

    tipus[] identificador = { valor0, valor1, valor2, ..., valorN };

Escriu un programa que generi el codi d'inicialització d'un array a
partir de les dades d'entrada.

El tipus de dades de l'entrada sempre és `int`, i l'identificador de
l'array ha de ser `myArray`.

**Input Format**

El primer número  indica la quantitat de nombres que venen a
continuació.

Després venen els  nombres separats per espais en blanc.

**Constraints**

\> 0

**Output Format**

S'imprimirà la declaració de l'array en el format indicat i en una sola
línia.

**Sample Input 0**

    5
    11 13 17 19 23

**Sample Output 0**

    int[] myArray = { 11, 13, 17, 19, 23 };

**Sample Input 1**

    3
    100 200 300

**Sample Output 1**

    int[] myArray = { 100, 200, 300 };

**Sample Input 2**

    10
    23 76 12 54 98 65 67 39 91 83

**Sample Output 2**

    int[] myArray = { 23, 76, 12, 54, 98, 65, 67, 39, 91, 83 };

**Sample Input 3**

    1
    67

**Sample Output 3**

    int[] myArray = { 67 };
