
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="cuenta-numeros"
p.name="Cuenta números"
p.summary="Decir la cantidad de números leídos antes de leer un 0."
p.description='''Se deben ir leyendo números hasta que se lea un 0. El programa debe
mostrar la cantidad de números leídos antes del 0.

**Input Format**

Una secuencia de N números.

**Constraints**

0 \<= 1 \<= 10^7

**Output Format**

Un entero indicando la cantidad de números leídos

**Sample Input 0**



**Sample Output 0**



**Sample Input 1**

    5 4 2 5 7 0

**Sample Output 1**



**Sample Input 2**

    3 5 6 3 0

**Sample Output 2**



**Sample Input 3**

    8 6 -1 7 0

**Sample Output 3**



**Sample Input 4**

    7 4 6 9 0

**Sample Output 4**



**Sample Input 5**

    5 8 0

**Sample Output 5**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
