
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="elimina-vocales"
p.name="Elimina vocales"
p.summary="Elimina las vocales de una frase."
p.description='''Dada una frase (terminada con un salto de linea), escribe la misma frase
pero eliminando las vocales.

**Input Format**

Una frase terminada con un salto de linea '\n'

**Constraints**

1 \<= L \<= 100

**Output Format**

La frase sin las vocales.

**Sample Input 0**

    hola mundo!

**Sample Output 0**

    hl mnd!

**Sample Input 1**

    lalalA

**Sample Output 1**

    lll

**Sample Input 2**

    xa, XA, xE, xI, xO, xu

**Sample Output 2**

    x, X, x, x, x, x

**Sample Input 3**

    xAaAxeEe

**Sample Output 3**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
