
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="lipograma"
p.name="[C5-L1-1] Lipograma #strings"
p.summary="Lipograma"
p.description='''Donat un text i una lletra, dir si el text **omet** aquesta lletra.

**Input Format**

En primer lloc va el text, en vàries línies, i acabat amb .

A continuació ve el caràcter.

**Constraints**

\-

**Output Format**

true | false

**Sample Input 0**

    Hello world!
    END
    e

**Sample Output 0**

    false

**Sample Input 1**

    Hello World!
    END
    a

**Sample Output 1**

    true

**Sample Input 2**

    Hello World!
    END
    u

**Sample Output 2**

    true

**Sample Input 3**

    Lorem ipsum 
    dolor sit amet, 
    consectetur adipiscing elit
    END
    x

**Sample Output 3**

    true

**Sample Input 4**

    Lorem ipsum 
    dolor sit amet, 
    consectetur adipiscing
    END
    g

**Sample Output 4**

    false
'''
p.is_public=True
p.date=timezone.now()
p.save()
