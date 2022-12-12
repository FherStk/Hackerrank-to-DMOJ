
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="los-primos-del-puebl"
p.name="Los primos del pueblo"
p.summary="Decir si la cantidad de números primos en cada secuencia."
p.description='''Dadas varias secuencias de números, decir la cantidad de números primos
que hay en cada una de ellas.

**Input Format**

El primer número T indica la cantidad de casos de prueba que vienen a
continuación. Cada caso de prueba es una secuencia de N números que
termina con un 0.

**Constraints**

1 \<= T \<= 10 1 \<= N \<= 10

**Output Format**

Un numero entero por cada secuencia de numeros; separados por un salto
de línea.

**Sample Input 0**

    1
    1 2 3 5 7 11 13 17 19 23 0

**Sample Output 0**



**Sample Input 1**

    2
    4 6 2 10 5 0
    14 9 15 21 0

**Sample Output 1**

    2
    0

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
