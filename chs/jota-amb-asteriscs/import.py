
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="jota-amb-asteriscs"
p.name="Jota amb asteriscs  #literals"
p.summary="Jota amb asteriscs"
p.description='''Escriu un programa que imprimeixi la lletra  amb asteriscs.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    ********
          **
          **
          **
    **    **
    **    **
     *******

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
