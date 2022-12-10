
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="el-primo-del-pueblo"
p.name="El primo del pueblo"
p.summary="Di si un número es primo o no"
p.description='''Dado un número, di si es primo o no.

**Input Format**

Un número N

**Constraints**

1 \<= N \<= 10^9

**Output Format**

true | false

**Sample Input 0**



**Sample Output 0**

    false

**Sample Input 1**



**Sample Output 1**

    true

**Sample Input 2**



**Sample Output 2**

    true

**Sample Input 3**



**Sample Output 3**

    true

**Sample Input 4**



**Sample Output 4**

    false

**Sample Input 5**



**Sample Output 5**

    true

**Sample Input 6**



**Sample Output 6**

    true

**Sample Input 7**



**Sample Output 7**

    false

**Sample Input 8**



**Sample Output 8**

    true
'''
p.is_public=True
p.date=timezone.now()
p.save()
