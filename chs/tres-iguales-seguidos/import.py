
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="tres-iguales-seguido"
p.name="Tres iguales seguidos"
p.summary="Decir si hay tres números iguales seguidos."
p.description='''A partir de una serie de secuencias de números, decir si en cada una de
ellas hay tres números iguales seguidos.

**Input Format**

El primer número T indica la cantidad de secuencias que vienen a
continuación. Cada secuencia de N números termina con un 0.

**Constraints**

1 \<= T \<= 100 1 \<= N \<= 10^7

**Output Format**

Un "SI" o un "NO" por cada secuencia de números leída; separados por un
salto de línea.

**Sample Input 0**

    3
    1 4 3 5 5 5 6 8 5 3 8 9 5 5 5 8 7 3 5 0
    1 3 5 7 9 0
    1 1 1 0

**Sample Output 0**

    SI
    NO
    SI

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
