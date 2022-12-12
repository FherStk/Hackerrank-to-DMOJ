
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c3-l0-1-linia-de-pun"
p.name="[b9c97] Línia de punts #for"
p.summary="Línia de punts"
p.description='''Pinta una línia amb la quantitat de punts indicada.

**Input Format**

Un nombre enter .

**Constraints**

\-

**Output Format**

{ . } 

**Sample Input 0**



**Sample Output 0**

    ...

**Sample Input 1**



**Sample Output 1**

    .....

**Sample Input 2**



**Sample Output 2**

    ..........

**Sample Input 3**



**Sample Output 3**

    ....................

**Sample Input 4**

    100

**Sample Output 4**

    ....................................................................................................

**Sample Input 5**

    229

**Sample Output 5**

    .....................................................................................................................................................................................................................................

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
