
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="d3da3-paper-rock-sci"
p.name="[d3da3] Paper, rock, scissors #class #L0"
p.summary="Paper, rock, scissors"
p.description='''Implementa les classes Game i Player

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    4 ## @# %# %@

**Sample Output 0**

    PLAYER 2 WINS

**Sample Input 1**

    6 #@ %@ %# #% %@ @%

**Sample Output 1**

    TIE

**Sample Input 2**

    6 @% @% %# %# #% #@

**Sample Output 2**

    PLAYER 1 WINS

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
