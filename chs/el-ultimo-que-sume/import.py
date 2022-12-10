
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="el-ultimo-que-sume"
p.name="[a86f2] L'últim que sumi #arrays"
p.summary="L'últim que sumi"
p.description='''Donada una seqüència de números, s'ha de sumar l'últim nombre de dita
seqüència a tots els números (inclòs ell mateix).

**Input Format**

El primer nombre  indica la quantitat de nombres que hi ha a la
seqüència. A continuació ve la seqüència de nombres.

**Constraints**

\-

**Output Format**

La seqüència resultant

**Sample Input 0**

    5    
    100 200 300 400 500

**Sample Output 0**

    600 700 800 900 1000

**Sample Input 1**

    10    
    3 5 2 4 3 6 5 4 8 1

**Sample Output 1**

    4 6 3 5 4 7 6 5 9 2

**Sample Input 2**

    4    
    23 34 45 10

**Sample Output 2**

    33 44 55 20

**Sample Input 3**

    1    
    10

**Sample Output 3**



**Sample Input 4**

    8
    4 6 3 4 5 6 4 0

**Sample Output 4**

    4 6 3 4 5 6 4 0
'''
p.is_public=True
p.date=timezone.now()
p.save()
