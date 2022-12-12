
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="mezcla-de-secuencias"
p.name="[f1762] Mescla de seqüències #array"
p.summary="Mescla de seqüències"
p.description='''Donades dues seqüències de nombres, s'ha d'obtenir una mescla d'elles.

Per a obtenir la mescla s'ha d'agafar un element de cada seqüència
alternativament. És a dir, primer un nombre de la primera seqüència,
després un altre de la segona, i així successivament. Quan en una
seqüència ja no queden més nombres, s'agafaran els nombres que quedin
de l'altra.

**Input Format**

La entrada consta de des seqüències.

Per a cada seqüència, el primer nombre  indica el tamany. A continuació
ve la seqüència.

**Constraints**

\-

**Output Format**

La seqüència resultant.

**Sample Input 0**

    3    100 200 300
    3    400 500 600

**Sample Output 0**

    100 400 200 500 300 600

**Sample Input 1**

    5    10 11 12 13 14
    5    20 21 22 23 24

**Sample Output 1**

    10 20 11 21 12 22 13 23 14 24

**Sample Input 2**

    1    1000
    1    2000

**Sample Output 2**

    1000 2000

**Sample Input 3**

    4    1 2 3 4
    3    1 2 3

**Sample Output 3**

    1 1 2 2 3 3 4

**Sample Input 4**

    6    1 2 3 4 5 6
    3    1 2 3

**Sample Output 4**

    1 1 2 2 3 3 4 5 6

**Sample Input 5**

    3    10 20 30
    6    10 20 30 40 50 60

**Sample Output 5**

    10 10 20 20 30 30 40 50 60

**Sample Input 6**

    6     76 65 98 45 32 21
    3     99 88 77

**Sample Output 6**

    76 99 65 88 98 77 45 32 21

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
