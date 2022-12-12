
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c3-l2-3-l33t"
p.name="[C3-L2-3] l33t #for"
p.summary="l33t"
p.description='''El l33t no té regles, però un algoritme sí. Posem aquestes:

1.  Es substitueixen aquestes lletres:

<!-- end list -->

    A: 4
    B: 8
    E: 3
    G: 6
    I: !
    L: 1
    M: /\/    O: 0
    S: 5
    T: 7
    U: |_|
    V: \//
    W: \/\/
    Z: 2

2.  La resta de lletres s'escriuen alternant minúscules i majúscules

3.  S'eliminen els punts i les comes

**Input Format**

Un text amb  linies. El text acaba amb una línia amb la paraula .

**Constraints**

\-

**Output Format**

El text en llengua l33t

**Sample Input 0**

    Hello leet
    END

**Sample Output 0**

    h3110 1337

**Sample Input 1**

    goodbye world
    END

**Sample Output 1**

    600d8Y3 \/\/0r1D

**Sample Input 2**

    all your base are belong to us
    END

**Sample Output 2**

    411 y0|_|R 8453 4r3 8310N6 70 |_|5

**Sample Input 3**

    Lorem ipsum 
    dolor sit amet, 
    consectetur adipiscing elit.
    END

**Sample Output 3**

    10r3/\/\ !P5|_|/\/\ 
    d010R 5!7 4/\/\37 
    c0N53c737|_|R 4d!P!5c!N6 31!7

**Sample Input 4**

    This isn't even, 
    my final form.
    END

**Sample Output 4**

    7h!5 !5N'7 3\//3N 
    /\/\y F!n41 F0r/\/
**Sample Input 5**

    If the Tao is great, then the operating system is great. 
    If the operating system is great, then the compiler is great. 
    If the compiler is great, then the application is great. 
    The user is pleased, and there is harmony in the world.
    END

**Sample Output 5**

    !f 7H3 740 !5 6r347 7H3n 7H3 0p3R47!n6 5Y573/\/\ !5 6r347 
    !F 7h3 0P3r47!N6 5y573/\/\ !5 6R347 7h3N 7h3 C0/\/\p!13R !5 6r347 
    !F 7h3 C0/\/\p!13R !5 6r347 7H3n 7H3 4pP1!c47!0N !5 6r347 
    7H3 |_|53r !5 P13453d 4Nd 7H3r3 !5 H4r/\/\0Ny !N 7h3 \/\/0R1d

**Sample Input 6**

    It's over 9000!
    END

**Sample Output 6**

    !7'5 0\//3R 9000!

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
