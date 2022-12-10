
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="d1e2a-contact-class-l0"
p.name="[d1e2a] Contact #class #L0"
p.summary="Contact"
p.description='''Assigna els valors dels camps a partir de les dades de l'entrada.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    Adrian
    Droide Perez
    C/Calleja, 2
    09876
    Barcelona
    Barcelona

**Sample Output 0**

    Droide Perez, Adrian
    C/Calleja, 2
    09876 - Barcelona
    Barcelona

**Sample Input 1**

    Alba
    Bosa Garcia
    C/Callejon, 4, 3a
    01234
    Madrid
    Madrid

**Sample Output 1**

    Bosa Garcia, Alba
    C/Callejon, 4, 3a
    01234 - Madrid
    Madrid
'''
p.is_public=True
p.date=timezone.now()
p.save()
