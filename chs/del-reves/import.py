
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="del-reves"
p.name="[a67a1] Del revés #arrays"
p.summary="Del revés"
p.description='''Donada una seqüència de números, mostrar-la en ordre invers.

**Input Format**

El primer número  indica la quantitat de números que hi ha en la
seqüència.

A continuació venen els números de la seqüència.

**Constraints**

\-

**Output Format**

La seqüència de números en ordre invers, separats per espais.

**Sample Input 0**

    5 
    100 200 300 400 500

**Sample Output 0**

    500 400 300 200 100

**Sample Input 1**

    3 
    23 56 45

**Sample Output 1**

    45 56 23

**Sample Input 2**

    1 
    1000

**Sample Output 2**

    1000

**Sample Input 3**

    10 
    3 1 4 2 6 5 4 7 6 9

**Sample Output 3**

    9 6 7 4 5 6 2 4 1 3

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
