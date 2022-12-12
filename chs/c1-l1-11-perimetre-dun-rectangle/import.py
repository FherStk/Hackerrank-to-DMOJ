
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c1-l1-11-perimetre-d"
p.name="[f22f4] Perímetre d'un rectangle  #operadors #aritmetics"
p.summary="Perímetre d'un rectangle"
p.description='''El perímetre d'un rectangle és la suma de la longitud de tots els seus
costats.

Un rectangle es pot definir proporcionant les coordenades del seu cantó
superior dret, i les del seu cantó inferior esquerra:

![image](1555870845-59da793e47-rect.png)

**Input Format**

La entrada consta de **dues** coordenades, primer el cantó superior dret
i segon el cantó inferior esquerra.

Per a cada coordenada el primer nombre  es la posició en l'eix
horitzontal, y el segon nombre  és la posició en l'eix vertical.

**Constraints**

\-

**Output Format**

Un nombre enter indicant el perímetre del rectangle

**Sample Input 0**

    3 2
    0 0

**Sample Output 0**



**Sample Input 1**

    1 1
    1 1

**Sample Output 1**



**Sample Input 2**

    2 2
    1 1

**Sample Output 2**



**Sample Input 3**

    1 1
    -1 -1

**Sample Output 3**



**Sample Input 4**

    4 7
    -2 -5

**Sample Output 4**



**Sample Input 5**

    7 6
    2 4

**Sample Output 5**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
