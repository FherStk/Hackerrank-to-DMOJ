
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="esquirols-i-nous"
p.name="Esquirols i nous  #operadors #aritmetics"
p.summary="Esquirols i nous"
p.description='''esquirols han trobat  nous i han decidit repartir-se-les equitativament.
Esbrina quantes nous quedaran després de que cada esquirol prengui la
seva quantitat de nous.

**Input Format**

Dos enters positius  i . Separats per un *whitespace* o un *newline*.

\<= 10000  \<= 10000

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    2 10

**Sample Output 0**



**Explanation 0**

Cada esquirol pren 5 nous, i no en sobra cap.

**Sample Input 1**

    3 14

**Sample Output 1**



**Explanation 1**

Els 3 esquirols prenen cadascú 4 nous, i en sobren 2.

**Sample Input 2**

    7 48

**Sample Output 2**



**Explanation 2**

Cadascún dels 7 esquirols pren 6 nous, en sobren 6.

**Sample Input 3**

    4564 98743

**Sample Output 3**

    2899

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
