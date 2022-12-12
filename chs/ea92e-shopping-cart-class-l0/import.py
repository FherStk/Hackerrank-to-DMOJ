
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="ea92e-shopping-cart-"
p.name="[ea92e] Shopping Cart #class #L0"
p.summary="Shopping Cart"
p.description='''Crea les classes necessàries.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    4
    FREKVENS Altavoz, 10x20 cm
    59
    SYMFONISK Altavoz wifi, 31x10x15 cm
    105.9
    ENEBY Altavoz Bluetooth, 20x20 cm
    49.99
    ENEBY Altavoz Bluetooth, 30x30 cm
    89.99

**Sample Output 0**

    ShoppingCart
                  FREKVENS Altavoz, 10x20 cm   59.00
         SYMFONISK Altavoz wifi, 31x10x15 cm  105.90
           ENEBY Altavoz Bluetooth, 20x20 cm   49.99
           ENEBY Altavoz Bluetooth, 30x30 cm   89.99

**Sample Input 1**

    2
    LILLHULT MiniUSB cable, 0.4 m
    2.25
    LILLHULT USB tipo C cable, 1.5 m
    4.45

**Sample Output 1**

    ShoppingCart
               LILLHULT MiniUSB cable, 0.4 m    2.25
            LILLHULT USB tipo C cable, 1.5 m    4.45

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
