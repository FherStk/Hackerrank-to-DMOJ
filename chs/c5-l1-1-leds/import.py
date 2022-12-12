
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c5-l1-1-leds"
p.name="[dafef] Leds #class #L0"
p.summary="Leds"
p.description='''Implementa els mètodes switchOn() i switchOff() de la classe Led.

  - switchOn() canvia la variable 'state' a 'true'
  - switchOff() canvia la variable 'state' a 'false'

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    ( )( )
    (*)( )
    (*)(*)
    ( )(*)

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
