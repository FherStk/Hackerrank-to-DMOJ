
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="desglose-de-cantidades-en-monedas"
p.name="[a2ae3] Desglossament en monedes #if"
p.summary="Desglossament en monedes"
p.description='''Calculi el desglossament d'una quantitat en monedes, de tal forma que es
minimitzi el número de monedes utilitzades en el desglossament.

Les monedes que es poden usar per al desglossament són: 500, 100, 50, 5,
1

**Input Format**

Un número enter indicant la quantitat a desglossar

**Constraints**

\-

**Output Format**

Imprimeix el número utlitzat de cada moneda utilitzat en el
desglossament, ordenades per valor.

Si una moneda no s'utilitza en el desglossament, no s'ha d'imprimir.

Si solament s'utilitza 1 moneda en el desglossament, s'ha d'imprimir
"moneda" en singular.

**Sample Input 0**

    649

**Sample Output 0**

    1 moneda de 500
    1 moneda de 100
    9 monedes de 5
    4 monedes de 1

**Sample Input 1**

    2026

**Sample Output 1**

    4 monedes de 500
    5 monedes de 5
    1 moneda de 1
'''
p.is_public=True
p.date=timezone.now()
p.save()
