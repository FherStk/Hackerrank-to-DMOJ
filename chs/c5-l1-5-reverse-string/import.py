
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c5-l1-5-reverse-stri"
p.name="[C5-L1-5] Reverse String"
p.summary="Reverse String"
p.description='''Donat un string, inverteix-lo

**Input Format**

String

**Constraints**

\-

**Output Format**

L'string amb els caracters en ordre invers.

**Sample Input 0**

    hola

**Sample Output 0**

    aloh

**Sample Input 1**

    hola mon!

**Sample Output 1**

    !nom aloh

**Sample Input 2**

    java

**Sample Output 2**

    avaj

**Sample Input 3**

    toCharArray()

**Sample Output 3**

    )(yarrArahCot

**Sample Input 4**

    i love programming very much

**Sample Output 4**

    hcum yrev gnimmargorp evol i

**Sample Input 5**

    pipiripip

**Sample Output 5**

    pipiripip

**Sample Input 6**

    .si ti ,sey ?gnirts desrever gnol yrev a siht si

**Sample Output 6**

    is this a very long reversed string? yes, it is.

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
