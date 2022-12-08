Dadas las posiciones de las reinas blanca y negra en un tablero de
ajedrez, el programa debe decir si se atacan mútuamente.

**Input Format**

El tablero de ajedrez consiste en 8 lineas de ocho caracteres cada una.
Cada caracter representa una casilla del tablero. El caracter '-' indica
una casilla vacía. La casilla en la que está la reina BLANCA se indica
con una 'B'. La casilla en la que está la reina NEGRA se indica con una
'N'.

**Constraints**

C = 64

**Output Format**

SI | NO

**Sample Input 0**

    B----N--
    --------
    --------
    --------
    --------
    --------
    --------
    --------

**Sample Output 0**

``` 
SI
```

**Sample Input 1**

    --------
    B-------
    --------
    --------
    --------
    --------
    -----N--
    --------

**Sample Output 1**

``` 
SI
```

**Sample Input 2**

    --------
    --------
    B-------
    --------
    --------
    --------
    --------
    N-------

**Sample Output 2**

``` 
SI
```

**Sample Input 3**

    --------
    ------B-
    --------
    --------
    --------
    --N-----
    --------
    --------

**Sample Output 3**

``` 
SI
```

**Sample Input 4**

    --------
    -------N
    --------
    --------
    --------
    --------
    --------
    -B------

**Sample Output 4**

``` 
SI
```

**Sample Input 5**

    --------
    --------
    --------
    --------
    --------
    -------N
    --------
    -------B

**Sample Output 5**

``` 
SI
```

**Sample Input 6**

    --------
    --------
    -N------
    --------
    --------
    --------
    --------
    ------B-

**Sample Output 6**

``` 
SI
```

**Sample Input 7**

    --------
    --------
    --------
    --------
    --------
    --------
    --------
    --N--B--

**Sample Output 7**

``` 
SI
```

**Sample Input 8**

    -B------
    ------N-
    --------
    --------
    --------
    --------
    --------
    --------

**Sample Output 8**

``` 
NO
```

**Sample Input 9**

    -----B--
    --------
    --------
    --------
    --------
    --------
    --------
    ---N----

**Sample Output 9**

``` 
NO
```

**Sample Input 10**

    --------
    --------
    --------
    --------
    N-------
    --------
    --------
    ------B-

**Sample Output 10**

``` 
NO
```

**Sample Input 11**

    --------
    --------
    --------
    --------
    -------N
    --------
    --------
    B-------

**Sample Output 11**

``` 
NO
```
