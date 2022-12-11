La codificació Run-length encoding (RLE) és una forma molt simple de
compressió de dades en què seqüències de dades amb el mateix valor
consecutiu són emmagatzemades com un únic valor més el seu recompte.

Per exemple, la cadena següent cadena de text:

    BBBBNNNBBBBBNN

Es pot comprimir d'aquesta manera:

    4B3N5B2N

S'interpreta com 4 bes, 3 enes, 5 bes, 2 enes.

**Input Format**

Una cadena de L caracters comprimida en RLE

**Constraints**

No hi ha cap recompte superior a 9

**Output Format**

La cadena descomprimida

**Sample Input 0**

    3B4N

**Sample Output 0**

    BBBNNNN

**Sample Input 1**

    5B3N1B

**Sample Output 1**

    BBBBBNNNB

**Sample Input 2**

    1B5N1B

**Sample Output 2**

    BNNNNNB

**Sample Input 3**

    1A3B4A3N2C1A5D

**Sample Output 3**

    ABBBAAAANNNCCADDDDD

**Sample Input 4**

    8W7H7A9T

**Sample Output 4**

    WWWWWWWWHHHHHHHAAAAAAATTTTTTTTT

**Sample Input 5**

    1J1A1V1A

**Sample Output 5**

    JAVA

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
