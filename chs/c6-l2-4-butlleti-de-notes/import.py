
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c6-l2-4-butlleti-de-"
p.name="[c621f] Butlletí de notes"
p.summary="Butlletí de notes"
p.description='''Afegeix els camps i mètodes que falten a la classe ReportCard.

*La variable  indica el pes de l'activitat en la nota final*

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    2
    Projecte 10 50
    Examen 0 50

**Sample Output 0**

    Average Grade: 5.00

**Sample Input 1**

    3
    Practiques 9 20
    Exercicis 8 30
    Examen 5 50

**Sample Output 1**

    Average Grade: 6.70

**Sample Input 2**

    5
    Projecte 8 30
    Practica1 9 10
    Practica2 7 10
    Practica3 6 10
    Examen 5 40

**Sample Output 2**

    Average Grade: 6.60

**Sample Input 3**

    3
    Examen1 5 25
    Examen2 6.7 25
    Examen3 10 50

**Sample Output 3**

    Average Grade: 7.93

**Sample Input 4**

    1
    Examen 7.75 100

**Sample Output 4**

    Average Grade: 7.75

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
