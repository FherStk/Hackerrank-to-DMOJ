
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="assignacions"
p.name="Assignacions  #variables"
p.summary="Assignacions"
p.description='''Canvia el codi següent per fer que la sortida sigui aquesta:

    3 4 5

Per fer-ho, assigna correctament els valors a les variables.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    3 5 4

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
