
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l1-9-sobren-ous"
p.name="[dbcc6] Sobren ous #operadors #ternari"
p.summary="Sobren ous"
p.description='''Un granjer ha de portar al mercat els ous que ponen les seves gallines.

Par a transportar-los utilitza oueres en les quals caben 24 ous.

Quan arriba el moment de recollir els ous, el granjer necessita saber
quantes oueres li calen per a poder transportar-los tots.

A més a més, vol que totes les oueres quedin totalment plenes, de forma,
que si a la última ouera li queda espai, espera fins que les gallines
posin els ous que li falten.

**Input Format**

Un número  que indica el nombre d'ous que han posat les gallines.

**Constraints**

\-

**Output Format**

S'imprimiran dos nombres separats per un espai en blanc.

El primer nombre és la quantitat d'oueres que es necessiten.

El segon nombre és la quantitat d'ous que fan falta per omplir l'última
ouera.

**Sample Input 0**



**Sample Output 0**

    2 4

**Explanation 0**

Necessitará 2 oueres, i li faltaran 4 ous

**Sample Input 1**



**Sample Output 1**

    1 4

**Explanation 1**

Necesitará 1 ouera, i li faltaran 4 ous per a emplenar-la

**Sample Input 2**



**Sample Output 2**

    0 0

**Explanation 2**

No necessitará cap ouera, ni cap ou

**Sample Input 3**



**Sample Output 3**

    2 0
'''
p.is_public=True
p.date=timezone.now()
p.save()
