
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c3-l0-2-interval"
p.name="[dd3ea] Interval #for"
p.summary="Interval"
p.description='''Imprimeix tots els nombres enters X que hi ha entre dos nombres  i 
(exclusiu).

**Input Format**

Dos nombres enters  i .

**Constraints**

\-

**Output Format**

S'imprimiran els nombres de l'interval, sense separació entre ells.

**Sample Input 0**

    2 6

**Sample Output 0**

    2345

**Sample Input 1**

    4 9

**Sample Output 1**

    45678

**Sample Input 2**

    10 15

**Sample Output 2**

    1011121314

**Sample Input 3**

    0 25

**Sample Output 3**

    0123456789101112131415161718192021222324

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
