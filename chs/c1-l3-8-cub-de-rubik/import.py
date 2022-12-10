
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l3-8-cub-de-rubik"
p.name="[b1ac9] Cub de Rubik #operadors"
p.summary="Cub de Rubik"
p.description='''El cub de Rubik stàndard (de tamany 3) consisteix en 26 "cubies" o
"cubelets" (a la part interior no hi ha cap cubelet).

![image](1556380034-03bcac4051-rubik.png)

Hi ha moltes altres variants del cub, amb tamanys i formes diferents.

**Input Format**

La entrada consisteix en un nombre  indicant el tamany del cub.

**Constraints**

\-

**Output Format**

S'imprimira el nombre de "cubelets" que té el cub.

**Sample Input 0**



**Sample Output 0**



**Sample Input 1**



**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Sample Input 3**



**Sample Output 3**

    152

**Sample Input 4**



**Sample Output 4**

    488

**Sample Input 5**

    1000

**Sample Output 5**

    5988008

**Sample Input 6**

    1000000

**Sample Output 6**

    5999988000008
'''
p.is_public=True
p.date=timezone.now()
p.save()
