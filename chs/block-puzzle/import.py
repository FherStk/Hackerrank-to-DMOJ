
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="block-puzzle"
p.name="Block Puzzle #array"
p.summary="Block Puzzle"
p.description='''![image](1613466953-600b40fd49-bp.png)

En el juego Block Puzzle, el jugador va colocando unas piezas en el
tablero completando filas o columnas. Las piezas no se pueden
superponer.

Dado un tablero con las fichas que ya estaban colocadas, y otro tablero
con la ficha que desea colocar el jugador, indica si la ficha se puede
colocar en esa posición.

![image](1613467406-5443f7c755-blokpuzzle0.png)

**Input Format**

Los dos primeros números  y  indican el alto y ancho del tablero.

A continuación vienen las x casillas del tablero ( significa que la
casilla está ocupada y  que está libre).

A continación viene otro tablero de x casillas, con la ficha que trata
de poner el juagdor ( indica las casillas que ocupa la ficha).

**Constraints**

\-

**Output Format**

Se imprimirá  si la ficha se puede colocar en esa posición, y
 en caso contrario

**Sample Input 0**

    4 5
    
    1 0 0 0 0
    1 0 0 0 0
    1 0 0 1 1
    0 1 1 1 1
    
    0 0 1 1 0
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 0 0

**Sample Output 0**

    true

**Explanation 0**

![image](1613466939-b5689eb242-blokpuzzle.png)

**Sample Input 1**

    4 3
    
    1 1 0
    1 1 0
    0 0 0
    1 1 1
    
    0 0 0
    0 0 0
    0 1 1
    0 1 1

**Sample Output 1**

    false

**Explanation 1**

![image](1613468138-31f2165a34-blokpuzzle2.png)

**Sample Input 2**

    5 5
    
    0 1 1 0 1
    0 1 0 0 1
    0 1 0 0 1
    0 0 0 1 1
    0 0 0 1 1
    
    0 0 0 0 0
    0 0 0 0 0
    1 1 1 0 0
    1 1 1 0 0
    1 1 1 0 0

**Sample Output 2**

    false

**Sample Input 3**

    2 3
    
    0 1 1
    0 0 1
    
    1 0 0
    1 1 0

**Sample Output 3**

    true

**Sample Input 4**

    4 6
    
    1 1 1 1 0 1
    1 1 1 0 0 1
    1 1 1 1 0 1
    0 0 0 0 0 1
    
    0 0 0 0 1 0
    0 0 0 1 1 0
    0 0 0 0 1 0
    0 0 0 0 0 0

**Sample Output 4**

    true

**Explanation 4**

true
'''
p.is_public=True
p.date=timezone.now()
p.save()
