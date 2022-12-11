Algunes discoteques tenen unes normes d'accés extranyes. Aquesta en
concret té les següents:

  - Si ets menor d'edad no pots entrar

  - Els homes no poden portar arracades

  - S'ha d'anar ben vestit

  - Els que tenen la tarjeta VIP poden entrar, sense tenir en compte
    aquestes normes.

Es desitja implementar un sistema de control d'accés automàtic a la
discoteca que autoritzi l'accès en base a aquestes regles. (*Un sistema
basat en el reconeixement d'imatges i NFC proporciona les dades
d'entrada*).

**Input Format**

L'entrada consta de 5 dades:

  - Un nombre enter indica l'edat

  - El sexe s'indica amb {home|dona}

  - Un booleà indica si porta arracades

  - Un booleà indica si va ben vestit

  - Un booleà indica si té tarjeta VIP

**Constraints**

No hi ha

**Output Format**

S'imprimirà "ENTRA" si el sistema autoritza l'accés i "NO ENTRA" en cas
contrari.

**Sample Input 0**

    17 home true true true

**Sample Output 0**

    ENTRA

**Sample Input 1**

    17 home true true false

**Sample Output 1**

    NO ENTRA

**Sample Input 2**

    17 home true false true

**Sample Output 2**

    ENTRA

**Sample Input 3**

    17 home true false false

**Sample Output 3**

    NO ENTRA

**Sample Input 4**

    17 home false true true

**Sample Output 4**

    ENTRA

**Sample Input 5**

    17 home false true false

**Sample Output 5**

    NO ENTRA

**Sample Input 6**

    17 home false false true

**Sample Output 6**

    ENTRA

**Sample Input 7**

    17 home false false false

**Sample Output 7**

    NO ENTRA

**Sample Input 8**

    17 dona true true true

**Sample Output 8**

    ENTRA

**Sample Input 9**

    17 dona true true false

**Sample Output 9**

    NO ENTRA

**Sample Input 10**

    17 dona true false true

**Sample Output 10**

    ENTRA

**Sample Input 11**

    17 dona true false false

**Sample Output 11**

    NO ENTRA

**Sample Input 12**

    17 dona false true true

**Sample Output 12**

    ENTRA

**Sample Input 13**

    17 dona false true false

**Sample Output 13**

    NO ENTRA

**Sample Input 14**

    17 dona false false true

**Sample Output 14**

    ENTRA

**Sample Input 15**

    17 dona false false false

**Sample Output 15**

    NO ENTRA

**Sample Input 16**

    18 home true true true

**Sample Output 16**

    ENTRA

**Sample Input 17**

    18 home true true false

**Sample Output 17**

    NO ENTRA

**Sample Input 18**

    18 home true false true

**Sample Output 18**

    ENTRA

**Sample Input 19**

    18 home true false false

**Sample Output 19**

    NO ENTRA

**Sample Input 20**

    18 home false true true

**Sample Output 20**

    ENTRA

**Sample Input 21**

    18 home false true false

**Sample Output 21**

    ENTRA

**Sample Input 22**

    18 home false false true

**Sample Output 22**

    ENTRA

**Sample Input 23**

    18 home false false false

**Sample Output 23**

    NO ENTRA

**Sample Input 24**

    18 dona true true true

**Sample Output 24**

    ENTRA

**Sample Input 25**

    18 dona true true false

**Sample Output 25**

    ENTRA

**Sample Input 26**

    18 dona true false true

**Sample Output 26**

    ENTRA

**Sample Input 27**

    18 dona true false false

**Sample Output 27**

    NO ENTRA

**Sample Input 28**

    18 dona false true true

**Sample Output 28**

    ENTRA

**Sample Input 29**

    18 dona false true false

**Sample Output 29**

    ENTRA

**Sample Input 30**

    18 dona false false true

**Sample Output 30**

    ENTRA

**Sample Input 31**

    18 dona false false false

**Sample Output 31**

    NO ENTRA

**Sample Input 32**

    19 home true true true

**Sample Output 32**

    ENTRA

**Sample Input 33**

    19 home true true false

**Sample Output 33**

    NO ENTRA

**Sample Input 34**

    19 home true false true

**Sample Output 34**

    ENTRA

**Sample Input 35**

    19 home true false false

**Sample Output 35**

    NO ENTRA

**Sample Input 36**

    19 home false true true

**Sample Output 36**

    ENTRA

**Sample Input 37**

    19 home false true false

**Sample Output 37**

    ENTRA

**Sample Input 38**

    19 home false false true

**Sample Output 38**

    ENTRA

**Sample Input 39**

    19 home false false false

**Sample Output 39**

    NO ENTRA

**Sample Input 40**

    19 dona true true true

**Sample Output 40**

    ENTRA

**Sample Input 41**

    19 dona true true false

**Sample Output 41**

    ENTRA

**Sample Input 42**

    19 dona true false true

**Sample Output 42**

    ENTRA

**Sample Input 43**

    19 dona true false false

**Sample Output 43**

    NO ENTRA

**Sample Input 44**

    19 dona false true true

**Sample Output 44**

    ENTRA

**Sample Input 45**

    19 dona false true false

**Sample Output 45**

    ENTRA

**Sample Input 46**

    19 dona false false true

**Sample Output 46**

    ENTRA

**Sample Input 47**

    19 dona false false false

**Sample Output 47**

    NO ENTRA

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
