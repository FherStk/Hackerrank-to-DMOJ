
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c5-l1-2"
p.name="[c872c] Array de leds #class #L0"
p.summary="Array de Leds"
p.description='''Implementa el mètode switchLed de la classe LedArray. El mètode rep com
a paràmetre la posició d'un led, i inverteix el seu estat.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    1 2 3 2   -1

**Sample Output 0**

    ( )(*)( )( )( )
    ( )(*)(*)( )( )
    ( )(*)(*)(*)( )
    ( )(*)( )(*)( )

**Sample Input 1**

    0 4 2   -1

**Sample Output 1**

    (*)( )( )( )( )
    (*)( )( )( )(*)
    (*)( )(*)( )(*)

**Sample Input 2**

    0 3 2 4 1 0 4 0 3 2 1   -1

**Sample Output 2**

    (*)( )( )( )( )
    (*)( )( )(*)( )
    (*)( )(*)(*)( )
    (*)( )(*)(*)(*)
    (*)(*)(*)(*)(*)
    ( )(*)(*)(*)(*)
    ( )(*)(*)(*)( )
    (*)(*)(*)(*)( )
    (*)(*)(*)( )( )
    (*)(*)( )( )( )
    (*)( )( )( )( )

**Sample Input 3**

    0 2 4 1 3 0 2 4 1 3  -1

**Sample Output 3**

    (*)( )( )( )( )
    (*)( )(*)( )( )
    (*)( )(*)( )(*)
    (*)(*)(*)( )(*)
    (*)(*)(*)(*)(*)
    ( )(*)(*)(*)(*)
    ( )(*)( )(*)(*)
    ( )(*)( )(*)( )
    ( )( )( )(*)( )
    ( )( )( )( )( )
'''
p.is_public=True
p.date=timezone.now()
p.save()
