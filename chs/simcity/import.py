
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="simcity"
p.name="Simcity #arrays"
p.summary="Simcity"
p.description='''Los **Tilemaps** son una técnica popular en el desarrollo de juegos 2D,
que consiste en construir el mundo del juego a partir de pequeñas
imagenes regulares llamadas *tiles*.

Estamos desarrollando un juego de simulación de ciudades isométrico. Ya
tenemos listo el desarrollo de las carreteras. El mapa del juego está
representado internamente por una matriz de caracteres. Cada caracter
corresponde a un *tile* del mapa. Los tiles donde hay carretera
corresponden al caracter , y en los que hay hierba, el caracter 

Por ejemplo el siguiente mapa se representa con la siguiente matriz:

![image](1612872676-4ec549f4b2-tilemapex.png)

Para hacer más atractivo el juego queremos añadir los semáforos en las
intersecciones. Emepezaremos contando el número de semáforos que serán
necesarios.

Necesitaremos 3 semáforos en aquellas intersecciones donde se crucen 3
carreteras, y 4 en los cruces de 4 carreteras:

![image](1612869695-4137da2748-iso1.png)

**Input Format**

En primer lugar, los números  y  indican el ancho y alto del mapa,
respectivamente.

A continuación vienen los x *tiles* del mapa ( ). Los *tiles*
están separados por espacios en blanco y saltos de línea.

**Constraints**

\-

**Output Format**

Un entero indicando la cantidad de semáforos necesaria

**Sample Input 0**

    5 5
    . . . . .
    . . # . .
    . # # # .
    . . # . .
    . . . . .

**Sample Output 0**



**Explanation 0**

![image](1612870272-b3cc3fed74-isotest1.png)

**Sample Input 1**

    4 5
    . . . .
    . . # .
    . # # .
    . . # .
    . . . .

**Sample Output 1**



**Explanation 1**

![image](1612870439-faf61d0ae7-isotest2.png)

**Sample Input 2**

    7 4
    . . . . . . .
    . # # # . # .
    . # . # # # .
    . . . . . . .

**Sample Output 2**



**Explanation 2**

![image](1612870793-3a1cd41e84-isotest3.png)

**Sample Input 3**

    6 3
    . # . # . #
    # # # # # #
    . . . # . .

**Sample Output 3**



**Explanation 3**

![image](1612871080-7dfa0f4797-isotest4.png)

**Sample Input 4**

    7 4
    . . # . . . .
    # # # # # # #
    . . . # . # .
    . . . # . # .

**Sample Output 4**



**Sample Input 5**

    8 5
    . # . # . . # .
    # # # # . . # #
    . # . # . . # .
    . # # # # # # .
    . . # . . # . .

**Sample Output 5**



**Sample Input 6**

    11 8
    # . . # . . . # . . #
    # . . # # # # # . . #
    # # . # . . . # # # #
    . # # # . . # # . . #
    . . . # . . # . . . #
    . # # # # # # # # # #
    # # . # . . # . . # .
    # . . # # # # # # # .

**Sample Output 6**



**Sample Input 7**

    4 4
    . . # .
    . . # .
    # # # #
    # . # .

**Sample Output 7**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
