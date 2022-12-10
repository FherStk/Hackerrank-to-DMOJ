
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="superbowling"
p.name="Superbowling"
p.summary="Determina si una cantidad de bolos se puede colocar formando un triangulo completo."
p.description='''En el juego de bolos, los bolos se colocan en filas de manera que en la
primera fila hay un bolo, y en cada fila hay un bolo más que en la
anterior.

![image](1548249910-2030623bda-Untitleddrawing.png)

Dado un número de bolos, determina si es posible organizarlos para que
se forme un triangulo completo, es decir que ninguna fila quede
incompleta.

**Input Format**

Un numero N de bolos

**Constraints**

1 \<= N \<= 100000

**Output Format**

true | false

**Sample Input 0**



**Sample Output 0**

    true

**Explanation 0**

6 bolos se pueden colocar perfectamente:

    o o o
     o o
      o

**Sample Input 1**



**Sample Output 1**

    false

**Explanation 1**

8 bolos no se pueden colocar de forma perfecta. Quedaría incompleto.

    o o
     o o o
      o o
       o

**Sample Input 2**



**Sample Output 2**

    true

**Explanation 2**

21 bolos se pueden colocar perfectamente:

    o o o o o o
     o o o o o
      o o o o
       o o o
        o o
         o

**Sample Input 3**



**Sample Output 3**

    false

**Explanation 3**

Con 4 bolos el triángulo queda incompleto:

    o
     o o
      o

**Sample Input 4**



**Sample Output 4**

    true

**Sample Input 5**



**Sample Output 5**

    true

**Sample Input 6**



**Sample Output 6**

    true

**Sample Input 7**

    990

**Sample Output 7**

    true

**Sample Input 8**

    9870

**Sample Output 8**

    true

**Sample Input 9**

    998991

**Sample Output 9**

    true

**Sample Input 10**

    997570

**Sample Output 10**

    false

**Sample Input 11**



**Sample Output 11**

    false
'''
p.is_public=True
p.date=timezone.now()
p.save()
