
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c7-l1-2-factorial"
p.name="[C7-L1-2] Factorial #recursivitat"
p.summary="Factorial"
p.description='''Escriu un algorisme recursiu per a calcular el factorial d'un nombre:

Exemple

    5! = 5*4*3*2*1 = 120

**Input Format**

Un nombre enter

**Constraints**

No hi ha

**Output Format**

El factorial

**Sample Input 0**



**Sample Output 0**



**Sample Input 1**



**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Sample Input 3**



**Sample Output 3**

    120

**Sample Input 4**



**Sample Output 4**

    3628800

**Sample Input 5**



**Sample Output 5**

    2004310016

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
