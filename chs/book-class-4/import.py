
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="book-class-4"
p.name="Book #class"
p.summary="Book"
p.description='''Defineix la classe Book. Ha de contenir tres camps: camp string ,
camp enter  i camp booleà .

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    Through the looking glass
    1871
    true

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
