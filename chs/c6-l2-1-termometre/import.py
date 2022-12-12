
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c6-l2-1-termometre"
p.name="[d52a3] Termòmetre #class #L0"
p.summary="Termòmetre"
p.description='''Implementa els mètodes de la classe Thermometer:

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    0
    100
    
    -273.1
    232.778
    
    -274

**Sample Output 0**

    Termometre 1
       0.00C
      32.00F
     273.15K
    Termometre 2
     100.00C
     212.00F
     373.15K
    --------
    Termometre 1
    -273.10C
    -459.58F
       0.05K
    Termometre 2
     232.78C
     451.00F
     505.93K
    --------

**Sample Input 1**

    100
    100
    
    451
    -173
    
    36.8
    5000
    
    -275

**Sample Output 1**

    Termometre 1
     100.00C
     212.00F
     373.15K
    Termometre 2
     100.00C
     212.00F
     373.15K
    --------
    Termometre 1
     451.00C
     843.80F
     724.15K
    Termometre 2
    -173.00C
    -279.40F
     100.15K
    --------
    Termometre 1
      36.80C
      98.24F
     309.95K
    Termometre 2
    5000.00C
    9032.00F
    5273.15K
    --------

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
