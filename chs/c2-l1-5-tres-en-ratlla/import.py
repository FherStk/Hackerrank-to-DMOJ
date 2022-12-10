
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c2-l1-5-tres-en-ratlla"
p.name="[C2-L2-1] Tres en ratlla #if"
p.summary="Tres en ratlla"
p.description='''Donat un tauler de tres en ratlla, determina el guanyador, o si hi ha
empat.

**Input Format**

El tauler consta de nou nombres corresponents a les nou caselles.

Les caselles buides es marquen amb un 0.

Les caselles amb una fitxa es marquen amb un 1 o un 2.

**Constraints**

El tauler és vàlid.

**Output Format**

Jugador1 | Jugador2 | Empat

**Sample Input 0**

    1 2 2
    1 2 2
    1 0 0

**Sample Output 0**

    Jugador1

**Sample Input 1**

    1 2 2
    2 1 0
    2 0 1

**Sample Output 1**

    Jugador1

**Sample Input 2**

    0 0 0
    1 1 1
    2 2 0

**Sample Output 2**

    Jugador1

**Sample Input 3**

    0 0 0
    1 1 2
    2 1 1

**Sample Output 3**

    Empat

**Sample Input 4**

    0 1 0
    2 1 2
    0 1 2

**Sample Output 4**

    Jugador1

**Sample Input 5**

    1 0 2
    1 2 0
    2 1 0

**Sample Output 5**

    Jugador2

**Sample Input 6**

    1 1 0
    1 1 0
    2 2 2

**Sample Output 6**

    Jugador2

**Sample Input 7**

    0 2 1
    2 1 1
    2 2 1

**Sample Output 7**

    Jugador1

**Sample Input 8**

    0 0 0
    0 0 0
    0 0 0

**Sample Output 8**

    Empat
'''
p.is_public=True
p.date=timezone.now()
p.save()
