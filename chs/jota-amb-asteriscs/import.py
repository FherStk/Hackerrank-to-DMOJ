
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
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
'''
p.is_public=True
p.date=timezone.now()
p.save()
