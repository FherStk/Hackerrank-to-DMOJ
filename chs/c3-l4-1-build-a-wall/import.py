
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c3-l4-1-build-a-wall"
p.name="[b490c] Another brick in the wall #for"
p.summary="Build a wall"
p.description='''L'any 1978, el mític grup Pink Floyd va publicar el seu 11è disc: The
Wall. A les seves actuacions, Pink FLoyd, sempre utilitzaven efectes
visuals per acompanyar la seva psicodèlica música rock. Per al tour de
The Wall, un enorme mur es construïa a l'escenari entre la banda i el
públic.

![image](1557178012-c19859ff70-PinkFloydWallCoverOriginalNoText.jpg)

En aquesta ocasió la banda ens demana una aplicació que generi un mur
ASCII-ART per a projectar a l'escenari.

**Input Format**

L'entrada consisteix en 4 nombres: amplada del maó, alçada del maó,
nombre de maons per línia, nombre de línies de maons.

**Constraints**

No hi ha restriccions significatives.

**Output Format**

S'imprimirà un mur de les dimensions especificades. El mur ha de
començar amb un maó complet.

Exemple de mur 8-1-3-3:

    ----------------------------
    |        |        |        |
    ----------------------------
        |        |        |
    ----------------------------
    |        |        |        |
    ----------------------------

**Sample Input 0**

    8 1 4 3

**Sample Output 0**

    -------------------------------------
    |        |        |        |        |
    -------------------------------------
        |        |        |        |
    -------------------------------------
    |        |        |        |        |
    -------------------------------------

**Sample Input 1**

    6 1 5 4

**Sample Output 1**

    ------------------------------------
    |      |      |      |      |      |
    ------------------------------------
       |      |      |      |      |
    ------------------------------------
    |      |      |      |      |      |
    ------------------------------------
       |      |      |      |      |
    ------------------------------------

**Sample Input 2**

    6 2 4 3

**Sample Output 2**

    -----------------------------
    |      |      |      |      |
    |      |      |      |      |
    -----------------------------
       |      |      |      |
       |      |      |      |
    -----------------------------
    |      |      |      |      |
    |      |      |      |      |
    -----------------------------

**Sample Input 3**

    6 3 4 2

**Sample Output 3**

    -----------------------------
    |      |      |      |      |
    |      |      |      |      |
    |      |      |      |      |
    -----------------------------
       |      |      |      |
       |      |      |      |
       |      |      |      |
    -----------------------------

**Sample Input 4**

    8 1 6 10

**Sample Output 4**

    -------------------------------------------------------
    |        |        |        |        |        |        |
    -------------------------------------------------------
        |        |        |        |        |        |
    -------------------------------------------------------
    |        |        |        |        |        |        |
    -------------------------------------------------------
        |        |        |        |        |        |
    -------------------------------------------------------
    |        |        |        |        |        |        |
    -------------------------------------------------------
        |        |        |        |        |        |
    -------------------------------------------------------
    |        |        |        |        |        |        |
    -------------------------------------------------------
        |        |        |        |        |        |
    -------------------------------------------------------
    |        |        |        |        |        |        |
    -------------------------------------------------------
        |        |        |        |        |        |
    -------------------------------------------------------
'''
p.is_public=True
p.date=timezone.now()
p.save()
