
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="gatito-ascii-art"
p.name="Gatito ASCII-art  #literals"
p.summary="Gatito ASCII-art"
p.description='''Gatito ASCII-art (dedicado a Arnau)

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    (\___/)
    (=)
    (_(")(")

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
