
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="suma-digitos-1"
p.name="Suma dígitos 1"
p.summary="Suma los dígitos de un número"
p.description='''Dado un número entero positivo, realiza la suma de sus dígitos.

**Input Format**

Un número entero positvo N.

**Constraints**

0 \<= N \<= 2147483647

**Output Format**

Un número entero

**Sample Input 0**

    123

**Sample Output 0**



**Sample Input 1**

    11111

**Sample Output 1**



**Sample Input 2**

    100000

**Sample Output 2**



**Sample Input 3**

    2147483647

**Sample Output 3**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
