
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c6-l3-1-triangle"
p.name="[f31a3] Triangle"
p.summary="Triangle"
p.description='''Implementa el mètodes de la classe Triangle:

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    3 4
    2 5

**Sample Output 0**

    Area triangle1: 6.00
    Area triangle2: 5.00

**Sample Input 1**

    30.77 23.5
    22.9 5.1

**Sample Output 1**

    Area triangle1: 361.55
    Area triangle2: 58.39

**Sample Input 2**

    0 89
    103 0

**Sample Output 2**

    Area triangle1: 0.00
    Area triangle2: 0.00

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
