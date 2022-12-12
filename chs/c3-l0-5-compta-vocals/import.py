
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c3-l0-5-compta-vocal"
p.name="[e31b2] Filtra vocals #for"
p.summary="Filtra vocals"
p.description='''Donada una llista de lletres, imprimeix únicament les vocals que hi
hagi.

**Input Format**

L'entrada consta de dues parts:

  - Primer s'indica la quantitat de lletres

  - A continuació venen les lletres, en minúscules i separades per
    espais en blanc

**Constraints**

\-

**Output Format**

S'imprimirà cada vocal en una línia

**Sample Input 0**

    3
    a b c

**Sample Output 0**



**Sample Input 1**

    5
    a b c d e

**Sample Output 1**

    a
    e

**Sample Input 2**

    5
    a x e x a

**Sample Output 2**

    a
    e
    a

**Sample Input 3**

    10
    i j u k i l l o m a

**Sample Output 3**

    i
    u
    i
    o
    a

**Sample Input 4**

    20
    a e t h v u i e a o c x u i a o e u l o

**Sample Output 4**

    a
    e
    u
    i
    e
    a
    o
    u
    i
    a
    o
    e
    u
    o

**Sample Input 5**

    1
    a

**Sample Output 5**



**Sample Input 6**

    5
    x u v z i

**Sample Output 6**

    u
    i

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
