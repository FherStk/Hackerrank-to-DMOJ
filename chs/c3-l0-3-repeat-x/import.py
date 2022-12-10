
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c3-l0-3-repeat-x"
p.name="[b8703] Repeat X #for"
p.summary="Repeat X"
p.description='''Donat un nombre , imprimeix-lo  vegades.

**Input Format**

Un enter 

**Constraints**

\-

**Output Format**

S'imprimrà el nombre repetit.

**Sample Input 0**



**Sample Output 0**

    333

**Sample Input 1**



**Sample Output 1**

    4444

**Sample Input 2**



**Sample Output 2**

    55555

**Sample Input 3**



**Sample Output 3**

    10101010101010101010

**Sample Input 4**



**Sample Output 4**

    25252525252525252525252525252525252525252525252525

**Sample Input 5**



**Sample Output 5**



**Sample Input 6**

    100

**Sample Output 6**

    100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100
'''
p.is_public=True
p.date=timezone.now()
p.save()
