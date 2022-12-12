
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="distancia-hamming"
p.name="[C5-L1-4] Distància Hamming"
p.summary="Distància Hamming"
p.description='''Donats dos Strings, calcula la seva distància Hamming.

La distància Hamming entre dos Strings de la mateixa longitud és la
quantitat de posicions en les quals els caracters són diferents.

Exemple:

    Hola mon
    Hala man

La distància Hamming entre "Hola mon" i "Hala man" és 2, ja que en les
posicions 1 i 6 els caracters són diferents.

**Input Format**

Dos Strings, cadascun en una línia.

**Constraints**

\-

**Output Format**

La distància Hamming entre els dos Strings, **si són d'igual longitud**.

Si són de distinta longitud s'imprimirá -1.

**Sample Input 0**

    Hola mon
    Hala man

**Sample Output 0**



**Sample Input 1**

    i hate java
    i love java

**Sample Output 1**



**Sample Input 2**

    CAGGTACAGT
    AAGGTACTTA

**Sample Output 2**



**Sample Input 3**

    1011010
    1000010

**Sample Output 3**



**Sample Input 4**

    hola
    hol

**Sample Output 4**



**Sample Input 5**

    CGATTGACGATCAT
    CGATGCTGACTAT

**Sample Output 5**



**Sample Input 6**

    hola
    hola

**Sample Output 6**



**Sample Input 7**

    h
    k

**Sample Output 7**



**Sample Input 8**

    is this a string?
    is this a  string?

**Sample Output 8**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
