
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="divisibles-por-7"
p.name="Divisibles por 7"
p.summary="Decir si los números leídos son divisibles por 7 o no."
p.description='''A partir de una secuencia de números, decir si cada uno de ellos es
divisible por 7 o no.

**Input Format**

Una secuencia de (N) números terminada en 0.

**Constraints**

0 \<= N \<= 10^7

**Output Format**

Un "SI" o un "NO" por cada número leído.

**Sample Input 0**

    7 4 14 3 21 49 0

**Sample Output 0**

    SI
    NO
    SI
    NO
    SI
    SI

**Sample Input 1**



**Sample Output 1**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
