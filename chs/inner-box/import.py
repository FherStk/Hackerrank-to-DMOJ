
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="inner-box"
p.name="Inner Box #class"
p.summary="Inner Box"
p.description='''Defineix una classe anomenada . Ha de tenir quatre camps: ,
 i  de tipus float, i un camp  del mateix tipus
que la classe definida.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    4.75

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
