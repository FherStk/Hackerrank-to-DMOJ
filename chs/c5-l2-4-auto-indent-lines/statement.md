Indentar -tabular, sagnar- és obligatori en Python. No obstant, és
important fer-ho en tots els llenguatges, ja que ajuda a la
comprensibilitat del codi.

Hi ha diferents estils d'indentació per als llenguatges que defineixen
els blocs amb claus. La més comú és la K\&R

  - K\&R

<!-- end list -->

    while (x == y) {
        something();
        somethingelse();
    }

  - Allman

<!-- end list -->

    while (x == y)
    {
        something();
        somethingelse();
    }

  - GNU

<!-- end list -->

    while (x == y)
      {
        something ();
        somethingelse ();
      }

  - Whitesmiths

<!-- end list -->

    while (x == y)
        {
        something();
        somethingelse();
        }

  - Horstmann

<!-- end list -->

    while (x == y)
    {   something();
        somethingelse();
    }

  - Pico

<!-- end list -->

    while (x == y)
    {   something();
        somethingelse(); }

  - Ratliff

<!-- end list -->

    while (x == y) {
        something();
        somethingelse();
        }

  - Lisp

<!-- end list -->

    while (x == y)
      { something();
        somethingelse(); }

  - Haskell

<!-- end list -->

    while (x == y)
      { something()
      ; somethingelse()
      ; 
      }

Amb els IDE tenim l'opció d'Auto-Indentar el codi. ¿Com ho fan?

**Input Format**

La entrada és un codi escrit amb indentació K\&R, però els espais
d'indentació mal col·locats. Tots els blocs del codi estan entre claus
{} El codi acaba amb la marca END.

**Constraints**

No hi ha cap restricció significativa.

**Output Format**

S'escriurà el codi correctament indentat, estil K\&R. El tamany
d'indentació és 4 espais.

**Sample Input 0**

    if(true){
       a=3;
          b=7;
    }
    
    END

**Sample Output 0**

    if(true){
        a=3;
        b=7;
    }

**Sample Input 1**

``` 
   while(true){
   a=3;
  b=7;
}

END
```

**Sample Output 1**

    while(true){
        a=3;
        b=7;
    }

**Sample Input 2**

``` 
    if(true){
        a=10;
      } else {
    b=7;
  }

END
```

**Sample Output 2**

    if(true){
        a=10;
    } else {
        b=7;
    }

**Sample Input 3**

``` 
   if(true){
   a=3;
      b=7;
 while(false){
 c=9;
    }
       }

END
```

**Sample Output 3**

    if(true){
        a=3;
        b=7;
        while(false){
            c=9;
        }
    }

**Sample Input 4**

``` 
 if(true){
        a=10;
    } else {
  b=7;
for(int i=0; i<10; i++){
  c=0;
  }  
     }

END
```

**Sample Output 4**

    if(true){
        a=10;
    } else {
        b=7;
        for(int i=0; i<10; i++){
            c=0;
        }
    }

**Sample Input 5**

``` 
 if(true){
        a=10;
       } else {
       if(a==b){
          d=6;
   } else {
  b=7;
for(int i=0; i<10; i++){
  c=0;
  }
     }
}
END
```

**Sample Output 5**

    if(true){
        a=10;
    } else {
        if(a==b){
            d=6;
        } else {
            b=7;
            for(int i=0; i<10; i++){
                c=0;
            }
        }
    }

**Sample Input 6**

    while(!false){
        if(true){
            l--;
            sout();
            l++;
        } else if(false){
               sout();
               l++;
            } else if(true){
                l--;
                sout();
            } else {
                sout();
        }
    }
    
    END

**Sample Output 6**

    while(!false){
        if(true){
            l--;
            sout();
            l++;
        } else if(false){
            sout();
            l++;
        } else if(true){
            l--;
            sout();
        } else {
            sout();
        }
    }

**Sample Input 7**

    if(true){
    a();
        if(true){
            a();
        } else if(true){
            if(true){
            a();    
        } else {
             if(true){
                a();    
                }
                a();
                   }
              } else {
                  a();
        if(true){
            a();
        }
         a();
        }
        a();
        } else {
            if(true){
                if(true){
                    a();    
                }
                a();
    } else {
        a();
        }
        a();
    }
    
    END

**Sample Output 7**

    if(true){
        a();
        if(true){
            a();
        } else if(true){
            if(true){
                a();
            } else {
                if(true){
                    a();
                }
                a();
            }
        } else {
            a();
            if(true){
                a();
            }
            a();
        }
        a();
    } else {
        if(true){
            if(true){
                a();
            }
            a();
        } else {
            a();
        }
        a();
    }

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
