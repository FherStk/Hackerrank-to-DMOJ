
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="triler"
p.name="[C2-L3-3] Triler #if"
p.summary="Triler"
p.description='''L'objectiu del joc de triler és que la víctima endevini sota quin dels 3
gobelets es troba la boleta. Els gobelets son manejats per l'estafador,
canviant-los de posició i movent la boleta d'un a l'atre.

![image](1570732092-eeaae46518-path4680.png)

Els moviments del triler tracten de despistar la víctima, però al cap i
a la fi cada moviment es resumeix en: "**Moure la bola a l'esquerra o a
la dreta**".

Representarem l'estat del joc amb un "\*" per al gobelet que té la bola,
i amb "\_" els gobelets que no tenen bola.

**El joc comença amb la bola al primer gobelet** (\* \_ \_ *).
Aleshores, si el triler fa dos moviments cap a la dreta, per exemple, la
bola acabará en el tercer gobelet (* \_ \_ \*).

Els moviments són "circulars", és a dir, si la bola està per exemple al
primer gobelet (\* \_ \_ *) i es fa un moviment a l'esquerra, la bola
passa al tercer gobelet (* \_ \_ \*).

**Input Format**

L'entrada consta de quatre lletres "L" o "R" (separades per espais en
blanc) que indiquen els moviments que fa l'estafador.

**Constraints**

Sempre es realitzen 4 moviments

**Output Format**

S'imprimirà l'estat final dels gobelets, amb un asterisc per al gobelet
on queda la bola, i un guió baix per als gobelets que no la tenen.

**Sample Input 0**

    L L L L 

**Sample Output 0**

    _ _ *

**Explanation 0**











**Sample Input 1**

    L L L R 

**Sample Output 1**

    _ * _

**Explanation 1**











**Sample Input 2**

    L L R L 

**Sample Output 2**

    _ * _

**Explanation 2**











**Sample Input 3**

    L L R R 

**Sample Output 3**

    * _ _

**Explanation 3**











**Sample Input 4**

    L R L L 

**Sample Output 4**

    _ * _

**Explanation 4**











**Sample Input 5**

    L R L R 

**Sample Output 5**

    * _ _

**Sample Input 6**

    L R R L 

**Sample Output 6**

    * _ _

**Sample Input 7**

    L R R R 

**Sample Output 7**

    _ _ *

**Sample Input 8**

    R L L L 

**Sample Output 8**

    _ * _

**Sample Input 9**

    R L L R 

**Sample Output 9**

    * _ _

**Sample Input 10**

    R L R L 

**Sample Output 10**

    * _ _

**Sample Input 11**

    R L R R 

**Sample Output 11**

    _ _ *

**Sample Input 12**

    R R L L 

**Sample Output 12**

    * _ _

**Sample Input 13**

    R R L R 

**Sample Output 13**

    _ _ *

**Sample Input 14**

    R R R L 

**Sample Output 14**

    _ _ *

**Sample Input 15**

    R R R R 

**Sample Output 15**

    _ * _

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
