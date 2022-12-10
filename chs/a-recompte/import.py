
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="a-recompte"
p.name="[ddc25] Sortida en autobús  #operadors #aritmetics"
p.summary="Calcula la quantitat de passatgers"
p.description='''Per a realitzar una sortida a l'institut, s'han contractat els serveis
de dues empreses d'autocars. Cada empresa té disponibles un nombre
d'autocars.

Es vol saber la capacitat total de passatgers, per veure si hi podran
anar tots els alumnes.

**Input Format**

El primer nombre  indica els autobusos disponibles de la primera
empresa.

El segon nombre  indica els autobusos disponibles de la segona empresa.

El tercer nombre  indica la capacitat de passatgers d'un autobús.

**Constraints**

\-

**Output Format**

Un número indicant la capacitat total de passatagers

**Sample Input 0**

    2 3 50

**Sample Output 0**

    250

**Sample Input 1**

    1 2 25

**Sample Output 1**



**Sample Input 2**

    0 0 50

**Sample Output 2**



**Sample Input 3**

    2 0 30

**Sample Output 3**


'''
p.is_public=True
p.date=timezone.now()
p.save()
