
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="cargol"
p.name="Cargol  #operadors"
p.summary="Cargol"
p.description='''Un cargol vol trepar un pal d'una alçada d' metres. Si puja  metres
durant el dia, però rellisca  metres avall per la nit, en quin dia
aconseguirà arribar a dalt de tot?

**Input Format**

Tres números enters positius: ,  i 

**Constraints**

\> 

\> 

**Output Format**

\-

**Sample Input 0**

    6 3 2

**Sample Output 0**



**Explanation 0**

![image](1601420565-ca68dfa438-cargol.png)

**Sample Input 1**

    5 3 1

**Sample Output 1**



**Explanation 1**

![image](1601420706-04227ef7c8-cargol2.png)

**Sample Input 2**

    7 4 3

**Sample Output 2**



**Explanation 2**

![image](1601421627-65fb1ccd48-cargol3.png)

**Sample Input 3**

    6 4 2

**Sample Output 3**



**Sample Input 4**

    9 4 2

**Sample Output 4**



**Sample Input 5**

    13 5 3

**Sample Output 5**



**Sample Input 6**



**Sample Output 6**


'''
p.is_public=True
p.date=timezone.now()
p.save()
