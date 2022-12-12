
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="cada-paraula-a-una-l"
p.name="Cada paraula a una línia  #scanner"
p.summary="Cada paraula a una línia"
p.description='''Escriu un programa que llegeixi cinc paraules de l'entrada estàndard i
imprimeixi cada paraula en una nova línia. Les paraules han d'estar en
el mateix ordre.

**Input Format**

Cinc paraules, separades per espais en blanc o salts de línia.

**Constraints**

\-

**Output Format**

Cada paraula en una nova línia

**Sample Input 0**

    Java te
    8 tipus primitius

**Sample Output 0**

    Java
    te
    8
    tipus
    primitius

**Sample Input 1**

    Java te 5
    operadors
    aritmetics

**Sample Output 1**

    Java
    te
    5
    operadors
    aritmetics

**Sample Input 2**

    gat gos
    vaca
    porc gall

**Sample Output 2**

    gat
    gos
    vaca
    porc
    gall

**Sample Input 3**

    a b c d e

**Sample Output 3**

    a
    b
    c
    d
    e

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
