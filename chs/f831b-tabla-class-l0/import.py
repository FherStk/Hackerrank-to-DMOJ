
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="f831b-tabla-class-l0"
p.name="[f831b] Taula #class #L0"
p.summary="Taula"
p.description='''Completa els constructors de els classes Taula, Fila, Columna i Casella

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    3 3 a

**Sample Output 0**

    aaa
    aaa
    aaa

**Sample Input 1**

    2 10 z

**Sample Output 1**

    zzzzzzzzzz
    zzzzzzzzzz

**Sample Input 2**

    7 25 x

**Sample Output 2**

    xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxx
'''
p.is_public=True
p.date=timezone.now()
p.save()
