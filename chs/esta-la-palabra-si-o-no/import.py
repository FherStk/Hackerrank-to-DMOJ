
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="esta-la-palabra-si-o-no"
p.name="Está la palabra? si o no?"
p.summary="Está la palabra? si o no?"
p.description='''Dada una lista de palabras, imprime si se encuentra o no la palabra
indicada

Algoritmo:

  - Lee de la entrada la cantidad de palabras
  - Crea un array para almacenar esas palabras
  - Rellena el array con las palabras de la entrada
  - Lee la palabra a buscar
  - Recorre el array de palabras, y por cada palabra del array:
      - Si la palabra que estás viendo del array es igual a la palabra a
        buscar
          - Guarda en una variable boolean que has encontrado la
            palabra. En este punto, puedes cortar el bucle con break,
            porque si ya has encontrado la palabra no tiene sentido
            seguir buscando.
  - Imprime  si la variable boolean te indica que has encontrado la
    palabra.  en caso contrario

**Input Format**

El primer número  indica la cantidad de palabras

A continuación vienen las  palabras.

**Constraints**

\-

**Output Format**

 | 

**Sample Input 0**

    5
    main class void static main
    
    main

**Sample Output 0**

    YES

**Sample Input 1**

    6
    public static void main string args
    
    void

**Sample Output 1**

    YES

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

    YES
'''
p.is_public=True
p.date=timezone.now()
p.save()
