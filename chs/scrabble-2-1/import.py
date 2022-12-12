
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="scrabble-2-1"
p.name="[C3-L2-5] Scrabble #for"
p.summary="Scrabble"
p.description='''Donada una paraula, obté la seva puntuació d'Scrabble.

    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10

**Input Format**

Una paraula

**Constraints**

\-

**Output Format**

La puntuació obtinguda

**Sample Input 0**

    hola

**Sample Output 0**



**Explanation 0**



**Sample Input 1**

    mundo

**Sample Output 1**



**Explanation 1**



**Sample Input 2**

    java

**Sample Output 2**



**Explanation 2**



**Sample Input 3**

    HACKERRANK

**Sample Output 3**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
