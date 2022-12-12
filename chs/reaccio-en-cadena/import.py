
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="reaccio-en-cadena"
p.name="Reacció en cadena #arrays"
p.summary="Reacció en cadena #arrays"
p.description='''![image](1610984838-c68799088b-reaccioencadena0.png)

Hi han una sèrie de bombes col·locades en línia recta i separades per 1
metre.

Quan una bomba explota, la seva ona expansiva fa que explotin totes
aquelles bombes que estiguin dintre del seu abast.

A partir de l'abast de l'ona expansiva de cada bomba, indica quina serà
l'última bomba en explotar si fem explotar la primera de totes.

**Input Format**

El primer nombre  indica la quantitat de bombes que hi ha.

A continuació venen els  abasts de l'ona expansiva de cada bomba.

Per exemple, els següents abasts corresponen a les següents bombes:

    2 1 3 0 1 1

![image](1611047065-2cb4acf98b-reaccioencadenae.png)

**Constraints**

\-

**Output Format**

S'imprimirà la posició de l'última bomba en explotar (començant a
comptar per 1)

**Sample Input 0**

    4
    1 1 0 1

**Sample Output 0**



**Explanation 0**

![image](1611046827-10c04574a5-reaccioencadena0.png)

**Sample Input 1**

    6
    3 1 2 1 0 1

**Sample Output 1**



**Explanation 1**

![image](1611047127-8b7ed9561a-reaccioencadena1.png)

**Sample Input 2**

    4
    2 0 1 0

**Sample Output 2**



**Explanation 2**

![image](1611047166-591b5a7c34-reaccioencadena2.png)

**Sample Input 3**

    5
    4 0 0 0 0

**Sample Output 3**



**Explanation 3**

![image](1611047228-4d4c895af9-reaccioencadena3.png)

**Sample Input 4**

    6
    2 1 0 3 2 2

**Sample Output 4**



**Explanation 4**

![image](1611047265-047cefcc65-reaccioencadena4.png)

**Sample Input 5**

    7
    0 1 1 0 1 0 1

**Sample Output 5**



**Explanation 5**

![image](1611047304-da3fd67741-reaccioencadena5.png)

**Sample Input 6**

    5
    1 1 4 0 0

**Sample Output 6**



**Explanation 6**

![image](1611047337-b2f87007b2-reaccioencadena6.png)

**Sample Input 7**

    10
    3 0 0 2 0 1 8 0 0 0

**Sample Output 7**



**Sample Input 8**

    1
    0

**Sample Output 8**



**Sample Input 9**

    1
    5

**Sample Output 9**



**Sample Input 10**

    4
    2 2 0 1

**Sample Output 10**



**Explanation 10**

![image](1613064771-d693fed1b8-reaccioencadena.png)

**Sample Input 11**

    10
    3 2 2 0 1 2 3 0 0 1 

**Sample Output 11**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
