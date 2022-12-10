
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c6-l1-3-lineseparator"
p.name="[c71c4] LineSeparator #class #L0"
p.summary="LineSeparator"
p.description='''Completa el mètode main():

  - Crea un objecte de la classe LineSeparator
  - Estableix el tamany de la linea a partir de la dades d'entrada.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    3 5 7   -1

**Sample Output 0**

    Aqui sota hi surt una line de 3 guions
    ---
    Aqui sota hi surt una line de 5 guions
    -----
    Aqui sota hi surt una line de 7 guions
    -------

**Sample Input 1**

    10 20 30   -1

**Sample Output 1**

    Aqui sota hi surt una line de 10 guions
    ----------
    Aqui sota hi surt una line de 20 guions
    --------------------
    Aqui sota hi surt una line de 30 guions
    ------------------------------
'''
p.is_public=True
p.date=timezone.now()
p.save()
