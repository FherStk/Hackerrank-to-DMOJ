
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c4-l0-1-altura-minima"
p.name="[b4322] Altura mínima #arrays"
p.summary="Altura mínima"
p.description='''![image](1573811284-7756e2e813-Untitleddrawing1.png)

Avuí a l'escola fan una sortida al parc d'atraccions. La professora ha
apuntat l'alçada de cada nen i nena, per veure qui podrà pujar a la
muntanya russa i qui no.

**Input Format**

L'entrada consta de tres parts:

  - El primer nombre
    indica el nombre de nens i nenes (*int*)
  - A continuació venen les seves alçades (*float*)
  - Per últim, el nombre
    indica l'alçada mínima de la muntanya russa (*float*)

**Constraints**

\-

**Output Format**

S'imprimirà  o  en una línia, per a cadascun dels nens i nenes

**Sample Input 0**

    5
    1.50   1.40   1.55   1.35   1.40
    
    1.45

**Sample Output 0**

    SI
    NO
    SI
    NO
    NO

**Sample Input 1**

    3
    1.30  1.40  1.50
    
    1.40

**Sample Output 1**

    NO
    SI
    SI

**Sample Input 2**

    4
    1.44  1.45  1.46  1.47
    
    1.44

**Sample Output 2**

    SI
    SI
    SI
    SI

**Sample Input 3**

    1
    1.51
    
    1.51

**Sample Output 3**



**Sample Input 4**

    10
    1.46 1.43 1.56 1.57 1.50 1.51 1.39 1.45 1.60 1.47
    
    1.50

**Sample Output 4**

    NO
    NO
    SI
    SI
    SI
    SI
    NO
    NO
    SI
    NO
'''
p.is_public=True
p.date=timezone.now()
p.save()
