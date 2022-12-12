
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l2-2-prova-mecano"
p.name="[e9ac5] Prova mecanogràfica  #conversio"
p.summary="Prova mecanogràfica"
p.description='''En les proves de mecanografia es demana teclejar un text i es medeix la
precisió i la velocitat:

  - La PRECISIÓ es mideix en **Percentatge** entre el nombre de
    caracters del text i el nombre d'errors comesos.

  - La VELOCITAT es medeix en **Paraules Per Minut** (es considera que
    **una paraula són 5 caracters -sense importar si són lletres, signes
    o espais-**).

Donades les dades d'una prova, determina la precisió i la velocitat.

Les dades d'una prova consisteixen en el nombre de caracters del text,
el nombre d'errores comesos i el temps trigat **(en segons)**.

**Input Format**

La entrada consta de tres nombres:

: nombre de caracters del text

: nombre d'errors comesos

: temps trigat (en segons)

**Constraints**

\-

**Output Format**

S'ha d'imprimir la Precisió (percentatge d'encerts) i la Velocitat
(paraules per minut), cadscun en una línia, i sense decimals.

**Sample Input 0**

    100 10 60

**Sample Output 0**

    90
    20

**Explanation 0**

Si en un text de **100** caracters s'han comés **10** errors i s'ha
trigat **60** segons, el resultat de la prova és:

Precisió: **90**%

Velocitat: **20** PPM

**Sample Input 1**

    10 3 60

**Sample Output 1**

    70
    2

**Explanation 1**

Si en un text de **10** caracters s'han comés **3** errors i s'ha trigat
**60** segons, el resultat de la prova és:

Precisió: **70**%

Velocitat: **2** PPM

**Sample Input 2**

    60 0 10

**Sample Output 2**

    100
    72

**Explanation 2**

Si en un text de **60** caracters s'han comeés **0** errors i s'ha
trigat **10** segons, el resultat de la prova és:

Precisió: **100**%

Velocitat: **72** PPM

**Sample Input 3**

    300 37 65

**Sample Output 3**

    87
    55

**Sample Input 4**

    789 7 165

**Sample Output 4**

    99
    57

**Sample Input 5**

    60 60 6

**Sample Output 5**

    0
    120

**Sample Input 6**

    1 1 1

**Sample Output 6**

    0
    12

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
