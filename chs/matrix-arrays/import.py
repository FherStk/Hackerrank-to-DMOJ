
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="matrix-arrays"
p.name="Matrix #arrays"
p.summary="Matrix"
p.description='''Donada la següent matriu, compta el número de zeros i uns que hi ha.

**Input Format**

El primer nombre  indica les files que té la matriu.

El segon nombre  indica les columnes que té la matriu.

A continuació venen els números de la matriu.

**Constraints**

\-

**Output Format**

S'imprimiran el nombre de zeros i uns separats per espai en blanc

**Sample Input 0**

    2 4
    0 1 0 1
    1 1 1 0

**Sample Output 0**

    3 5

**Sample Input 1**

    4 6
    1 1 0 1 0 0
    1 1 1 0 1 0
    0 1 0 1 1 0
    1 0 1 1 1 1

**Sample Output 1**

    9 15

**Sample Input 2**

    5 3
    1 0 0
    0 1 0
    0 1 1
    1 1 0
    1 1 1

**Sample Output 2**

    6 9

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
