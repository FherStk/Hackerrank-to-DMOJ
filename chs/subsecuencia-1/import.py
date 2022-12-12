
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="subsecuencia-1"
p.name="[e2368] Subseqüència"
p.summary="Subseqüència"
p.description='''Donades dues seqüències de números, dir si la primera es troba (de forma
correlativa) a dintre de la segona.

Exemple 1:

    13 21 11
    8 34 13 21 11 23

SI (La primera seqüència es troba a dintre de la segona)

Exemple 2:

    4 1 5
    4 1 7 5

NO (La primera seqüència no es troba a dintre de la segona)

**Input Format**

La entrada consisteix en una primera seqüència d'  números, i una segona
d'  números.

**Constraints**

\-

**Output Format**

"SI" o "NO"

**Sample Input 0**

    2 111 111
    2 111 111

**Sample Output 0**



**Sample Input 1**

    4    11 22 33 44
    3    11 22 33

**Sample Output 1**



**Sample Input 2**

    4    11 22 33 44
    5    11 22 33 55 44

**Sample Output 2**



**Sample Input 3**

    3     7 8 9
    10    1 2 3 4 5 6 7 8 9 10

**Sample Output 3**



**Sample Input 4**

    1    1
    4    2 3 1 4

**Sample Output 4**



**Sample Input 5**

    3    11 22 33
    3    33 22 11

**Sample Output 5**



**Sample Input 6**

    3    4 6 5
    5    3 2 465 7 8

**Sample Output 6**



**Sample Input 7**

    3    3 5 4
    6    3 5 4 3 5 4

**Sample Output 7**



**Sample Input 8**

    3    3 5 4
    5    1 2 3 5 4

**Sample Output 8**



**Sample Input 9**

    3   7 8 9
    8   1 7 8 1 1 7 8 9

**Sample Output 9**



**Sample Input 10**

    3   7 8 9
    5   1 1 1 7 8

**Sample Output 10**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
