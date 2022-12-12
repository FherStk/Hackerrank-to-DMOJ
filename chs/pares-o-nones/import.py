
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="pares-o-nones"
p.name="Pares o nones  #ternari"
p.summary="Pares o nones"
p.description='''Dos amics juguen al pares o nones. Ú diu *pares*, i l'altre *nones*, i
després trauen els dits. Digues qui guanya\!

**Input Format**

l'entrada consta de 4 dades: - una paraula amb que diu el primer jugador
- un número amb els dits que trau el primer jugador - una paraula amb el
que diu el segon jugador - un número amb els dits que trau el segon
jugador

**Constraints**

\-

**Output Format**

S'imprimirà el jugador que guanya:  | 

**Sample Input 0**

    pares 4
    nones 1

**Sample Output 0**

    segon jugador

**Sample Input 1**

    nones 4
    pares 1

**Sample Output 1**

    primer jugador

**Sample Input 2**

    pares 3
    nones 3

**Sample Output 2**

    primer jugador

**Sample Input 3**

    nones 3
    pares 3

**Sample Output 3**

    segon jugador

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
