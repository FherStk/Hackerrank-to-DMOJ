
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="ebeac-fighters-class-l0"
p.name="[ebeac] Fighters #class #L0"
p.summary="Fighters"
p.description='''Implementa el mètode Fight.winner()

El resultat del combat es decideix en funció de les característiques
dels combatents. Guanya el que tingui la suma de força, velocitat i
agilitat més alta. Si els dos combatents tenen la mateixa es produeix un
DOBLE KO.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    ryu 80 90 80
    honda 100 60 50

**Sample Output 0**

    ryu

**Sample Input 1**

    blanka 80 80 80
    chun-li 60 90 100

**Sample Output 1**

    chun-li

**Sample Input 2**

    ryu 80 90 80
    ken 80 80 90

**Sample Output 2**

    DOUBLE KO
'''
p.is_public=True
p.date=timezone.now()
p.save()
