
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="tres-en-raya"
p.name="OXO"
p.summary="Tres en ratlla"
p.description='''Donat un tauler de tres en ratlla, determina el guanyador, o si hi ha
empat.

**Input Format**

El tauler consisteix en 3 línies amb 3 caracters cada línia. Les
caselles del tauler buides es marquen amb un '-' Les caselles ocupades
per fitxes es marquen amb 'O' i 'X'.

**Constraints**

El tauler és vàlid

**Output Format**

El guanyador es mostrarà amb la seva marca, i s'usa '-' per a l'empat.

{ X | O | - }

**Sample Input 0**

    O--
    -O-
    XXX

**Sample Output 0**



**Sample Input 1**

    --X
    OOO
    -X-

**Sample Output 1**



**Sample Input 2**

    XXX
    00X
    X00

**Sample Output 2**



**Sample Input 3**

    O-X
    -XO
    XO-

**Sample Output 3**



**Sample Input 4**

    OXX
    XOX
    XOO

**Sample Output 4**



**Sample Input 5**

    XO-
    XO-
    X--

**Sample Output 5**



**Sample Input 6**

    XO-
    XO-
    -O-

**Sample Output 6**



**Sample Input 7**

    XXO
    XXO
    O-O

**Sample Output 7**



**Sample Input 8**

    OXO
    OXO
    XOX

**Sample Output 8**



**Sample Input 9**

    XXO
    OXX
    XOO

**Sample Output 9**



**Sample Input 10**

    OXO
    XOX
    XOX

**Sample Output 10**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
