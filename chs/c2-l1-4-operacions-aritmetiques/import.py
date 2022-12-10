
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c2-l1-4-operacions-aritmetiques"
p.name="[C2-L1-4] Expressions aritmètiques #if"
p.summary="Expressions aritmètiques"
p.description='''Implementa un intèrpret d'expressions aritmètiques.

Els operadors que ha d'implementar són:

    +    Addició
    -    Subtracció
    *    Multiplicació
    /    Divisió
    %    Residu

**Input Format**

La entrada consisteix en el primer operand , l'operador , i el segon
operand , separats per espais en blanc.

**Constraints**

\-100 \<=  \<= 100

\-100 \<=  \<= 100

i  són nombres decimals.

**Output Format**

El resultat de la operació (float), o els missatges  i  en el seu cas.

**Sample Input 0**

    1 + 1

**Sample Output 0**

    2.0

**Sample Input 1**

    1 - 1

**Sample Output 1**

    0.0

**Sample Input 2**

    100 * 100

**Sample Output 2**

    10000.0

**Sample Input 3**

    5 / 10

**Sample Output 3**

    0.5

**Sample Input 4**

    10 % 0.5

**Sample Output 4**

    0.0

**Sample Input 5**

    10 / 0

**Sample Output 5**

    Error: division by zero

**Sample Input 6**

    7 & 3

**Sample Output 6**

    Error: operation not permitted

**Sample Input 7**

    27 % 0

**Sample Output 7**

    Error: division by zero
'''
p.is_public=True
p.date=timezone.now()
p.save()
