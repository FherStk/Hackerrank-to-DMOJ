
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="declaracio-invalida-de-variables"
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
'''
p.is_public=True
p.date=timezone.now()
p.save()
