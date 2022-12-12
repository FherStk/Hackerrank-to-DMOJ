
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="cuenta-vocales"
p.name="Cuenta vocales"
p.summary="Cuenta el número de veces que aparece cada vocal."
p.description='''Dada una frase (terminada con un salto de línea), cuenta el número de
veces que aparece cada vocal.

**Input Format**

Un texto terminado con un salto de línea.

**Constraints**

1 \<= L \<= 100

**Output Format**

En la primera linea la cantidad de 'a', en la siguiente linea la
cantidad de 'e', etc.

**Sample Input 0**

    hola mundo

**Sample Output 0**

    1
    0
    0
    2
    1

**Sample Input 1**

    aa ee ii oo uu

**Sample Output 1**

    2
    2
    2
    2
    2

**Sample Input 2**

    xxa xax axx

**Sample Output 2**

    3
    0
    0
    0
    0

**Sample Input 3**

    aa, EE, ii.

**Sample Output 3**

    2
    2
    2
    0
    0

**Sample Input 4**

    aA eE iI oO u

**Sample Output 4**

    2
    2
    2
    2
    1

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
