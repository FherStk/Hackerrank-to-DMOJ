
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="tipus-correctes"
p.name="Tipus correctes  #variables"
p.summary="Tipus correctes"
p.description='''Completa el següent programa afegint els tipus correctes a cada
variable.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    2020
    Abril
    37.5
    false
    ;

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
