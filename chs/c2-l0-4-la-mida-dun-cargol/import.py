
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c2-l0-4-la-mida-dun-"
p.name="[ba4d0] La mida d'un cargol #if"
p.summary="La mida d'un cargol"
p.description='''![image](1576672258-b20fcd32e4-cargol.jpg) Crea un programa que a partir
de la mida d'un cargol, mostri el text corresponent a la mida, segons la
taula següent:

  - D’1 cm (inclòs) a 3 cm (no inclòs): petit
  - De 3 cm (inclòs) a 5 cm (no inclòs): mitjà
  - De 5 cm (inclòs) a 8 cm (no inclòs): gran
  - De 8 cm (inclòs) a 10 cm (inclòs): molt gran
  - Qualsevol altre valor indica que la mida del cargol és incorrecta.

**Input Format**

La mida del cargol en centímetres (int).

**Constraints**

\-

**Output Format**

{ petit | mitja | gran | molt gran | mida incorrecta }

**Sample Input 0**



**Sample Output 0**

    petit

**Sample Input 1**



**Sample Output 1**

    mitja

**Sample Input 2**



**Sample Output 2**

    mitja

**Sample Input 3**



**Sample Output 3**

    gran

**Sample Input 4**



**Sample Output 4**

    gran

**Sample Input 5**



**Sample Output 5**

    gran

**Sample Input 6**



**Sample Output 6**

    molt gran

**Sample Input 7**



**Sample Output 7**

    molt gran

**Sample Input 8**



**Sample Output 8**

    molt gran

**Sample Input 9**



**Sample Output 9**

    mida incorrecta

**Sample Input 10**



**Sample Output 10**

    mida incorrecta

**Sample Input 11**



**Sample Output 11**

    mida incorrecta

**Sample Input 12**



**Sample Output 12**

    mida incorrecta

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
