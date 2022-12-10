
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="e33c4-full-de-notes"
p.name="[e33c4] Full de notes #for"
p.summary="Full de notes"
p.description='''![image](1580920290-fe8cff42df-media.png)

**Input Format**

La entrada és la matriu de notes

**Constraints**

\-

**Output Format**

S'imprimirà la matriu de notes, afegint la columna de la mitjana.

**Sample Input 0**

    3 4
    4 6 5 5
    8 8 6 6
    4 5 6 5

**Sample Output 0**

    4 6 5 5 5.0
    8 8 6 6 7.0
    4 5 6 5 5.0

**Sample Input 1**

    4 3
    4 6 5
    8 8 6
    4 5 6
    9 6 5

**Sample Output 1**

    4 6 5 5.0
    8 8 6 7.3333335
    4 5 6 5.0
    9 6 5 6.6666665

**Sample Input 2**

    2 6
    4 6 5 8 8 6
    4 5 6 9 6 5

**Sample Output 2**

    4 6 5 8 8 6 6.1666665
    4 5 6 9 6 5 5.8333335
'''
p.is_public=True
p.date=timezone.now()
p.save()
