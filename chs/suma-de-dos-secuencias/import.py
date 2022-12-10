
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="suma-de-dos-secuencias"
p.name="Suma de dos secuencias"
p.summary="Sumar cada número de una secuencia con su correspondiente de otra secuencia."
p.description='''Dadas dos secuencias de números, sumar cada número de la primera con su
correspondiente de la segunda.

**Input Format**

La entrada consta de dos secuencias de números. Para cada secuencia
primero se indica la cantidad N de números que hay en la secuencia. A
continuación viene la secuencia.

**Constraints**

1 \<= N \<= 100

**Output Format**

La secuencia de números resultante, separados por espacios en blanco

**Sample Input 0**

    3    1 2 3
    3    4 5 6

**Sample Output 0**

    5 7 9

**Sample Input 1**

    4    100 200 300 400
    4    10 20 30 40

**Sample Output 1**

    110 220 330 440

**Sample Input 2**

    5    2 1 4 3 2
    5    3 4 2 3 4

**Sample Output 2**

    5 5 6 6 6

**Sample Input 3**

    1    10
    1    10

**Sample Output 3**


'''
p.is_public=True
p.date=timezone.now()
p.save()
