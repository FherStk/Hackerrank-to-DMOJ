
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="tetris-eliminar-lini"
p.name="Tetris, eliminar línies #arrays"
p.summary="Tetris, eliminar línies"
p.description='''![image](1612523216-fc62f6bda7-1611068668-a4adf963d1-21a.png)

Al Tetris, quan una línia horitzontal es completa, aquesta línia
desapareix i totes les peces que estan a sobre descendeixen una posició.

Donat un tauler de Tetris, imprimeix el tauler resultant d'eliminar les
línies completades.

**Input Format**

Primer s'indica el número de  i  del tauler.

A continuació venen una sèrie de  i  que indiquen l'estat de cada
casella.  significa ocupada i  significa lliure.

Per exemple, aquest tauler de Tetris es podria representar així:

![image](1612521867-25f9159e3c-tetris.png)

**Constraints**

\-

**Output Format**

S'imprimirà el tauler resultant amb el mateix format que a l'entrada.

**Sample Input 0**

    3 4
    1 1 0 1
    1 0 0 1
    1 1 1 1

**Sample Output 0**

    1 1 0 1
    1 0 0 1

**Sample Input 1**

    5 4
    1 0 0 1
    1 1 1 1
    1 0 1 1
    1 1 0 0
    0 1 1 1

**Sample Output 1**

    1 0 0 1
    1 0 1 1
    1 1 0 0
    0 1 1 1

**Sample Input 2**

    6 4
    1 0 0 0
    1 1 0 0
    1 1 1 1
    1 1 1 1
    0 1 1 1
    1 1 1 1

**Sample Output 2**

    1 0 0 0
    1 1 0 0
    0 1 1 1

**Sample Input 3**

    8 5
    0 0 0 0 0
    0 0 0 0 0
    1 0 0 0 1
    1 1 0 0 1
    1 1 1 1 1
    1 1 1 1 1
    0 1 1 1 1
    1 1 1 1 0

**Sample Output 3**

    0 0 0 0 0
    0 0 0 0 0
    1 0 0 0 1
    1 1 0 0 1
    0 1 1 1 1
    1 1 1 1 0

**Sample Input 4**

    3 4
    1 1 1 1
    1 1 1 1
    1 1 1 1

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
