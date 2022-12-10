
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c1-l2-2-secret-handshake"
p.name="[C1-L2-2] Secret Handshake #if"
p.summary="Secret Handshake"
p.description='''Hi ha 10 tipus de persones al món: *els que entenen el binari i els que
no*.

Vosaltres i els vostres companys de cohort dels que "sabeu" quan es
tracta d’un binari decidiu crear una "salutació" secreta.

    1 = fer l'ullet
    10 = doble parpalleig
    100 = tancar el ulls
    1000 = saltar

**Input Format**

La entrada consisteix en una seqüència de 4 bits, separats per espais.

**Constraints**

4 bits

**Output Format**

S'escriurà la seqüència d'events de la "salutació" secreta

**Sample Input 0**

    1 0 0 0

**Sample Output 0**

    saltar

**Sample Input 1**

    1 0 0 1

**Sample Output 1**

    tancar els ulls
    fer l'ullet

**Sample Input 2**

    1 0 1 0

**Sample Output 2**

    doble parpalleig
    doble parpalleig

**Sample Input 3**

    1 0 1 1

**Sample Output 3**

    doble parpalleig
    fer l'ullet
    fer l'ullet

**Sample Input 4**

    1 1 0 0

**Sample Output 4**

    fer l'ullet
    tancar els ulls

**Sample Input 5**

    1 1 0 1

**Sample Output 5**

    fer l'ullet
    doble parpalleig
    fer l'ullet

**Sample Input 6**

    1 1 1 0

**Sample Output 6**

    fer l'ullet
    fer l'ullet
    doble parpalleig

**Sample Input 7**

    1 1 1 1

**Sample Output 7**

    fer l'ullet
    fer l'ullet
    fer l'ullet
    fer l'ullet
'''
p.is_public=True
p.date=timezone.now()
p.save()
