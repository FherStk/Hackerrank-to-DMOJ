
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="suma-de-pares-y-producto-de-impares"
p.name="[b28ef] Suma de parells i producte d'imparells"
p.summary="Suma de parells i producte d'imparells"
p.description='''Escriu un programa que llegeixi una seqüència de números enters
positius, i escrigui la suma dels números parells, el producte dels
números imparells i la quantitat de números.

**Input Format**

Una seqüència de números enters positius acabada en -1.

**Constraints**

\-

**Output Format**

Imprimeix la suma dels números parells en una línia, en la següent línia
el producte dels números imparells i en la següent línea el total de
números llegits (sense comptar el -1).

**Sample Input 0**

    2 3 4 6 7 8 -1

**Sample Output 0**

    20
    21
    6

**Sample Input 1**

    9 8 7 6 -1

**Sample Output 1**

    14
    63
    4

**Sample Input 2**

    7 4 8 1 2 3 7 3 -1

**Sample Output 2**

    14
    441
    8
'''
p.is_public=True
p.date=timezone.now()
p.save()
