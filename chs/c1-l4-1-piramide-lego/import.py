
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c1-l4-1-piramide-leg"
p.name="[e1070] Piràmide lego #operadors"
p.summary="Piràmide lego"
p.description='''Amb peces de lego de 4x4 pots construir piràmides com aquesta de 3
pisos:

![image](1556381326-670e308ced-lego2.png)

Per a construir-la hem utilitzat 14 peces:

![image](1556381474-cb0adb7ecc-lego1.png)

¿Quantes peces es necessiten per a construir un piràmide d'un determinat
nombre de pisos?

**Input Format**

La entrada consta d'un nombre de pisos 

**Constraints**

\-

**Output Format**

El nombre de peces necessàries

**Sample Input 0**



**Sample Output 0**



**Explanation 0**

![image](1556382453-eca1a030c5-lego3.png)

**Sample Input 1**



**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Explanation 2**

![image](1556382656-90785cc9b1-lego4.png)

**Sample Input 3**



**Sample Output 3**



**Sample Input 4**



**Sample Output 4**



**Sample Input 5**



**Sample Output 5**

    385

**Sample Input 6**

    1000

**Sample Output 6**

    333833500

**Sample Input 7**

    765892

**Sample Output 7**

    149755297914942910

**Sample Input 8**

    1000000

**Sample Output 8**

    333333833333500000

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
