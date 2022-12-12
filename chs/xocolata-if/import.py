
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="xocolata-if"
p.name="Xocolata  #operadors #ternari"
p.summary="Xocolata  #if"
p.description='''Una barra de xocolata té x quadradets. Esbrina si és possible paritr la
barra per una única línia, de forma que ens quedi un troç amb exactament
 quadradets.

**Input Format**

Tres nombres enters:  - Açada  - Amplada  - Quadradets a obtenir

**Constraints**

\-

**Output Format**

 | 

**Sample Input 0**

    4 2 6

**Sample Output 0**



**Explanation 0**

![image](1601981625-69da57c544-x1.png)

**Sample Input 1**

    5 4 5

**Sample Output 1**



**Explanation 1**

![image](1601981699-fa5aceb80f-x2.png)

**Sample Input 2**

    2 4 3

**Sample Output 2**



**Explanation 2**

![image](1601981744-333e143db0-x3.png)

**Sample Input 3**

    2 6 18 

**Sample Output 3**



**Explanation 3**

No hi ha prou quadradets a la barreta

**Sample Input 4**

    6 7 18

**Sample Output 4**



**Sample Input 5**

    5 6 12

**Sample Output 5**



**Sample Input 6**

    5 6 12

**Sample Output 6**



**Sample Input 7**

    4 6 10

**Sample Output 7**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
