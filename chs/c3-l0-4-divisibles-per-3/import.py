
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c3-l0-4-divisibles-p"
p.name="[d8601] Divisibles per 3 #for"
p.summary="Divisibles per 3"
p.description='''Imprimeix tots els nombres enters divisibles per 3 que hi ha entre  i 
(inclusiu).

**Input Format**

Dos nombres enters  i 

**Constraints**

\-

**Output Format**

S'imprimirà cada número en una línia.

**Sample Input 0**

    1 7

**Sample Output 0**

    3
    6

**Sample Input 1**

    5 10

**Sample Output 1**

    6
    9

**Sample Input 2**

    10 22

**Sample Output 2**

    12
    15
    18
    21

**Sample Input 3**

    -1 3

**Sample Output 3**

    0
    3

**Sample Input 4**

    12 45

**Sample Output 4**

    12
    15
    18
    21
    24
    27
    30
    33
    36
    39
    42
    45

**Sample Input 5**

    3 7

**Sample Output 5**

    3
    6

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
