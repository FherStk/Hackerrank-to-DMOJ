
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="hora-dapertura-operadors-ternari"
p.name="Hora d'apertura  #operadors #ternari"
p.summary="Hora d'apertura  #operadors #ternari"
p.description='''Un local té horaris d'apertura diferents entre setmana i el cap de
setmana.

Entre setmana obri a les 8:00, y els cap de setmana a les 10:00.

**Input Format**

L'entrada és un dia de la setmana.

**Constraints**

\-

**Output Format**

 | 

**Sample Input 0**

    Dilluns

**Sample Output 0**

    8:00

**Sample Input 1**

    Dimarts

**Sample Output 1**

    8:00

**Sample Input 2**

    Dimecres

**Sample Output 2**

    8:00

**Sample Input 3**

    Dijous

**Sample Output 3**

    8:00

**Sample Input 4**

    Divendres

**Sample Output 4**

    8:00

**Sample Input 5**

    Dissabte

**Sample Output 5**

    10:00

**Sample Input 6**

    Diumenge

**Sample Output 6**

    10:00
'''
p.is_public=True
p.date=timezone.now()
p.save()
