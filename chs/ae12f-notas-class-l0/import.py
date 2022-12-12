
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="ae12f-notas-class-l0"
p.name="[ae12f] Notas #class #L0"
p.summary="Notas"
p.description='''Crea la classe Alumne

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    5
    9 5.6 7 7.5 6.4

**Sample Output 0**

    Nota media: 7.1

**Sample Input 1**

    3
    10 5 0

**Sample Output 1**

    Nota media: 5.0

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
