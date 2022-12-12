
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="d5d1e-creditcard-cla"
p.name="[d5d1e] CreditCard #class #L0"
p.summary="CreditCard "
p.description='''Crea la classe .

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    Lola Mento
    1234567812345678
    2000.5
    300

**Sample Output 0**

    LOLA MENTO
    1234 5678 1234 5678 
    Saldo: 2000.5
    Limit: 300.0

**Sample Input 1**

    Elena Nito
    9876543219876543
    0
    1000000

**Sample Output 1**

    ELENA NITO
    9876 5432 1987 6543 
    Saldo: 0.0
    Limit: 1000000.0

**Sample Input 2**

    Penelope Luda
    1234567891234567
    9999999
    0.9

**Sample Output 2**

    PENELOPE LUDA
    1234 5678 9123 4567 
    Saldo: 9999999.0
    Limit: 0.9

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
