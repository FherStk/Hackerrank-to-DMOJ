
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="xirtam"
p.name="Xirtam #arrays"
p.summary="Xirtam"
p.description='''Donada una matriu, imprimeix-la amb els 0 canviats per 1, i els 1
canviats per 0.

**Input Format**

El primer nombre  indica les files que té la matriu.

El segon nombre  indica les columnes que té la matriu.

A continuació venen els números de la matriu.

**Constraints**

\-

**Output Format**

S'imprimirà la matriu, separant els números amb espais en blanc.

**Sample Input 0**

    4 5
    1 0 1 0 0
    0 1 1 0 1
    1 1 0 0 0
    1 0 1 1 0

**Sample Output 0**

    0 1 0 1 1
    1 0 0 1 0
    0 0 1 1 1
    0 1 0 0 1

**Sample Input 1**

    3 3
    1 1 1
    0 0 0
    1 1 1

**Sample Output 1**

    0 0 0
    1 1 1
    0 0 0

**Sample Input 2**

    1 5
    1 1 0 1 1

**Sample Output 2**

    0 0 1 0 0

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
