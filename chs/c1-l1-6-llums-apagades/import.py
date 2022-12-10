
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l1-6-llums-apagades"
p.name="[dcbf4] Llums apagats  #operadors #logics"
p.summary="Llums apagats"
p.description='''S'està realitzant una aplicació per a controlar els llums d'una casa.
L'aplicació ha de mostrar si tots els llums de la casa estan apagats. En
total hi ha 4 llums.

**Input Format**

La entrada consta de 4 valors booleans que indiquen si cadascun dels
llums està encés o apagat.

 =\> encés

 =\> apagat

**Constraints**

\-

**Output Format**

S'ha d'imprimir  si tots els llums estan apagats, i  si hi
ha algún llum encés.

**Sample Input 0**

    false false false false

**Sample Output 0**

    true

**Explanation 0**

Tots els llums estan apagats

**Sample Input 1**

    true false false false

**Sample Output 1**

    false

**Explanation 1**

El primer llum està encés

**Sample Input 2**

    false false false true

**Sample Output 2**

    false

**Explanation 2**

L'últim llum està encés
'''
p.is_public=True
p.date=timezone.now()
p.save()
