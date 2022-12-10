
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l2-8-notacio-algebraica-als-escacs"
p.name="[d5dbb] Notació algebraica als escacs  #conversio"
p.summary="Notació algebraica als escacs"
p.description='''Les caselles del tauler d'escacs es poden identificar per la seva fila i
columna.

Hi han diverses notacions per a identificar la fila i columna d'una
casella.

La més senzilla és la númèrica, on s'identifica cada fila i columna pel
seu número d'ordre.

Una altra notació és l'algebraica, on la fila d'identifica pel seu
número i la columna per les lletres minúscules a, b, c, d, e, f, g, h.

![image](1556193381-4e2ad9590a-AlgebraicNotationOnChessboard.png)

**Input Format**

La entrada consisteix en dos nombres  i  corresponents a la fila i
columna d'una casella.

**Constraints**

\-

**Output Format**

S'imprimirà la posició de la casella en notació algebraica.

**Sample Input 0**

    1 1

**Sample Output 0**



**Sample Input 1**

    2 3

**Sample Output 1**



**Sample Input 2**

    3 1

**Sample Output 2**



**Sample Input 3**

    4 8

**Sample Output 3**



**Sample Input 4**

    5 7

**Sample Output 4**



**Sample Input 5**

    6 6

**Sample Output 5**



**Sample Input 6**

    7 8

**Sample Output 6**



**Sample Input 7**

    8 1

**Sample Output 7**


'''
p.is_public=True
p.date=timezone.now()
p.save()
