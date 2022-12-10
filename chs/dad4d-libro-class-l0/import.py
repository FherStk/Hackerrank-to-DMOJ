
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="dad4d-libro-class-l0"
p.name="[dad4d] Libro #class #L0"
p.summary="Libro"
p.description='''Crea les classes  i 

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    C Programming Language
    978-0131103627
    4.5
    Dennis M. Ritchie
    5

**Sample Output 0**

    978-0131103627
    C Programming Language
    ****
    Dennis M. Ritchie
    *****

**Sample Input 1**

    Expert C Programming: Deep C Secrets
    978-0131774292
    4.7
    Peter van der Linden
    5

**Sample Output 1**

    978-0131774292
    Expert C Programming: Deep C Secrets
    ****
    Peter van der Linden
    *****

**Sample Input 2**

    C: A Reference Manual
    978-0130895929
    5
    Samuel P. Harbison
    5

**Sample Output 2**

    978-0130895929
    C: A Reference Manual
    *****
    Samuel P. Harbison
    *****
'''
p.is_public=True
p.date=timezone.now()
p.save()
