Donats dos operands i un resultat, troba l'operador que satisfà la
operació.

Els operadors possibles són: suma, resta, multiplicació, divisió i
mòdul.

    + - * / %

Si la operació pot ser resolta per més d'un operador, s'ha d'escollir el
que estigui primer en la llista.

Si no es pot satisfer amb ninguna operació s'escriurà "IMPOSSIBLE".

**Input Format**

Dos operands O1 i O2. I un resultat R

**Constraints**

0 \<= O1 \<= 10^9

0 \<= O2 \<= 10^9

0 \<= R \<= 10^9

**Output Format**

Es mostrarà el símbol de l'operador que satisfà la operació.

    + - * / %

En cas de que no es puig satisfer amb cap, es mostrarà:

    IMPOSSIBLE

**Sample Input 0**

    1 1 1

**Sample Output 0**

``` 
*
```

**Explanation 0**

1 **\*** 1 = 1

**Sample Input 1**

    1 2 3

**Sample Output 1**

``` 
+
```

**Explanation 1**

1 **+** 2 = 3

**Sample Input 2**

    0 0 0

**Sample Output 2**

``` 
+
```

**Explanation 2**

0 **+** 0 = 0

**Sample Input 3**

    10 0 7

**Sample Output 3**

    IMPOSSIBLE

**Sample Input 4**

    1 3 1

**Sample Output 4**

``` 
%
```

**Explanation 4**

1 **%** 3 = 1

**Sample Input 5**

    30 12 6

**Sample Output 5**

``` 
%
```

**Sample Input 6**

    13 7 91

**Sample Output 6**

``` 
*
```

**Sample Input 7**

    14 7 2

**Sample Output 7**

``` 
/
```

**Sample Input 8**

    10 3 1

**Sample Output 8**

``` 
%
```

**Sample Input 9**

    55 15 10

**Sample Output 9**

``` 
%
```

**Sample Input 10**

    84 0 0

**Sample Output 10**

``` 
*
```

**Sample Input 11**

    62 0 21

**Sample Output 11**

    IMPOSSIBLE

**Sample Input 12**

    99 15 29

**Sample Output 12**

    IMPOSSIBLE

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
