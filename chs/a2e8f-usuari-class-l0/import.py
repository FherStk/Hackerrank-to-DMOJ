
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="a2e8f-usuari-class-l0"
p.name="[a2e8f] Usuari #class #L0"
p.summary="Usuari"
p.description='''Utilitza el mètode constructor de la clase User per a crear i
inicialitzar els objectes necessaris.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**


'''
p.is_public=True
p.date=timezone.now()
p.save()
