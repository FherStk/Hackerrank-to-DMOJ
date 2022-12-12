
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c1-l3-3-piramides-de"
p.name="[c1124] Piràmides de llumins #operadors"
p.summary="Llumins"
p.description='''Al meu oncle li agrada fer figures amb els llumins a les sobretaules,
com aquesta piràmide:

![image](1556271563-38f46282f2-llumins.png)

Per a fer aquesta piràmide de 3 pisos li calen 18 llumins.

¿Quants llumins calen per fer piràmides de diferents alçades?

*<https://www.aceptaelreto.com/problem/statement.php?id=371>*

**Input Format**

La entrada consta d'un número  indicant l'alçada de la piràmide

**Constraints**

\-

**Output Format**

El nombre de llumins necessaris per fer la piràmide.

**Sample Input 0**



**Sample Output 0**



**Explanation 0**

![image](1556271775-3375f463d1-llumins1.png)

**Sample Input 1**



**Sample Output 1**



**Explanation 1**

9 ![image](1556271844-ec87a381e8-llumins2.png)

**Sample Input 2**



**Sample Output 2**



**Explanation 2**

![image](1556271869-b8d476adf8-llumins.png)

**Sample Input 3**



**Sample Output 3**



**Explanation 3**

![image](1556271993-3faea1d6a1-llumins4.png)

**Sample Input 4**



**Sample Output 4**



**Sample Input 5**



**Sample Output 5**



**Sample Input 6**



**Sample Output 6**

    165

**Sample Input 7**



**Sample Output 7**

    3825

**Sample Input 8**

    115

**Sample Output 8**

    20010

**Sample Input 9**

    800

**Sample Output 9**

    961200

**Sample Input 10**

    999

**Sample Output 10**

    1498500

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
