
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="secuencias-rotativas"
p.name="[ddcb9] Parin les rotatives!"
p.summary="Parin les rotatives!"
p.description='''A la redacció del periòdic arriba una notícia molt important... parin
les rotatives\!\!

La màquina rotativa del periòdic és així:

![image](1556790353-d3d6097268-rodillo1.png)

En un rodet està el text que es va a imprimir. Aleshores el rodet
comença a rodar i el paper va corrent per sota.

**Input Format**

El primer número  indica el tamany de la seqüència. A continuació ve la
seqüència de números a imprimir.

Després ve la quantitat de números  que s'havien imprés en el moment en
que es para la rotativa.

**Constraints**

\-

**Output Format**

La seqüència de números impresos separada per espais.

**Sample Input 0**

    3    100 200 300
    5

**Sample Output 0**

    100 200 300 100 200

**Sample Input 1**

    3    100 200 300
    7

**Sample Output 1**

    100 200 300 100 200 300 100

**Sample Input 2**

    3    100 200 300
    2

**Sample Output 2**

    100 200

**Sample Input 3**

    5    100 200 300 400 500
    4

**Sample Output 3**

    100 200 300 400

**Sample Input 4**

    3    10 20 30
    10

**Sample Output 4**

    10 20 30 10 20 30 10 20 30 10

**Sample Input 5**

    3    1 2 3
    20

**Sample Output 5**

    1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
