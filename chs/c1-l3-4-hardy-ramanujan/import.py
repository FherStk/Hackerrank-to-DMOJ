
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l3-4-hardy-ramanu"
p.name="[d59ab] Hardy-Ramanujan #operadors"
p.summary="Hardy-Ramanujan"
p.description='''Desde que va llegir sobre el matemàtic Ramanujan, busca el nombre 1729
per tot arreu: a les matrícules dels cotxes, als números de telèfon, a
les tarjetes bancàries, ...

Especialment a les tarjetes busca que sigui un dels grups de nombres de
4 xifres.

![image](1556298623-afb0e1cb38-creditcard.png)

**Input Format**

La entrada consisteix en un nombre  de tarjeta bancària.

**Constraints**

\-

**Output Format**

si el 1729 es un dels grups de 4 xifres

si no ho és

**Sample Input 0**

    1111222233334444

**Sample Output 0**

    false

**Sample Input 1**

    1111222233331729

**Sample Output 1**

    true

**Sample Input 2**

    1111222217294444

**Sample Output 2**

    true

**Sample Input 3**

    1111172933334444

**Sample Output 3**

    true

**Sample Input 4**

    1729222233334444

**Sample Output 4**

    true

**Sample Input 5**

    1117292233334444

**Sample Output 5**

    false

**Sample Input 6**

    1111221729334444

**Sample Output 6**

    false

**Sample Input 7**

    1111222233317294

**Sample Output 7**

    false

**Sample Input 8**

    0000000017290000

**Sample Output 8**

    true

**Sample Input 9**

    0000000000001729

**Sample Output 9**

    true

**Sample Input 10**

    1234567891234567

**Sample Output 10**

    false

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
