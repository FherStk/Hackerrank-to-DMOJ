
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="a-hello-you"
p.name="[f947e] Hello you  #scanner"
p.summary="Saluda a una persona"
p.description='''Donat el nom d'una persona, fes-li una salutació

**Input Format**

Un string  amb el nom d'una persona

**Constraints**

\-

**Output Format**

La paraula "Hola" seguida d'un espai en blanc, el nom de la persona, i
una exclamació "\!"

**Sample Input 0**

    Joan

**Sample Output 0**

    Hola Joan!

**Sample Input 1**

    Anna

**Sample Output 1**

    Hola Anna!

**Sample Input 2**

    Josep Antoni

**Sample Output 2**

    Hola Josep Antoni!

**Sample Input 3**

    Maria Elena

**Sample Output 3**

    Hola Maria Elena!
'''
p.is_public=True
p.date=timezone.now()
p.save()
