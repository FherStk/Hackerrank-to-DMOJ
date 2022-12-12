
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c7-l3-1-palindrom"
p.name="[C7-L3-1] Palíndrom #recursivitat"
p.summary="Palíndrom"
p.description='''Donat un String, dir si és un palíndrom.

**Input Format**

String

**Constraints**

No hi ha

**Output Format**

{ true | false }

**Sample Input 0**



**Sample Output 0**

    true

**Sample Input 1**



**Sample Output 1**

    true

**Sample Input 2**

    abba

**Sample Output 2**

    true

**Sample Input 3**

    abcba

**Sample Output 3**

    true

**Sample Input 4**

    abcb

**Sample Output 4**

    false

**Sample Input 5**

    abcdcb

**Sample Output 5**

    false

**Sample Input 6**

    abcdcbaa

**Sample Output 6**

    false

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
