
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c6-l2-3-gearbox"
p.name="[ff910] GearBox"
p.summary="GearBox"
p.description='''Implementa els mètodes GearBox.gearUp() i GearBox.gearDown()

  - gearUp() incrementa la 'gear' en 1. Quan s'arriba a límit
    'numGears', no s'ha d'incrementar

  - gearDown() decrementa la 'gear' en 1. Quan s'arriba a '-1' (marxa
    enrere), no s'ha de decrementar

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    5
    UP
    UP
    UP
    DOWN
    DOWN
    __END__

**Sample Output 0**

    Current gear: 1
    Current gear: 2
    Current gear: 3
    Current gear: 2
    Current gear: 1

**Sample Input 1**

    6
    UP
    UP
    DOWN
    DOWN
    DOWN
    __END__

**Sample Output 1**

    Current gear: 1
    Current gear: 2
    Current gear: 1
    Current gear: N
    Current gear: R

**Sample Input 2**

    5
    UP
    UP
    UP
    UP
    UP
    UP
    __END__

**Sample Output 2**

    Current gear: 1
    Current gear: 2
    Current gear: 3
    Current gear: 4
    Current gear: 5
    Current gear: 5

**Sample Input 3**

    5
    UP
    UP
    UP
    UP
    UP
    UP
    DOWN
    DOWN
    DOWN
    DOWN
    DOWN
    DOWN
    DOWN
    DOWN
    __END__

**Sample Output 3**

    Current gear: 1
    Current gear: 2
    Current gear: 3
    Current gear: 4
    Current gear: 5
    Current gear: 5
    Current gear: 4
    Current gear: 3
    Current gear: 2
    Current gear: 1
    Current gear: N
    Current gear: R
    Current gear: R
    Current gear: R
'''
p.is_public=True
p.date=timezone.now()
p.save()
