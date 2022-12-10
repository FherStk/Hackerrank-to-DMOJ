
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
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
'''
p.is_public=True
p.date=timezone.now()
p.save()
