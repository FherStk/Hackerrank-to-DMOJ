
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="ordenar-secuencia"
p.name="[c9ac3] Ordenar seqüència"
p.summary="Ordenar seqüència"
p.description='''Donada una seqüència de números, ordenar-la en ordre **ascendent**.

**Input Format**

El primer número  indica el tamany de la seqüència. A continuació ve la
seqüència.

**Constraints**

\-

**Output Format**

La seqüència ordenada de números, separats per espais.

**Sample Input 0**

    5    20 10 40 50 30

**Sample Output 0**

    10 20 30 40 50

**Sample Input 1**

    5    50 40 30 20 10

**Sample Output 1**

    10 20 30 40 50

**Sample Input 2**

    1   500

**Sample Output 2**

    500

**Sample Input 3**

    10    6 3 7 56 4 7 4 4 9 3

**Sample Output 3**

    3 3 4 4 4 6 7 7 9 56

**Sample Input 4**

    3    1 1 1

**Sample Output 4**

    1 1 1

**Sample Input 5**



**Sample Output 5**

    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
