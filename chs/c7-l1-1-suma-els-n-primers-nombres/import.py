
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c7-l1-1-suma-els-n-primers-nombres"
p.name="[C7-L1-1] Suma els n primers nombres #recursivitat"
p.summary="Suma els n primers nombres"
p.description='''Escriu un algorisme recursiu per a sumar els n primers nombres.

Exemple:

    n=10 -> 1+2+3+4+5+6+7+8+9+10=55

**Input Format**

Un nombre enter

**Constraints**

No hi ha

**Output Format**

La suma

**Sample Input 0**



**Sample Output 0**



**Sample Input 1**



**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Sample Input 3**



**Sample Output 3**

    210

**Sample Input 4**

    1000

**Sample Output 4**

    500500
'''
p.is_public=True
p.date=timezone.now()
p.save()
