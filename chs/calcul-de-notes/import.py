
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="calcul-de-notes"
p.name="[de5a8] Càlcul de notes #if"
p.summary="Càlcul de notes"
p.description='''Donada una entrada de teclat corresponent a la marca numèrica d'un
examen, el programa imprimirà la qualificació textual corresponent:

  - Menys de 5: INSUFICIENT
  - 5 a 6 (no inclòs): SUFICIENT
  - 6 a 7 (no inclòs): BE
  - 7 a 8.5 (no inclòs): NOTABLE
  - 8.5 a 10 (no inclòs): EXCEL.LENT
  - 10: MATRICULA

**Input Format**

Un número flotant corresponent a la nota

**Constraints**

\-

**Output Format**

{ INSUFICIENT | SUFICIENT | BE | NOTABLE | EXCEL.LENT | MATRICULA }

**Sample Input 0**

    4.5

**Sample Output 0**

    INSUFICIENT

**Sample Input 1**

    4.999

**Sample Output 1**

    INSUFICIENT

**Sample Input 2**



**Sample Output 2**

    SUFICIENT

**Sample Input 3**

    5.999

**Sample Output 3**

    SUFICIENT

**Sample Input 4**



**Sample Output 4**



**Sample Input 5**

    6.999

**Sample Output 5**



**Sample Input 6**



**Sample Output 6**

    NOTABLE

**Sample Input 7**

    8.499

**Sample Output 7**

    NOTABLE

**Sample Input 8**

    8.5

**Sample Output 8**

    EXCEL.LENT

**Sample Input 9**

    9.255

**Sample Output 9**

    EXCEL.LENT

**Sample Input 10**

    9.999

**Sample Output 10**

    EXCEL.LENT

**Sample Input 11**



**Sample Output 11**

    MATRICULA

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
