
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="afe43-amaga-les-columnes"
p.name="[afe43] Amaga les columnes"
p.summary="Amaga les columnes"
p.description='''![image](1579623863-f2d38217d1-excel.png)

Els programes de Full de Càlcul solen tenir la funció d'amagar columnes.

Tractem d'implementar aquesta funcionalitat...

**Input Format**

L'entrada consta en primer lloc d'un Full de càlcul:

  - Els dos primers números
    i
    indiquen la quantitat de files i columnes
  - A continuació ve la taula amb les dades (Les files separades per un
    salt de línia i les columnes separades per espai en blanc)

En segon lloc venen les columnes que cal ocultar:

  - S'inidica el número
    de columnes que s'han d'ocultar
  - Després venen els índexs d'aquestes columnes (començant per 1)

**Constraints**

\-

**Output Format**

S'imprimirà la taula, sense mostrar les columnes indicades. Tots els
camps de la taula han d'ocupar **10 espais i aliniats a l'esquerra**

**Sample Input 0**

    4 6
    Nombre  Apellidos UF1 UF2 UF3 FINAL
    Juan    Perez     5   6   6   6
    Pepe    Alvarez   1   2   1   1
    Eloy    Lopez     7   8   7   7
    
    3
    3 4 5

**Sample Output 0**



**Sample Input 1**

    4 6
    Nombre  Apellidos UF1 UF2 UF3 FINAL
    Juan    Perez     5   6   6   6
    Pepe    Alvarez   1   2   1   1
    Eloy    Lopez     7   8   7   7
    
    1
    2

**Sample Output 1**



**Sample Input 2**

    6 3
    Columna1 Columna2 Columna3
    Campo11  Campo12  Campo13
    Campo21  Campo22  Campo23
    Campo31  Campo32  Campo33
    Campo41  Campo42  Campo43
    Campo51  Campo52  Campo53
    
    2
    2 3

**Sample Output 2**



**Sample Input 3**

    6 3
    Columna1 Columna2 Columna3
    Campo11  Campo12  Campo13
    Campo21  Campo22  Campo23
    Campo31  Campo32  Campo33
    Campo41  Campo42  Campo43
    Campo51  Campo52  Campo53
    
    2
    1 3

**Sample Output 3**

    Columna2  
    Campo12   
    Campo22   
    Campo32   
    Campo42   
    Campo52
'''
p.is_public=True
p.date=timezone.now()
p.save()
