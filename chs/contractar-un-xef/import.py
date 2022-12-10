
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="contractar-un-xef"
p.name="Contractar un xef  #scanner"
p.summary="Contractar un xef"
p.description='''Imagina que ets el cap de personal d'un restaurant i has de contractar
un xef. Per fer-ho has de recollir algunes dades preliminars dels
candidats.

Tens un formulari per a recollir les següents dades dels candidats: nom,
edat, nivell d'estudis, anys d'experiència, i tipus de cuina.

El teu programa ha de llegir totes les paraules (o números) de les cinc
línies de l'entrada i imprimir: "El formulari de  s'ha completat.
Et contactarem si necessitem un xef de cuina ."

**Input Format**

L'entrada consta de 5 línies:

  - A la primera línia hi ha el nom (String)
  - A la segona línia hi ha l'edat (int)
  - A la tercera línia hi ha el nivell d'estudis (String)
  - A la quarta línia hi ha els anys (int)
  - A la cinquena línia hi ha el tipus de cuina (String)

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    Joan
    33
    secundaria
    4
    tradicional

**Sample Output 0**

    El formulari de Joan s'ha completat. Et contactarem si necessitem un xef de cuina tradicional.

**Sample Input 1**

    Miquel
    24
    universitari
    2
    fussio

**Sample Output 1**

    El formulari de Miquel s'ha completat. Et contactarem si necessitem un xef de cuina fussio.

**Sample Input 2**

    Maria Elena
    34
    universitari
    10
    vanguardista

**Sample Output 2**

    El formulari de Maria Elena s'ha completat. Et contactarem si necessitem un xef de cuina vanguardista.

**Sample Input 3**

    Josep Antoni
    20
    sense estudis
    3
    nouvelle cuisine

**Sample Output 3**

    El formulari de Josep Antoni s'ha completat. Et contactarem si necessitem un xef de cuina nouvelle cuisine.
'''
p.is_public=True
p.date=timezone.now()
p.save()
