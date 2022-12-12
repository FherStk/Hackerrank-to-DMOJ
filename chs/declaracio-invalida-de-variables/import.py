
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="declaracio-invalida-"
p.name="Declaració invàlida de variables  #variables"
p.summary="Declaració invàlida de variables"
p.description='''Donades dues variables  i  amb declaracions invàlides, afegeix el
tipus correcte.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    3943574

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
