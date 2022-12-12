
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="f2eb6-players"
p.name="[f2eb6] Players #class #L0"
p.summary="Players"
p.description='''Crea els objectes necessaris.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    10 10
    a 2300 9 5
    b 5700 7 6

**Sample Output 0**

    P1:a #2300 {9, 5}
    P2:b #5700 {7, 6}

**Sample Input 1**

    20 20
    gcd 17900 10 10
    mcm 8000 14 3

**Sample Output 1**

    P1:gcd #17900 {10, 10}
    P2:mcm #8000 {14, 3}

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
