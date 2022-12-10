
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c6-l2-2-equation"
p.name="[c789a] Equation"
p.summary="Equation"
p.description='''Implementa el mètode Equation.calculateSolution()

Aquest mètode ha d'emmagatzemar en la variable 'x' la solució a
l'equació:

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    10 5
    5 10
    2.5 5
    0

**Sample Output 0**

    10.00 * -0.50 + 5.00 = 0
    5.00 * -2.00 + 10.00 = 0
    2.50 * -2.00 + 5.00 = 0

**Sample Input 1**

    100 500
    1 5
    2 10
    5 25
    0

**Sample Output 1**

    100.00 * -5.00 + 500.00 = 0
    1.00 * -5.00 + 5.00 = 0
    2.00 * -5.00 + 10.00 = 0
    5.00 * -5.00 + 25.00 = 0
'''
p.is_public=True
p.date=timezone.now()
p.save()
