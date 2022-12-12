
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c6-l1-4-advancedline"
p.name="[d85a9] AdvancedLineSeparator #class #L0"
p.summary="AdvancedLineSeparator"
p.description='''Completa la classe AdvancedLineSeparator:

  - Afegeix els camps que hi manquen

Completa el mètode Solution.main():

  - Crida adequadament al mètode AdvancedLineSeparator.print()

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    *
    30
    -
    35
    __END__

**Sample Output 0**

    Aqui sota apareix una linea de 30 *
    ******************************
    Aqui sota apareix una linea de 35 -
    -----------------------------------

**Sample Input 1**

    ^
    30
    #
    40
    =
    50
    __END__

**Sample Output 1**

    Aqui sota apareix una linea de 30 ^
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Aqui sota apareix una linea de 40 #
    ########################################
    Aqui sota apareix una linea de 50 =
    ==================================================

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
