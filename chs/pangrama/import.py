
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="pangrama"
p.name="[f6471] Pangrama"
p.summary="Pangrama"
p.description='''Donat un text, dir si utilitza **totes** les lletres de l'alfabet.

Alfabet:

    abcdefghijklmnopqrstuvwxyz

**Input Format**

Un text en una sola línia

**Constraints**

\-

**Output Format**

true | false

**Sample Input 0**

    the quick brown fox jumps over the lazy dog

**Sample Output 0**

    true

**Sample Input 1**

    grumpy wizards make toxic brew for the evil queen and jack

**Sample Output 1**

    true

**Sample Input 2**

    jackdaws love my big sphinx of quartz

**Sample Output 2**

    true

**Sample Input 3**

    hello world of java programming

**Sample Output 3**

    false

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
