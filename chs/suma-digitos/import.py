
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="suma-digitos"
p.name="[C3-L1-6] Suma dígits #for"
p.summary="Suma dígits"
p.description='''Donada una seqüència de nombres de 4 dígits, suma cadscun dels seus
dígits.

**Input Format**

Una seqüència d' nombres. La seqüència acaba amb un 0.

**Constraints**

\-

**Output Format**

La suma dels dígits de cada nombre, separats per un salt de línia

**Sample Input 0**

    1111 2222 1234 1000 0

**Sample Output 0**

    4
    8
    10
    1

**Sample Input 1**

    1111 1111 1111 1111 1111 0

**Sample Output 1**

    4
    4
    4
    4
    4

**Sample Input 2**

    1234 4321 0

**Sample Output 2**

    10
    10

**Sample Input 3**

    0001 0010 0100 1000 0

**Sample Output 3**

    1
    1
    1
    1

**Sample Input 4**

    0001 0020 0300 4000 0

**Sample Output 4**

    1
    2
    3
    4

**Sample Input 5**

    0001 0002 0003 0004 0005 0006 0007 0

**Sample Output 5**

    1
    2
    3
    4
    5
    6
    7

**Sample Input 6**

    5476 9184 8794 7623 1862 4729 8248 0

**Sample Output 6**

    22
    22
    28
    18
    17
    22
    22

**Sample Input 7**

    8746 3794 8736 8302 7019 0987 8210 9302 2948 1429 9542 0980 0098 3424 0

**Sample Output 7**

    25
    23
    24
    13
    17
    24
    11
    14
    23
    16
    20
    17
    17
    13

**Sample Input 8**

    1111 0

**Sample Output 8**



**Sample Input 9**


'''
p.is_public=True
p.date=timezone.now()
p.save()
