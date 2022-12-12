
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l4-3-cercles-rgb"
p.name="[b83b5] Cercles RGB #operadors"
p.summary="Cercles RGB"
p.description='''RGB és un model de color additiu en el qual la llum vermella, verda i
blava son mesclades per a reproduir colors. És el model que s'usa en
pantalles, projectors, càmeres o scànners.

![image](1556403302-c0b3653a9f-2000px-AdditiveColor.svg.png)

Fem un experiment emetent sobre una pared tres focus rodons -de
diferents tamanys i posicions- de llum vermella, verda i blava.

¿Quants colors distints veurem?

**Input Format**

La entrada consisteix en la definició dels 3 cercles RGB.

Cada cercle es defineix per les coordinades del seu centre (, ) i la
longitud del seu radi .

**Constraints**

\-

**Output Format**

El nombre de colors distints que es veuran.

**Sample Input 0**

    0 0 1
    1 0 1
    2 0 1

**Sample Output 0**



**Explanation 0**

![image](1556400403-81415111d2-rgb1.png)

**Sample Input 1**

    0 0 1
    1 0 1
    3 0 1

**Sample Output 1**



**Explanation 1**

![image](1556400504-46e405efd0-rgb2.png)

**Sample Input 2**

    0 0 1
    2 0 1
    4 0 1

**Sample Output 2**



**Explanation 2**

![image](1556400588-a2612a86b5-rgb3.png)

**Sample Input 3**

    1 0 4
    2 0 2
    0 0 2

**Sample Output 3**



**Explanation 3**

![image](1556404149-55cfc50a49-rgb15.png)

**Sample Input 4**

    1 0 2
    3 0 1
    0 0 1

**Sample Output 4**



**Explanation 4**

![image](1556403831-bebcfe2bd5-rgb14.png)

**Sample Input 5**

    0 1 1
    1 0 1
    1 1 1

**Sample Output 5**



**Explanation 5**

![image](1556401318-b3855eeed6-rgb6.png)

**Sample Input 6**

    0 0 4
    4 0 3
    4 0 2

**Sample Output 6**



**Explanation 6**

![image](1556401893-8941b321ae-rgb7.png)

**Sample Input 7**

    0 0 4
    0 0 3
    0 0 2

**Sample Output 7**



**Explanation 7**

![image](1556402096-b4b1e6bb46-rgb8.png)

**Sample Input 8**

    0 0 4
    2 0 3
    2 0 1

**Sample Output 8**



**Explanation 8**

![image](1556402239-2427c6bf94-rgb9.png)

**Sample Input 9**

    0 0 4
    2 0 3
    4 0 2

**Sample Output 9**



**Explanation 9**

![image](1556402734-86c80870cd-rgb10.png)

**Sample Input 10**

    0 0 4
    6 0 4
    3 0 2

**Sample Output 10**



**Explanation 10**

![image](1556402922-18764a315f-rgb11.png)

**Sample Input 11**

    0 4 4
    6 2 3
    5 6 2

**Sample Output 11**



**Explanation 11**

![image](1556403237-f8b8f5eac0-rgb12.png)

**Sample Input 12**

    2 0 4
    4 0 2
    0 0 2

**Sample Output 12**



**Explanation 12**

![image](1556403552-f7e09bb5b1-rgb13.png)

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
