
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="arrodonir-la-nota"
p.name="Arrodonir la nota  #conversio"
p.summary="Arrodonir la nota"
p.description='''Al butlletí de notes no es poden posar notes amb decimals, així que el
professor ha decidit arrodonir-les. Si els decimals estan per sota de
0.5 es trunca la nota (es lleven els decimals), però si són igual o
majors que 0.5 aleshores s'arrodoneix cap amunt.

**Input Format**

Una nota amb o sense decimals

**Constraints**

\-

**Output Format**

enter

**Sample Input 0**

    5.1

**Sample Output 0**



**Sample Input 1**

    7.49

**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Sample Input 3**

    4.5

**Sample Output 3**



**Sample Input 4**

    7.75

**Sample Output 4**



**Sample Input 5**



**Sample Output 5**


'''
p.is_public=True
p.date=timezone.now()
p.save()
