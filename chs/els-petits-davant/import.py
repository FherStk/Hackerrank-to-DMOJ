
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="els-petits-davant"
p.name="Els petits davant  #operadors"
p.summary="Els petits davant"
p.description='''Escriu un programa que llegeixi tres números i digui si estan ordenats
de menor a major.

**Input Format**

tres números enters

**Constraints**

\-

**Output Format**

 | 

**Sample Input 0**

    1 2 3

**Sample Output 0**

    true

**Sample Input 1**

    1 3 2

**Sample Output 1**

    false

**Sample Input 2**

    2 1 3

**Sample Output 2**

    false

**Sample Input 3**

    2 3 1

**Sample Output 3**

    false

**Sample Input 4**

    3 1 2

**Sample Output 4**

    false

**Sample Input 5**

    3 2 1

**Sample Output 5**

    false

**Sample Input 6**

    1 1 1

**Sample Output 6**

    true

**Sample Input 7**

    1 1 2

**Sample Output 7**

    true

**Sample Input 8**

    1 2 1

**Sample Output 8**

    false

**Sample Input 9**

    1 2 2

**Sample Output 9**

    true

**Sample Input 10**

    10 1000 1000000

**Sample Output 10**

    true

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
