
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="posicion-en-el-alfab"
p.name="[f1dc8] Posició a l'alfabet"
p.summary="Posició a l'alfabet"
p.description='''Donat un text, indica la posició que ocupa cada lletra del text a
l'alfabet.

**Input Format**

String

**Constraints**

\-

**Output Format**

La posició de cada lletra en una línia diferent.

**Sample Input 0**

    hola

**Sample Output 0**

    7
    14
    11
    0

**Sample Input 1**

    mon

**Sample Output 1**

    12
    14
    13

**Sample Input 2**

    java

**Sample Output 2**

    9
    0
    21
    0

**Sample Input 3**

    tochararray

**Sample Output 3**

    19
    14
    2
    7
    0
    17
    0
    17
    17
    0
    24

**Sample Input 4**

    jived fox nymph grabs quick waltz

**Sample Output 4**

    9
    8
    21
    4
    3
    5
    14
    23
    13
    24
    12
    15
    7
    6
    17
    0
    1
    18
    16
    20
    8
    2
    10
    22
    0
    11
    19
    25

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
