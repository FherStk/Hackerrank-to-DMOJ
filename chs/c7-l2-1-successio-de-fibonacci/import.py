
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c7-l2-1-successio-de"
p.name="[C7-L2-1] Successió de Fibonacci #recursivitat"
p.summary="Successió de Fibonacci"
p.description='''Escriu un algoritme recursiu que trobi el nombre en la posició N de la
Successió de Fibonacci.

**Input Format**

Un nombre N

**Constraints**

No hi ha

**Output Format**

El número de la successió de Fibonacci que ocupa la posició N

**Sample Input 0**



**Sample Output 0**



**Sample Input 1**



**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Sample Input 3**



**Sample Output 3**



**Sample Input 4**



**Sample Output 4**



**Sample Input 5**



**Sample Output 5**



**Sample Input 6**



**Sample Output 6**



**Sample Input 7**



**Sample Output 7**



**Sample Input 8**



**Sample Output 8**



**Sample Input 9**



**Sample Output 9**

    610

**Sample Input 10**



**Sample Output 10**

    75025

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
