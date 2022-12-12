
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="noms-correctes"
p.name="Noms correctes  #variables"
p.summary="Noms correctes"
p.description='''Dona el nom que li pertoca a cada variable.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    Java 15 incorpora Text Blocks, que es delimiten amb """

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
