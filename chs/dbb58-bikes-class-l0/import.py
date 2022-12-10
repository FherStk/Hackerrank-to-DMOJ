
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="dbb58-bikes-class-l0"
p.name="[dbb58] Bikes #class #L0"
p.summary="Bikes"
p.description='''Implementa el mètode Race.fastest()

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    3
    10 20 30

**Sample Output 0**



**Sample Input 1**

    4
    20 30 20 10

**Sample Output 1**



**Sample Input 2**

    2
    40 30

**Sample Output 2**



**Sample Input 3**



**Sample Output 3**

    No bikes
'''
p.is_public=True
p.date=timezone.now()
p.save()
