
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="ete1"
p.name="Primero igual al último"
p.summary="Decir si el primer número leído es igual al último"
p.description='''Se deben ir leyendo números hasta que se lea un 0. El programa debe
mostrar "SI" en caso de que el primer número leído sea igual al último
número leído antes que el 0. En caso contrario debe mostrar "NO".

**Input Format**

Un secuencia de N números enteros que finaliza con un 0.

**Constraints**

1 \<= N \<= 10^7

**Output Format**

"SI" o "NO"

**Sample Input 0**

    1 2 3 2 1 0

**Sample Output 0**



**Sample Input 1**

    1 0

**Sample Output 1**



**Sample Input 2**

    1 2 0

**Sample Output 2**



**Sample Input 3**

    1 2 1 2 1 2 1 0

**Sample Output 3**



**Sample Input 4**

    -1 1 -1 1 -1 0

**Sample Output 4**



**Sample Input 5**



**Sample Output 5**



**Sample Input 6**

    1 2 3 4 0

**Sample Output 6**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
