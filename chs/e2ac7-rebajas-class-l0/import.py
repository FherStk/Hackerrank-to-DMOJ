
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="e2ac7-rebajas-class-"
p.name="[e2ac7] Rebaixes #class #L0"
p.summary="Rebaixes"
p.description='''\-

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    producto1 10
    15

**Sample Output 0**

    Producto{descripcion='producto1', precio=10.0}
    Producto{descripcion='producto1', precio=8.5}

**Sample Input 1**

    productoX 100
    25

**Sample Output 1**

    Producto{descripcion='productoX', precio=100.0}
    Producto{descripcion='productoX', precio=75.0}

**Sample Input 2**

    productoV 4.5
    1.5

**Sample Output 2**

    Producto{descripcion='productoV', precio=4.5}
    Producto{descripcion='productoV', precio=4.4325}

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
