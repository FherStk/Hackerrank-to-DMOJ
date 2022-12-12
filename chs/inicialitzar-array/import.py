
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="inicialitzar-array"
p.name="Inicialitzar array  #arrays"
p.summary="Inicialitzar array"
p.description='''Incialitza l'array d'enters anomenat  amb cinc elements
.

Utilitza la plantilla proporcionada.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    12
    17
    8
    101
    33

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
