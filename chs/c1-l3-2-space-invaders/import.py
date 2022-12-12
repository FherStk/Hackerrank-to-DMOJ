
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c1-l3-2-space-invade"
p.name="[e30d0] Space Invaders #operadors"
p.summary="Space Invaders"
p.description='''Es vol implementar un sistema de detecció de col·lisions per al joc
Space Invaders. Una de les col·lisions que s'haurà de detectar és quan
un dispar dona en un alien.

El sistema de col·lisions haurà de determinar si el rectangle que
envolta l'alien i el rectangle que envolta el dispar estan solapats

![image](1556267080-5852f74644-invaders.png)

**Input Format**

La entrada consisteix en la definició dels dos rectangles. Per a cada
rectangle es determinen les coordenades (,) del seu canto
inferior-esquerra, la seva amplada () i la seva alçada ().

**Constraints**

\-

**Output Format**

true | false

**Sample Input 0**

    2 3 4 2
    0 0 1 2

**Sample Output 0**

    false

**Explanation 0**

![image](1556268123-3520e7d647-invaders1.png)

**Sample Input 1**

    1 4 4 2
    2 1 1 2

**Sample Output 1**

    false

**Explanation 1**

![image](1556268246-9de6b7378f-invaders2.png)

**Sample Input 2**

    1 2 4 2
    2 1 1 2

**Sample Output 2**

    true

**Explanation 2**

![image](1556268298-3f6f7eaf9d-invaders3.png)

**Sample Input 3**

    1 0 4 2
    4 -1 1 2

**Sample Output 3**

    true

**Explanation 3**

![image](1556268414-decb7c5c18-invaders4.png)

**Sample Input 4**

    1 3 4 2
    1 1 1 2

**Sample Output 4**

    false

**Explanation 4**

![image](1556268518-5dbd54bea2-invaders5.png)

**Sample Input 5**

    1 1 4 3
    2 2 1 1

**Sample Output 5**

    true

**Explanation 5**

![image](1556268609-e363207d98-invaders6.png)

**Sample Input 6**

    -2 -1 4 3
    1 0 2 2

**Sample Output 6**

    true

**Explanation 6**

![image](1556268707-ce9cb439e8-invaders7.png)

**Sample Input 7**

    20 -20 40 80
    20 20 60 80

**Sample Output 7**

    true

**Sample Input 8**

    0 0 10 10
    0 0 10 10

**Sample Output 8**

    true

**Sample Input 9**

    0 0 1 1
    1 0 1 1

**Sample Output 9**

    false

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
