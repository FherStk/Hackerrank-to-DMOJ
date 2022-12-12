
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="sucesion-de-fibonacc"
p.name="[C3-L1-12] Successió de Fibonacci #for"
p.summary="Successió de Fibonacci"
p.description='''La successió de Fibonacci comença amb els nombres 0 i 1, i a partir
d'aquests, «cada terme és la suma dels dos anteriors».

![image](1556726526-96eb9e42a6-fibo1.png)

Determina si una seqüència de nombres és una successió de Fibonacci.

**Input Format**

Una seqüència de N nombres enters. La seqüència acaba amb un -1.

**Constraints**

\-

**Output Format**

"SI" o "NO"

**Sample Input 0**

    0 1    -1

**Sample Output 0**



**Sample Input 1**

    0 1 2     -1

**Sample Output 1**



**Sample Input 2**

    0 1 1 2 3 5 8 13 21 34      -1

**Sample Output 2**



**Sample Input 3**

    0 1 1    -1

**Sample Output 3**



**Sample Input 4**

    0 1 1 2 3 4     -1

**Sample Output 4**



**Sample Input 5**

    5 6 11 17 28   -1

**Sample Output 5**



**Sample Input 6**

    0 2 2 4 6 10 -1

**Sample Output 6**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
