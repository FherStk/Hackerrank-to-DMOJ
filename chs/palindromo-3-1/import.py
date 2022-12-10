
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="palindromo-3-1"
p.name="[C5-L1-2] Palíndrom #strings"
p.summary="Palíndrom"
p.description='''Donada una frase, digues si és un palíndrom

No s'han de comptar els espais en blanc, ni els caracters de puntuació:

    . , ' ! ? -

Tampoc s'han de tenir en compte les majúscules i minúscules.

**Input Format**

Una línia amb un String.

**Constraints**

\-

**Output Format**

'true' | 'false'

**Sample Input 0**

    hola mon!

**Sample Output 0**

    false

**Sample Input 1**

    luz azul

**Sample Output 1**

    true

**Sample Input 2**

    a ti no, bonita.

**Sample Output 2**

    true

**Sample Input 3**

    amor a roma

**Sample Output 3**

    true

**Sample Input 4**

    Ella te da detalles

**Sample Output 4**

    false

**Sample Input 5**

    anul-la la lluna

**Sample Output 5**

    true

**Sample Input 6**

    Catala, a l'atac

**Sample Output 6**

    true

**Sample Input 7**

    A una nena nua llepa-li la pell, llepa-li la pell a una nena nua.

**Sample Output 7**

    true

**Sample Input 8**

    Apa! Cal a la capa?

**Sample Output 8**

    true
'''
p.is_public=True
p.date=timezone.now()
p.save()
