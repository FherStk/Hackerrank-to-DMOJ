
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l1-12-artropodes"
p.name="[c36a9] Artròpodes #operadors #aritmetics"
p.summary="Artròpodes"
p.description='''En la classe de Naturals estan estudiant els artròpodes. Són animals
invertebrats dotats d'un esquelet extern i apèndixs articulats. Es
divideixen en insectes, aràcnids, crustacis i miriàpodes. El nombre de
potes en aquests animals és molt variable:

  - Els insectes tenen 6 potes

  - Els aràcnids tenen 8 potes

  - Els crustacis tenen 10 potes

  - Els miriàpodes tenen 2 o 4 potes per cada segment del seu cos

![image](1555875809-a55c59095f-artropodes.png)

Un dia la professora va demanar als alumnes que portessin artròpodes a
classe i els va posar un problema de matemàtiques: calcular el nombre de
pates de tots els animals que havien portat.

**Input Format**

El primer nombre  indica el nombre d'insectes.

El segon nombre  indica el nombre d'aràcnids.

El tercer nombre  indica el nombre de crustacis.

El quart nombre  indica el nombre de miriàpodes de 2 potes i el cinquè
el nombre  el nombre de segments que tenen.

El sisè nombre  indica el nombre de miriàpodes de 4 potes i el setè
nombre  el nombre de segments que tenen.

**Constraints**

\-

**Output Format**

Un nombre indicant la quantitat total de potes.

**Sample Input 0**

    1
    0
    0
    0 10
    0 10

**Sample Output 0**



**Explanation 0**

Només hi ha un insecte, per tant 6 potes

**Sample Input 1**

    0
    1 
    0
    0 5
    0 5

**Sample Output 1**



**Explanation 1**

Només hi ha un aràcnid, per tant 8 potes

**Sample Input 2**

    0
    0
    2
    0 12
    0 14

**Sample Output 2**



**Explanation 2**

Només hi ha 2 crustacis, per tant 20 potes

**Sample Input 3**

    0
    0
    0
    1 10
    0 12

**Sample Output 3**



**Explanation 3**

Hi ha un miriàpode de 10 segments (2 potes per segment), per tant 20
potes

**Sample Input 4**

    0
    0
    0
    0 8
    1 10

**Sample Output 4**



**Explanation 4**

Hi ha un miriàpode (de 4 potes per segment) amb 10 segments, per tant 40
potes

**Sample Input 5**

    1
    1
    1
    1 10
    1 10

**Sample Output 5**



**Sample Input 6**

    7
    11
    5
    3 10
    2 12

**Sample Output 6**

    336
'''
p.is_public=True
p.date=timezone.now()
p.save()
