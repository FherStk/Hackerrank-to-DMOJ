
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="contractar-un-progra"
p.name="Contractar un programador  #operadors"
p.summary="Contractar un programador"
p.description='''Una empresa necessita programadors Java i Python. En el procés de
selecció de programadors l'empresa té en compte si es coneix el
llenguatge i els anys d'experiència laboral amb el llenguatge.

L'empresa vol contractar:

a) programadors que coneguin Java i portin  any o més programant en
Java

b) programadors que coneguin Python i portin  anys o més progamant en
Python

Escriu un programa que a partir de les dades digui si passa el procés de
selecció.

**Input Format**

L'entrada consta de 4 dades.

  - un boolea indicant si coneix Java

  - un enter indicant els anys d'experiència en Java

  - un boolea indicant si coneix Python

  - un enter indicant els anys d'experiència en Python

**Constraints**

\-

**Output Format**

 | 

**Sample Input 0**

    true 1
    false 0

**Sample Output 0**

    true

**Sample Input 1**

    false 0
    true 3

**Sample Output 1**

    true

**Sample Input 2**

    true 0
    true 2

**Sample Output 2**

    false

**Sample Input 3**

    true 3
    true 2

**Sample Output 3**

    true

**Sample Input 4**

    false 1
    false 1

**Sample Output 4**

    false

**Explanation 4**

Inexplicablement, aquest candidat té 1 any d'experiència en Java, però
no coneix el llenguatge...

**Sample Input 5**

    false 0
    true 2

**Sample Output 5**

    false

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
