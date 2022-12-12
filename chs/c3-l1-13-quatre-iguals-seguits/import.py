
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c3-l1-13-quatre-igua"
p.name="[C3-L1-13] Quatre iguals seguits #for"
p.summary="Quatre iguals seguits"
p.description='''Donada una seqüència de números, digues quantes vegades apareixen 4
números iguals seguits.

**Input Format**

Una seqüència d'enters acabada amb 

**Constraints**

\-

**Output Format**

El número de vegades apareixen 4 números iguals seguits.

**Sample Input 0**

    1 1 1 1 2   -1

**Sample Output 0**



**Sample Input 1**

    1 1 1 1 1 2     -1

**Sample Output 1**



**Sample Input 2**

    1 1 1 2 2 2 2 1    -1

**Sample Output 2**



**Sample Input 3**

    1 1 1 1 1 1 1 2     -1

**Sample Output 3**



**Sample Input 4**

    1 2 2 2 2 1 1 1 1 2 2 2 2 1    -1

**Sample Output 4**



**Sample Input 5**

    1 2 1 2 1 2 1 1 1   -1

**Sample Output 5**



**Sample Input 6**

    1 2 2 3 3 3 4 4 4 4   -1

**Sample Output 6**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
