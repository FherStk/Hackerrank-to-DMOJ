
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="vocales-mayusculas"
p.name="Vocales Mayúsculas"
p.summary="Cambia las vocales minúsculas a mayúsculas"
p.description='''Dado un texto (con varios saltos de línea), cambia las vocales en
minúscula a mayúscula.

**Input Format**

Un texto con varios saltos de línea. El texto termina con la palabra END
(que no debe procesarse)

**Constraints**

1 \<= L \<= 100

**Output Format**

El mismo texto con las vocales en mayúscula.

**Sample Input 0**

    hola mundo!
    END

**Sample Output 0**

    hOlA mUndO!

**Sample Input 1**

    aae io uu
    ae, iii.
    OU
    END

**Sample Output 1**

    AAE IO UU
    AE, III.
    OU

**Sample Input 2**

    lorem ipsum dolor sit amet,
    consectetur adipiscing elit.
    Aliquam ut iaculis enim,
    sit amet tempor massa.
    END

**Sample Output 2**

    lOrEm IpsUm dOlOr sIt AmEt,
    cOnsEctEtUr AdIpIscIng ElIt.
    AlIqUAm Ut IAcUlIs EnIm,
    sIt AmEt tEmpOr mAssA.

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
