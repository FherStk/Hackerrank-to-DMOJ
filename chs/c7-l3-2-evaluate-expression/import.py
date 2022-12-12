
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c7-l3-2-evaluate-exp"
p.name="[C7-L3-2] Evaluate expression #recursivitat"
p.summary="Evaluate expression #recursivitat"
p.description='''Donat un String amb una expressió aritmètica de sumes i multiplicacions,
avaluar el seu resultat.

**Input Format**

Un string amb una expressió aritmètica de sumes i multiplicacions
enteres.

**Constraints**

No hi ha

**Output Format**

El resultat de l'expressió

**Sample Input 0**

    2+2

**Sample Output 0**



**Sample Input 1**

    2+2+2

**Sample Output 1**



**Sample Input 2**

    2*2

**Sample Output 2**



**Sample Input 3**

    2*2*2

**Sample Output 3**



**Sample Input 4**

    2+3*4

**Sample Output 4**



**Sample Input 5**

    2*3+4

**Sample Output 5**



**Sample Input 6**

    2*3+4*5

**Sample Output 6**



**Sample Input 7**

    2+3*4+5

**Sample Output 7**



**Sample Input 8**

    2+10*1+1*100

**Sample Output 8**

    112

**Sample Input 9**

    123*456+789*123+456*789

**Sample Output 9**

    512919

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
