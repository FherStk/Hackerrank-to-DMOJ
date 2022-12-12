
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="randomsix"
p.name="[C3-L1-8] RandomSix #for"
p.summary="RandomSix"
p.description='''Donat un nombre inicial de dues xifres (al que anomenarem llavor),
genera una seqüència de nombres a partir d'aquest.

Per generar un nou nombre, multiplica la xifra de les unitats per sis, i
suma-li la xifra de les desenes. El nombre generat pasarà a ser la
llavor per al següent nombre.

Exemple:

Llavor inicial = 13

13 --\> 19 --\> 55 --\> 35 --\> 33 --\> 21 --\> 08 --\> 35 --\> ...

    13 => 1 + 3*6 = 19
    19 => 1 + 9*6 = 55
    55 => 5 + 5*6 = 35
    35 => 3 + 5*6 = 33
    33 => 3 + 3*6 = 21
    21 => 2 + 1*6 = 8
    8  => 0 + 8*6 = 48
    48 => 4 + 8*6 = 52
    ...

**Input Format**

La entrada consisteix en dos nombres.

El primer nombre  és la llavor inicial.

El segon nombre  és la quantitat de nombres a generar.

**Constraints**

\-

**Output Format**

La seqüència de nombres generada, separats per un salt de línía.

**Sample Input 0**

    13
    10

**Sample Output 0**

    19
    55
    35
    33
    21
    8
    48
    52
    17
    43

**Sample Input 1**

    35
    4

**Sample Output 1**

    33
    21
    8
    48

**Sample Input 2**

    27
    5

**Sample Output 2**

    44
    28
    50
    5
    30

**Sample Input 3**

    10
    3

**Sample Output 3**

    1
    6
    36

**Sample Input 4**

    1 19

**Sample Output 4**

    6
    36
    39
    57
    47
    46
    40
    4
    24
    26
    38
    51
    11
    7
    42
    16
    37
    45
    34

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
