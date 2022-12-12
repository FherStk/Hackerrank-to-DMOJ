
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="sucesion-capicua"
p.name="[a02d0] Capicua #arrays"
p.summary="Capicua"
p.description='''Donada una seqüència de números, dir si és capicua.

**Input Format**

El primer número  indica la quantitat de números que hi ha en la
seqüència. A continuació ve la seqüència.

**Constraints**

\-

**Output Format**

"SI" si la seqüència és capicua. "NO" si no ho és.

**Sample Input 0**

    5    100 200 300 200 100

**Sample Output 0**



**Sample Input 1**

    6    100 200 300 300 200 100

**Sample Output 1**



**Sample Input 2**

    1    100

**Sample Output 2**



**Sample Input 3**

    2    100 100

**Sample Output 3**



**Sample Input 4**

    4    100 100 200 100

**Sample Output 4**



**Sample Input 5**

    3    100 100 200

**Sample Output 5**



**Sample Input 6**

    20    1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1

**Sample Output 6**



**Sample Input 7**

    7
    1 2 3 4 3 90 1

**Sample Output 7**



**Sample Input 8**

    6
    1 2 3 3 90 1

**Sample Output 8**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
