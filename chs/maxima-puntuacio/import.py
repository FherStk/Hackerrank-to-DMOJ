
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="maxima-puntuacio"
p.name="Màxima puntuació  #for"
p.summary="Màxima puntuació"
p.description='''En molts jocs guanya qui ha fet més punts al final de la partida.

Esbrina qui és el guanyador a partir de les puntuacions finals de 6
jugadors.

**Input Format**

L'entrada consta de 6 noms amb 6 puntuacions.

**Constraints**

\-

**Output Format**

El nom i la puntuació del guanyador

**Sample Input 0**

    Larry 100
    Ken 101
    Philip 105
    Niklaus 110
    Rasmus 99
    Chris 70

**Sample Output 0**

    Niklaus 110

**Sample Input 1**

    Bjarne 80
    Guido  77
    Dennis 99
    Yukihiro 89
    Alan 90
    James 100

**Sample Output 1**

    James 100

**Sample Input 2**

    Grace 105
    Kathleen 99
    Brendan 96
    Anders 101
    Roberto 87
    Xavier 70

**Sample Output 2**

    Grace 105

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
