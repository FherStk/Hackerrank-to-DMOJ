
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c6-l3-2-equation2d"
p.name="[ec0a7] Equation2d"
p.summary="Equation2d"
p.description='''Implementa el mètode de la classe Equation2D amb la solució a l'equació:

²

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    1 -5 6

**Sample Output 0**

    1.00 * 3.00 * 3.00  + -5.00 * 3.00 + 6.00 = 0
    1.00 * 2.00 * 2.00  + -5.00 * 2.00 + 6.00 = 0

**Sample Input 1**

    2 -10 12

**Sample Output 1**

    2.00 * 3.00 * 3.00  + -10.00 * 3.00 + 12.00 = 0
    2.00 * 2.00 * 2.00  + -10.00 * 2.00 + 12.00 = 0

**Sample Input 2**

    1 4 0

**Sample Output 2**

    1.00 * 0.00 * 0.00  + 4.00 * 0.00 + 0.00 = 0
    1.00 * -4.00 * -4.00  + 4.00 * -4.00 + 0.00 = 0

**Sample Input 3**

    1 0 -1

**Sample Output 3**

    1.00 * 1.00 * 1.00  + 0.00 * 1.00 + -1.00 = 0
    1.00 * -1.00 * -1.00  + 0.00 * -1.00 + -1.00 = 0

**Sample Input 4**

    15 -6.5 -2.7

**Sample Output 4**

    15.00 * 0.69 * 0.69  + -6.50 * 0.69 + -2.70 = 0
    15.00 * -0.26 * -0.26  + -6.50 * -0.26 + -2.70 = 0

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
