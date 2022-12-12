
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="posicion-de-una-letr"
p.name="[bf99e] Posició d'una lletra en un text #array"
p.summary="Posició d'una lletra en un text"
p.description='''Donat un text i una lletra, troba la posició de la primera ocurrència de
la lletra al text.

**Input Format**

A la primera línia hi ha el text.

A la següent hi ha la lletra.

**Constraints**

\-

**Output Format**

Un enter indicant la posició de la lletra. Si la lletra no hi és al
text, s'imprimirà 

**Sample Input 0**

    hola mon!
    o

**Sample Output 0**



**Sample Input 1**

    hola mon!
    m

**Sample Output 1**



**Sample Input 2**

    hola mon!
    z

**Sample Output 2**



**Sample Input 3**

    hola mons
    s

**Sample Output 3**



**Sample Input 4**

    hola hola
    h

**Sample Output 4**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
