
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="de-0-a-4"
p.name="De 0 a 4 #literals"
p.summary="De 0 a 4"
p.description='''Escriu un programa que imprimeixi els números de  a  inclusive.
Cada nombre ha d'estar en una nova línia.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    0
    1
    2
    3
    4
'''
p.is_public=True
p.date=timezone.now()
p.save()
