
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="ec528-producte-class-l0"
p.name="[ec528] Producte #class"
p.summary="Producte "
p.description='''Assigna els valors als camps de l'objecte  a partir de les
dades de l'entrada.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    Corsair Vengeance RGB Pro
    DDR4 3200 PC4-25600 16GB 2x8GB CL16
    109
    25

**Sample Output 0**

    Nom:        Corsair Vengeance RGB Pro
    Descripcio: DDR4 3200 PC4-25600 16GB 2x8GB CL16
    Preu:       109.0
    Stock:      25

**Sample Input 1**

    Kingston HyperX Fury Black
    16GB DDR4 2666Mhz PC-21300 (2x8GB) CL16
    79.5
    3

**Sample Output 1**

    Nom:        Kingston HyperX Fury Black
    Descripcio: 16GB DDR4 2666Mhz PC-21300 (2x8GB) CL16
    Preu:       79.5
    Stock:      3

**Sample Input 2**

    G.Skill Trident Z RGB
    DDR4 3200 PC4-25600 16GB 2x8GB CL16
    113.39
    55

**Sample Output 2**

    Nom:        G.Skill Trident Z RGB
    Descripcio: DDR4 3200 PC4-25600 16GB 2x8GB CL16
    Preu:       113.39
    Stock:      55
'''
p.is_public=True
p.date=timezone.now()
p.save()
