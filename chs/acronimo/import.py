
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="acronimo"
p.name="[C5-L1-3] Acrònims #strings"
p.summary="Acrònims"
p.description='''En el món de la informàtica els acrònims són molt comuns:
<https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations>

Transforma una frase en el seu acrònim.

![image](1557483137-04b68bf814-smfw.png)

**Input Format**

Una frase en una línia.

**Constraints**

\-

**Output Format**

L'acrònim de la frase

**Sample Input 0**

    Hello world!

**Sample Output 0**



**Sample Input 1**

    is this the real life

**Sample Output 1**

    ITTRL

**Sample Input 2**

    what the font

**Sample Output 2**

    WTF

**Sample Input 3**

    Read the fucking manual

**Sample Output 3**

    RTFM

**Sample Input 4**

    GNU's not Unix

**Sample Output 4**

    GNU

**Sample Input 5**

    PHP Hypertext Preprocessor

**Sample Output 5**

    PHP

**Sample Input 6**

    What you see is what you get

**Sample Output 6**

    WYSIWYG
'''
p.is_public=True
p.date=timezone.now()
p.save()
