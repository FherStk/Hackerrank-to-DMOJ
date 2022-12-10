
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="numero-de-divisores"
p.name="Número de divisores"
p.summary="Escribe un programa calcule la cantidad de divisores de un número."
p.description='''Dado un número, calcula la cantidad de divisores que tiene.

**Input Format**

Un número entero N

**Constraints**

0 \<= N \<= 10^9

**Output Format**

Un número indicando la cantidad de divisores

**Sample Input 0**



**Sample Output 0**



**Explanation 0**

El 6 es divisible por 1, 2, 3 y 6

**Sample Input 1**



**Sample Output 1**



**Explanation 1**

El 12 es divisible por 1, 2, 3, 4, 6 y 12

**Sample Input 2**



**Sample Output 2**



**Explanation 2**

El 17 es divisible por 1 y 17

**Sample Input 3**



**Sample Output 3**



**Sample Input 4**



**Sample Output 4**



**Sample Input 5**



**Sample Output 5**



**Sample Input 6**



**Sample Output 6**



**Sample Input 7**

    5160

**Sample Output 7**



**Sample Input 8**

    9985

**Sample Output 8**



**Sample Input 9**

    9973

**Sample Output 9**


'''
p.is_public=True
p.date=timezone.now()
p.save()
