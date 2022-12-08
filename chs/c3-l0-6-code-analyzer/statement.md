Donat un codi font en llenguatge Java, compta la quantitat de classes
que hi ha definides.

**Input Format**

L'entrada és un codi font en vàries línies.

La paraula  sempre va separada per espais en blanc de la resta del codi.

El codi acaba amb la paraula 

**Constraints**

\-

**Output Format**

S'imprimirà la quantitat de classes definides.

**Sample Input 0**

    class A { 
       int x; 
    } 
    
    END

**Sample Output 0**

``` 
1
```

**Sample Input 1**

    class Mktr {}
    
    class Pkjy {}
    
    END

**Sample Output 1**

``` 
2
```

**Sample Input 2**

    class Mktr {
       class Trws {}
    }
    
    class Pkjy {}
    
    END

**Sample Output 2**

``` 
3
```

**Sample Input 3**

    class Mktr {}
    
    abstract class Pkjy extends Mktr{
       int i;
       
       void xcvb();
    }
    
    END

**Sample Output 3**

``` 
2
```

**Sample Input 4**

    class Mktr {}
    
    abstract class Pkjy extends Mktr{
       int i;
    
       void xcvb();
    
       class Swqz { class Ynvc {} }
    }
    
    END

**Sample Output 4**

``` 
4
```

**Sample Input 5**

    int i = 0;
    END

**Sample Output 5**

``` 
0
```
