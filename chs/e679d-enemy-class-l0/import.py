
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="e679d-enemy-class-l0"
p.name="[e679d] Enemy #class #L0"
p.summary="Enemy"
p.description='''Implementa les classes necessàries

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    GUERRERO  Health: 50/50   Weapon: 60/60
    AMAZONA   Health: 40/40   Weapon: 70/70
    BRUJO     Health: 30/30   Weapon: 80/80
'''
p.is_public=True
p.date=timezone.now()
p.save()
