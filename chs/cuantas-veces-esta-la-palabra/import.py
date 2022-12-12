
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="cuantas-veces-esta-l"
p.name="Cuántas veces está la palabra?"
p.summary="Cuántas veces está la palabra?"
p.description='''Dada una lista de palabras, imprime la cantidad de veces que aparece la
palabra indicada

Algoritmo:

  - Lee de la entrada la cantidad de palabras
  - Crea un array para almacenar esas palabras
  - Rellena el array con las palabras de la entrada
  - Lee la palabra a buscar
  - Recorre el array de palabras, y por cada palabra del array:
      - Si la palabra que estás viendo del array es igual a la palabra a
        buscar
          - Augmenta una variable contador.
  - Imprime la variable contador

**Input Format**

El primer número  indica la cantidad de palabras

A continuación vienen las  palabras.

**Constraints**

\-

**Output Format**

entero

**Sample Input 0**

    5
    main class void static main
    
    main

**Sample Output 0**



**Sample Input 1**

    6
    public static void main string args
    
    void

**Sample Output 1**



**Sample Input 2**

    3
    char int string
    
    float

**Sample Output 2**



**Sample Input 3**

    13
    continue for switch boolean do if break else case int char float while
    
    break

**Sample Output 3**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
