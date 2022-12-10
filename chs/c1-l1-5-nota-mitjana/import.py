
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l1-5-nota-mitjana"
p.name="[fa2d9] Nota mitjana  #operadors aritmètics"
p.summary="Calcula la nota mitjana"
p.description='''Donades les notes de 3 exàmens, calcula la seva mitjana.

**Input Format**

El primer nombre  és la nota del primer examen.

El segon nombre  és la nota del segon examen.

El tercer nombre  és la nota del tercer examen.

**Constraints**

\-

**Output Format**

La nota mitjana

**Sample Input 0**

    0 5 10

**Sample Output 0**

    5.0

**Sample Input 1**

    5 7.5 10

**Sample Output 1**

    7.5

**Sample Input 2**

    6.75 7.25 8.4

**Sample Output 2**

    7.4666667
'''
p.is_public=True
p.date=timezone.now()
p.save()
