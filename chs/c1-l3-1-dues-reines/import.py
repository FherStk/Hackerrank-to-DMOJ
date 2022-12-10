
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l3-1-dues-reines"
p.name="[fd50d] Dues reines #operadors"
p.summary="Dues reines"
p.description='''Donades les posicions de les dues reines en un tauler d'escacs, digues
si s'amenacen mútuament.

![image](1556194741-5344980f93-escacs.png)

**Input Format**

La entrada consisteix en 4 nombres indicant la  i  de cada reina

**Constraints**

\-

**Output Format**

true | false

**Sample Input 0**

    4 4
    4 6

**Sample Output 0**

    true

**Explanation 0**

![image](1556195269-a879d1b83b-escacs1.png)

**Sample Input 1**

    3 5
    7 5

**Sample Output 1**

    true

**Explanation 1**

![image](1556195317-517dd415bf-escacs2.png)

**Sample Input 2**

    2 2
    5 3

**Sample Output 2**

    false

**Explanation 2**

![image](1556195389-a4f6ccb1d2-escacs3.png)

**Sample Input 3**

    3 3
    5 5

**Sample Output 3**

    true

**Explanation 3**

![image](1556195455-4980310fd6-escacs4.png)

**Sample Input 4**

    5 5
    3 3

**Sample Output 4**

    true

**Explanation 4**

![image](1556195473-d80d7cef34-escacs4.png)

**Sample Input 5**

    2 6
    5 3

**Sample Output 5**

    true

**Explanation 5**

![image](1556195579-9c56778dbc-escacs5.png)

**Sample Input 6**

    5 3
    2 6

**Sample Output 6**

    true

**Explanation 6**

![image](1556195596-87a216037f-escacs5.png)

**Sample Input 7**

    1 2
    7 8

**Sample Output 7**

    true

**Explanation 7**

![image](1556195658-999fe108b5-escacs6.png)

**Sample Input 8**

    7 8
    1 2

**Sample Output 8**

    true

**Explanation 8**

![image](1556195680-d675747010-escacs6.png)

**Sample Input 9**

    4 8
    7 3

**Sample Output 9**

    false

**Explanation 9**

![image](1556195818-3c6bd9959a-escacs8.png)
'''
p.is_public=True
p.date=timezone.now()
p.save()
