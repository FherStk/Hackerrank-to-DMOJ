
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="dos-reinas"
p.name="Dos Reinas"
p.summary="Di si dos reinas colocadas en un tablero de ajedrez se atacan mútuamente."
p.description='''Dadas las posiciones de las reinas blanca y negra en un tablero de
ajedrez, el programa debe decir si se atacan mútuamente.

**Input Format**

El tablero de ajedrez consiste en 8 lineas de ocho caracteres cada una.
Cada caracter representa una casilla del tablero. El caracter '-' indica
una casilla vacía. La casilla en la que está la reina BLANCA se indica
con una 'B'. La casilla en la que está la reina NEGRA se indica con una
'N'.

**Constraints**

C = 64

**Output Format**

SI | NO

**Sample Input 0**

    B----N--
    --------
    --------
    --------
    --------
    --------
    --------
    --------

**Sample Output 0**



**Sample Input 1**

    --------
    B-------
    --------
    --------
    --------
    --------
    -----N--
    --------

**Sample Output 1**



**Sample Input 2**

    --------
    --------
    B-------
    --------
    --------
    --------
    --------
    N-------

**Sample Output 2**



**Sample Input 3**

    --------
    ------B-
    --------
    --------
    --------
    --N-----
    --------
    --------

**Sample Output 3**



**Sample Input 4**

    --------
    -------N
    --------
    --------
    --------
    --------
    --------
    -B------

**Sample Output 4**



**Sample Input 5**

    --------
    --------
    --------
    --------
    --------
    -------N
    --------
    -------B

**Sample Output 5**



**Sample Input 6**

    --------
    --------
    -N------
    --------
    --------
    --------
    --------
    ------B-

**Sample Output 6**



**Sample Input 7**

    --------
    --------
    --------
    --------
    --------
    --------
    --------
    --N--B--

**Sample Output 7**



**Sample Input 8**

    -B------
    ------N-
    --------
    --------
    --------
    --------
    --------
    --------

**Sample Output 8**



**Sample Input 9**

    -----B--
    --------
    --------
    --------
    --------
    --------
    --------
    ---N----

**Sample Output 9**



**Sample Input 10**

    --------
    --------
    --------
    --------
    N-------
    --------
    --------
    ------B-

**Sample Output 10**



**Sample Input 11**

    --------
    --------
    --------
    --------
    -------N
    --------
    --------
    B-------

**Sample Output 11**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
