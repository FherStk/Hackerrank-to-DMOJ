
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="unicode-points"
p.name="Unicode points  #conversio"
p.summary="Unicode points"
p.description='''Unicode és una codificació de caracters textuals que pot respresentar
caracters de molts idiomes. Cada caracter es representat per un *Unicode
code point*. Un *code point* és un número enter que identifíca de forma
única un caracter.

Donats 6 code points, imprimeix el text codificat.

**Input Format**

6 números enters

**Constraints**

\-

**Output Format**

text

**Sample Input 0**

    97 98 99 100 101 102

**Sample Output 0**

    abcdef

**Sample Input 1**

    119 97 32 121 101 97

**Sample Output 1**

    wa yea

**Sample Input 2**

    65 90 97 122 48 57

**Sample Output 2**

    AZaz09

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
