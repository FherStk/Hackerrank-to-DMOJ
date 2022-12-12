
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="compresio-rle"
p.name="[C3-L2-6] Compressió RLE #for"
p.summary="Compressió RLE"
p.description='''La codificació Run-length encoding (RLE) és una forma molt simple de
compressió de dades en què seqüències de dades amb el mateix valor
consecutiu són emmagatzemades com un únic valor més el seu recompte.

Per exemple, la cadena següent cadena de text:

    BBBBNNNBBBBBNN

Es pot comprimir d'aquesta manera:

    4B3N5B2N

S'interpreta com 4 bes, 3 enes, 5 bes, 2 enes.

**Input Format**

Una cadena de L caràcters

**Constraints**

\-

**Output Format**

La cadena comprimida

**Sample Input 0**

    BBBNNNN

**Sample Output 0**

    3B4N

**Sample Input 1**

    BBBBBNNNB

**Sample Output 1**

    5B3N1B

**Sample Input 2**

    BNNNNNB

**Sample Output 2**

    1B5N1B

**Sample Input 3**

    ABBBAAAANNNCCADDDDD

**Sample Output 3**

    1A3B4A3N2C1A5D

**Sample Input 4**

    WWWWWWWWHHHHHHHAAAAAAATTTTTTTTTTTTTT

**Sample Output 4**

    8W7H7A14T

**Sample Input 5**

    JAVA

**Sample Output 5**

    1J1A1V1A

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
