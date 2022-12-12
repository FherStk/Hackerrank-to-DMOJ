
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="ec7cc-song-class-l0"
p.name="[ec7cc] Song #class #L0"
p.summary="Song"
p.description='''Crea l'objecte  i asigna-li els camps amb les dades de l'entrada.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    One love
    Bob Marley
    4.5
    true

**Sample Output 0**

    <3 Bob Marley - One love
    ****

**Sample Input 1**

    Hey Joe
    Jimmi Hendrix
    4.8
    true

**Sample Output 1**

    <3 Jimmi Hendrix - Hey Joe
    ****

**Sample Input 2**

    Whole Lotta Love
    Led Zeppelin
    4.6
    false

**Sample Output 2**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
