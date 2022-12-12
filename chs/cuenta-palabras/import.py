
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="cuenta-palabras"
p.name="Cuenta palabras"
p.summary="Cuenta el número de palabras de un texto."
p.description='''Dado un texto, cuenta el número de palabras que contiene.

**Input Format**

Un string con varios saltos de línea. El texto termina con la palabra
END (que no debe procesarse)

**Constraints**

1 \<= L \<= 100

**Output Format**

Un entero indicando el número de palabras

**Sample Input 0**

    hola mundo!
    END

**Sample Output 0**



**Sample Input 1**

    hola, que tal.
    END

**Sample Output 1**



**Sample Input 2**

    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit.
    END

**Sample Output 2**



**Sample Input 3**

    Lorem ipsum
    dolor sit amet,
    consectetur adipiscing
    elit.
    END

**Sample Output 3**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
