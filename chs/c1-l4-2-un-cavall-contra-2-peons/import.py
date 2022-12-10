
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l4-2-un-cavall-contra-2-peons"
p.name="[d87f8] Un cavall contra dos peons #operadors"
p.summary="Un cavall contra dos peons"
p.description='''Als escacs el cavall pot saltar fent una "L", així:

![image](1556383344-dffbb67ec9-cavallpeons.png)

Donada la posició d'un cavall i de dos peons al tauler, digues quants
peons està amenaçant el cavall.

**Input Format**

La posició del cavall, i del dos peons

**Constraints**

\-

**Output Format**

0 | 1 | 2

**Sample Input 0**

    4 5
    3 3
    5 4

**Sample Output 0**



**Explanation 0**

![image](1556383992-2399b03885-cavallpeons1.png)

**Sample Input 1**

    4 5
    2 4
    6 4

**Sample Output 1**



**Explanation 1**

![image](1556384047-ed8d954478-cavallpeons2.png)

**Sample Input 2**

    6 2
    6 4
    7 1

**Sample Output 2**



**Explanation 2**

![image](1556384115-a21b4284b9-cavallpeons3.png)

**Sample Input 3**

    1 1
    2 3
    3 2

**Sample Output 3**



**Explanation 3**

![image](1556384180-3aa3857b16-cavallpeons4.png)

**Sample Input 4**

    7 6
    3 4
    8 8

**Sample Output 4**



**Explanation 4**

![image](1556384253-e52c2dc2a5-cavallpeons5.png)

**Sample Input 5**

    3 5
    2 2
    1 1

**Sample Output 5**



**Sample Input 6**

    8 2
    7 4
    5 3

**Sample Output 6**


'''
p.is_public=True
p.date=timezone.now()
p.save()
