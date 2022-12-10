
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="einstein"
p.name="Cita Einstein #literals"
p.summary="Cita Einstein"
p.description='''Escriu un programa Java que mostri aquesta cita d'Einstein:

    Life is like riding a bicycle. To keep your balance you must keep moving.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    Life is like riding a bicycle. To keep your balance you must keep moving.
'''
p.is_public=True
p.date=timezone.now()
p.save()
