En el juego de bolos, los bolos se colocan en filas de manera que en la
primera fila hay un bolo, y en cada fila hay un bolo más que en la
anterior.

![image](1548249910-2030623bda-Untitleddrawing.png)

Dado un número de bolos, determina si es posible organizarlos para que
se forme un triangulo completo, es decir que ninguna fila quede
incompleta.

**Input Format**

Un numero N de bolos

**Constraints**

1 \<= N \<= 100000

**Output Format**

true | false

**Sample Input 0**

``` 
6
```

**Sample Output 0**

    true

**Explanation 0**

6 bolos se pueden colocar perfectamente:

    o o o
     o o
      o

**Sample Input 1**

``` 
8
```

**Sample Output 1**

    false

**Explanation 1**

8 bolos no se pueden colocar de forma perfecta. Quedaría incompleto.

    o o
     o o o
      o o
       o

**Sample Input 2**

``` 
21
```

**Sample Output 2**

    true

**Explanation 2**

21 bolos se pueden colocar perfectamente:

    o o o o o o
     o o o o o
      o o o o
       o o o
        o o
         o

**Sample Input 3**

``` 
4
```

**Sample Output 3**

    false

**Explanation 3**

Con 4 bolos el triángulo queda incompleto:

    o
     o o
      o

**Sample Input 4**

``` 
91
```

**Sample Output 4**

    true

**Sample Input 5**

``` 
78
```

**Sample Output 5**

    true

**Sample Input 6**

``` 
1
```

**Sample Output 6**

    true

**Sample Input 7**

    990

**Sample Output 7**

    true

**Sample Input 8**

    9870

**Sample Output 8**

    true

**Sample Input 9**

    998991

**Sample Output 9**

    true

**Sample Input 10**

    997570

**Sample Output 10**

    false

**Sample Input 11**

``` 
27
```

**Sample Output 11**

    false

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
