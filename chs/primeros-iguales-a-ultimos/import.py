
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="primeros-iguales-a-ultimos"
p.name="Primeros iguales a últimos"
p.summary="Para cada caso de prueba, decir si el primer número leído es igual al último."
p.description='''Para cada caso de prueba, se deben ir leyendo números hasta que se lea
un 0. El programa debe mostrar "SI" en caso de que el primer número
leído sea igual al último número leído antes que el 0. En caso
contrario debe mostrar "NO".

**Input Format**

El primer número (T) indica el número de casos de prueba. A continuación
viene una secuencia de N números por cada caso de prueba. Cada secuencia
finaliza con un 0.

**Constraints**

1 \<= T \<= 100 1 \<= N \<= 10^7

**Output Format**

Un "SI" o un "NO" por cada caso de prueba, separados por un salto de
linea "\n"

**Sample Input 0**

    1
    1 2 3 1 0

**Sample Output 0**



**Sample Input 1**

    1
    1 2 3 4 0

**Sample Output 1**



**Sample Input 2**

    2
    1 2 3 1 0
    1 2 2 1 0

**Sample Output 2**

    SI
    SI

**Sample Input 3**

    2
    1 2 3 1 0
    1 2 3 4 0

**Sample Output 3**

    SI
    NO

**Sample Input 4**

    4
    1 2 1 2 0
    1 1 1 2 0
    1 2 2 1 1 0
    -1 0

**Sample Output 4**

    NO
    NO
    SI
    SI

**Sample Input 5**

    3
    5 4 2 0
    6 4 3 6 0
    4 0

**Sample Output 5**

    NO
    SI
    SI

**Sample Input 6**

    2
    6 7 4 9 0
    9 9 9 8 0

**Sample Output 6**

    NO
    NO
'''
p.is_public=True
p.date=timezone.now()
p.save()
