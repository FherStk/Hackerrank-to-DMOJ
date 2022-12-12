
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c2-l4-1-les-quatre-e"
p.name="[b3e2c] Les quatre estacions #if"
p.summary="Les quatre estacions"
p.description='''Les quatre estacions tradicionals tenen el seu inici i final marcats per
esdeveniments astronòmics:

  - Hivern: entre el solstici d'hivern i l'equinocci de primavera.

  - Primavera: entre l'equinocci de primavera i el solstici d'estiu.

  - Estiu: entre el solstici d'estiu i l'equinocci de tardor.

  - Tardor: entre l'equinocci de tardor i el solstici d'hivern.

A l'hemisferi sud hivern-estiu i primavera-tardor estan invertits

![image](1556614140-ee3bab1cf9-estacions.png)

**Input Format**

La entrada consta d'un dia i mes de l'any.

**Constraints**

Les dates són vàlides

**Output Format**

S'imprimirà l'estació corresponent a l'hemisferi nord i a l'hemisferi
sud.

**Sample Input 0**

    21 12

**Sample Output 0**

    Hivern
    Estiu

**Sample Input 1**

    21 3

**Sample Output 1**

    Primavera
    Tardor

**Sample Input 2**

    21 6

**Sample Output 2**

    Estiu
    Hivern

**Sample Input 3**

    23 9

**Sample Output 3**

    Tardor
    Primavera

**Sample Input 4**

    20 12

**Sample Output 4**

    Tardor
    Primavera

**Sample Input 5**

    22 12

**Sample Output 5**

    Hivern
    Estiu

**Sample Input 6**

    20 3

**Sample Output 6**

    Hivern
    Estiu

**Sample Input 7**

    22 3

**Sample Output 7**

    Primavera
    Tardor

**Sample Input 8**

    20 6

**Sample Output 8**

    Primavera
    Tardor

**Sample Input 9**

    22 6

**Sample Output 9**

    Estiu
    Hivern

**Sample Input 10**

    22 9

**Sample Output 10**

    Estiu
    Hivern

**Sample Input 11**

    24 9

**Sample Output 11**

    Tardor
    Primavera

**Sample Input 12**

    15 1

**Sample Output 12**

    Hivern
    Estiu

**Sample Input 13**

    23 5

**Sample Output 13**

    Primavera
    Tardor

**Sample Input 14**

    21 7

**Sample Output 14**

    Estiu
    Hivern

**Sample Input 15**

    27 10

**Sample Output 15**

    Tardor
    Primavera

**Sample Input 16**

    30 1

**Sample Output 16**

    Hivern
    Estiu

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
