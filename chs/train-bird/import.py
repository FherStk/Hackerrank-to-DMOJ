
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="train-bird"
p.name="Train bird #operadors"
p.summary="Train bird"
p.description='''![image](birdtrain.gif)

El problema "A train and a bird" diu així:

*Un tren es troba a 20km de l'estació i s'aproxima a 10km/h cap a
l'estació. Al mateix temps, un ocell vola a 30km/h des de l'estació en
direcció al tren. Quan l'ocell arriba fins al tren, dona mitja volta i
torna cap a l'estació, i quan arriba a l'estació fa una altra vegada
mitja volta fins al tren... i així fins que el tren arriba a l'estació.*

Quants kms recorrerà l'ocell fins que el tren arribi a l'estació?

**Input Format**

L'entrada són tres números decimals:

  - Distancia del tren
  - Velocitat del tren
  - Velocitat de l'ocell

**Constraints**

\-

**Output Format**

S'imprimirà la distància recorreguda per l'ocell en format 

**Suggerència per a la solució**

En primer lloc cal esbrinar el temps que triga el tren en arribar a
l'estació.

Després, segons aquest temps i la velocitat a la que vola l'ocell, es
calcula la distància recorreguda per l'ocell.

**Sample Input 0**

    10
    10
    30

**Sample Output 0**

    30.0

**Explanation 0**

El tren trigarà 1 hora en arribar. L'ocell en 1 hora recorrerà 30 kms.

**Sample Input 1**

    50
    10
    100

**Sample Output 1**

    500.0

**Explanation 1**

El tren trigarà 5 hores en arribar. L'ocell en 5 hores recorrerà 500
kms.

**Sample Input 2**

    15
    30
    80

**Sample Output 2**

    40.0

**Sample Input 3**

    32.5
    65
    55.5

**Sample Output 3**

    27.75

**Sample Input 4**

    200.5
    43.25
    55.35

**Sample Output 4**

    256.59363
'''
p.is_public=True
p.date=timezone.now()
p.save()
