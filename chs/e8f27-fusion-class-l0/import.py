
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="e8f27-fusion-class-l0"
p.name="[e8f27] Fusion #class #L0"
p.summary="Fusion"
p.description='''Crea el mètode Fusion.fusionar()

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    Goku: fuerza=100, velocidad=100
    Vegeta: fuerza=90, velocidad=90
    Goten: fuerza=80, velocidad=100
    Trunks: fuerza=70, velocidad=90
    Gotenks: fuerza=150, velocidad=190
    Gogeta: fuerza=190, velocidad=190
'''
p.is_public=True
p.date=timezone.now()
p.save()
