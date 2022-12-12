
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="iguales-al-ultimo"
p.name="[a4035] Iguals a l'últim #arrays"
p.summary="Iguals a l'últim"
p.description='''Donada una seqüència de nombres, dir quants nombres de la seqüència són
iguals a l'últim (sense comptar-se ell mateix).

**Input Format**

El primer nombre  indica la quantitat de nombres que hi ha a la
seqüència. A continuació ve la seqüència.

**Constraints**

\-

**Output Format**

La quantitat de nombres iguals a l'últim.

**Sample Input 0**

    5    
    23 34 23 45 23

**Sample Output 0**



**Sample Input 1**

    1    
    23

**Sample Output 1**



**Sample Input 2**

    5    
    12 23 34 45 56

**Sample Output 2**



**Sample Input 3**

    3    
    100 100 100

**Sample Output 3**



**Sample Input 4**

    2    
    23 23

**Sample Output 4**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
