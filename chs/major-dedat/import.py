
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="major-dedat"
p.name="Major d'edat  #operadors #relacionals"
p.summary="Major d'edat"
p.description='''Escriu un programa que llegeix l'edat d'una persona i diu si té al menys
18 anys.

**Input Format**

un enter

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**



**Sample Output 0**

    false

**Sample Input 1**



**Sample Output 1**

    true

**Sample Input 2**



**Sample Output 2**

    true

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
