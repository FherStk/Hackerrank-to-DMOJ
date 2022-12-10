
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l1-10-comptant-els-minuts-per-cap-dany"
p.name="[c352b] Comptant els minuts per cap d'any  #operadors #aritmetics"
p.summary="Comptant els minuts per cap d'any"
p.description='''Ramon es passa el dia de cap d'any mirant el rellotge comptant els
minuts que falten per al raïm.

**Input Format**

El primer nombre  indica les hores que marca el rellotge

El segon nombre  indica els minuts que marca el rellotge

**Constraints**

\-

**Output Format**

Els minuts que falten per a les campanades.

**Sample Input 0**

    23 59

**Sample Output 0**



**Explanation 0**

Falta 1 minut per a les campanades

**Sample Input 1**

    23 00

**Sample Output 1**



**Sample Input 2**

    00 00

**Sample Output 2**

    1440

**Explanation 2**

Queden 1440 minuts (tot el dia)

**Sample Input 3**

    12 33

**Sample Output 3**

    687
'''
p.is_public=True
p.date=timezone.now()
p.save()
