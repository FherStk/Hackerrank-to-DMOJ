
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="passar-llista"
p.name="Passar llista #arrays"
p.summary="Passar llista"
p.description='''Tenim una llista d'alumnes.

Després preguntem els noms als alumnes que hi ha a classe, i hem de
determinar si estan a la llista, o no, i en quina posició.

**Input Format**

El primer nombre  indica la quantitat d'alumnes que hi ha a la llista.
Després venen els  noms de la llista.

A continuació ve una sèrie amb els noms dels alumnes que hi ha a la
classe. La sèrie acaba amb 

**Constraints**

\-

**Output Format**

Per cada alumne de la classe, s'escriurà la seva posició a la llista, o
la paraula  si no hi és a la llista.

**Sample Input 0**

    4
    pepe juan luis jose
    luis juan jose manolo vicente alfonso __FI__

**Sample Output 0**

    3
    2
    4
    NO
    NO
    NO

**Sample Input 1**

    7
    juan adrian oriol ruben jose carlos pol
    oriol ruben fernando vicente pedro __FI__

**Sample Output 1**

    3
    4
    NO
    NO
    NO

**Sample Input 2**

    1
    luis
    __FI__

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
