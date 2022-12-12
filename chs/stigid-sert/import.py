
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="stigid-sert"
p.name="stigid serT  #operadors #aritmetics"
p.summary="stigid serT"
p.description='''Escriu un progarma que llegeixi un número de xifres, calcula un nou
número invertint els dígits, i l'imprimeix.

**Input Format**

Un enter de 3 xifres

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    976

**Sample Output 0**

    679

**Sample Input 1**

    123

**Sample Output 1**

    321

**Sample Input 2**

    320

**Sample Output 2**



**Sample Input 3**

    100

**Sample Output 3**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
