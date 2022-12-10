
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c7-l2-2-reverse-string"
p.name="[C7-L2-2] Reverse String #recursivitat"
p.summary="Reverse String"
p.description='''Donat un String, invirteix-lo.

**Input Format**

Una línia de text

**Constraints**

No hi ha.

**Output Format**

El text amb l'ordre dels caracters invertit.

**Sample Input 0**

    abcde

**Sample Output 0**

    edcba

**Sample Input 1**

    ab c d efgh

**Sample Output 1**

    hgfe d c ba

**Sample Input 2**

    cgctagcttagctaacg

**Sample Output 2**

    gcaatcgattcgatcgc
'''
p.is_public=True
p.date=timezone.now()
p.save()
