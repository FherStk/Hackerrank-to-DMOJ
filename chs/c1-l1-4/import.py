
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l1-4"
p.name="[dd35e] Llibres i prestatgeries #operadors #relacionals"
p.summary="[dd35e] Llibres i prestatgeries #operadors #relacionals"
p.description='''Per a endreçar els seus llibres, Miquel ha comprat unes prestatgeries.
Cada prestatgeria té un nombre de prestatges, i a cada prestatge hi
caben una quantitat de llibres determinada. En Miquel vol saber si ha
comprat suficients prestatges.

**Input Format**

El primer nombre  indica la quanitat de prestatgeries.

El segon nombre  indica el nombre de prestatges que té cada
prestatgeria.

El tercer nombre  indica el nombre de llibres que hi caben a cada
prestatgeria.

L'últim nombre  indica la quantitat de llibres que té en Miquel.

**Constraints**

\-

**Output Format**

 | 

**Sample Input 0**

    2 4 10 60

**Sample Output 0**

    true

**Explanation 0**

2 prestatgeries X 4 prestatges X 10 llibres = 80 llibres de capacitat

La quantitat de llibres és 60, per tant sí que hi caben

**Sample Input 1**

    10 3 5 200

**Sample Output 1**

    false

**Explanation 1**

10 prestatges X 3 prestatges X 5 llibres = 150 llibres de capacitat

La quantitat de llibres és 200, per tant no hi caben tots.

**Sample Input 2**

    1 5 10 50

**Sample Output 2**

    true

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
