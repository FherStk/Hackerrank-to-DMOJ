
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="estan-todos"
p.name="[d89d7] Hi sou tots i totes?"
p.summary="Hi sou tots i totes?"
p.description='''En una sortida escolar, la mestra posa una enganxina a cada nen i nena
amb un número correlatiu.

Quan arriba el moment de pujar a l'autobús els nens i nenes van pujant i
la mestra va marcant a la seva llibreta els números dels que hi van
pujant.

![image](1556784726-b0d72bdd6a-schoolsbus.png)

Quan han pujat tots els alumnes, la mestra revisa les seves anotacions
per veure si estan tots els alumnes.

**Input Format**

El primer número  indica el nombre d'alumnes. A continuació ve la
seqüència de números.

**Constraints**

\-

**Output Format**

"SI" si han pujat tots els alumnes. "NO" en cas contrari.

**Sample Input 0**

    5 
    1 2 3 4 5

**Sample Output 0**



**Sample Input 1**

    5 
    1 1 2 3 4

**Sample Output 1**



**Sample Input 2**

    10 
    3 2 4 5 3 6 5 7 8 9

**Sample Output 2**



**Sample Input 3**

    10 
    5 3 4 10 6 8 7 1 9 2

**Sample Output 3**



**Sample Input 4**

    1 
    1

**Sample Output 4**



**Sample Input 5**

    1 
    23

**Sample Output 5**



**Sample Input 6**

    10 
    3 2 4 5 3 6 5 7 8 10

**Sample Output 6**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
