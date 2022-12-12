
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="street-fighter-1"
p.name="[C2-L2-5] Street Fighter #if"
p.summary="Street Fighter"
p.description='''En la majoria de jocs, per a modelar el comportament dels personatges
s'utilitza una **màquina d'estats**.

La màquina d'estats defineix les possibles accions que pot estar
realitzant un personatge, i els events que inicien les accions. Per
exemple, un jugador pot estar en estat "CAMINANT" i quan es produeix
l'event en què l'usuari "POLSA LA TECLA DE DISPAR", aleshores canvia
l'acció i passa a estar en estat "DISPARANT".

La cosa es complica una mica perquè hi ha estats als quals no es pot
arribar partint d'altres. Per exemple, hi ha jocs en els que el
personatge no pot disparar mentre esta saltant. En aquest cas no seria
possible la transició directa entre l'estat "SALTANT" i l'estat
"DISPARANT"·

Es demana implementar una màquina d'estats bàsica per a un personatge
del joc Street Fighter:

Els **estats** possibles d'un personatge són:

![image](1570555428-3edd8a3606-Untitleddrawing.png)

Els **events** que poden canviar l'estat d'un personatge són:

  - JOYSTICK\_UP: El jugador ha accionat el joystick cap amunt

  - JOYSTICK\_LEFT/RIGHT: El jugador ha accionat el joystick a esquerra
    o dreta

  - JOYSTICK\_CENTER: El jugador a deixat el joystick al centre

  - PUNCH\_KEY: El jugador a polsat el botó de cop de puny

  - KICK\_KEY: El jugador a polsat el botó de cop de peu

  - PUNCH\_END: L'acció de cop de puny ha acabat

  - KICK\_END: L'acció de cop de peu ha acabat

  - TOUCH\_FLOOR: El personatge ha tocat terra

El següent diagrama ilustra les transicions entre estats que provoquen
aquests events.

![image](1570555731-03e2925fea-streetfighter.png)

**Input Format**

L'entrada consta de dues paraules:

  - L'estat actual del personatge: {"IDLE", "WALK", "JUMP", "KICK",
    "PUNCH"}

  - L'event que ha ocorregut: {"JOYSTICK\_UP", "JOYSTICK\_LEFT/RIGHT",
    "JOYSTICK\_CENTER", "PUNCH\_KEY", "KICK\_KEY", "PUNCH\_END",
    "KICK\_END", "TOUCH\_FLOOR"}

**Constraints**

No hi ha

**Output Format**

S'imprimirà l'estat en el qual quedarà el personatge.

Si l'event ocorregut no modifica l'estat, es mostrarà el que tenia abans
de l'event.

**Sample Input 0**

    IDLE JOYSTICK_UP

**Sample Output 0**

    JUMPING

**Explanation 0**

El personatge es troba en estat "IDLE" i ocorre l'event "JOYSTICK\_UP".
El nou estat passa a ser "JUMPING"

**Sample Input 1**

    IDLE JOYSTICK_LEFT/RIGHT

**Sample Output 1**

    WALKING

**Explanation 1**

El personatge es troba en estat "IDLE" i ocorre l'event
"JOYSTICK\_LEFT/RIGHT". El nou estat passa a ser "WALKING"

**Sample Input 2**

    IDLE JOYSTICK_CENTER

**Sample Output 2**

    IDLE

**Explanation 2**

L'estat del personatge és "IDLE" i ocorre l'event "JOYSTICK\_CENTER".
Aquest event **no** modifica l'estat del personatge.

**Sample Input 3**

    IDLE PUNCH_KEY

**Sample Output 3**

    PUNCHING

**Sample Input 4**

    IDLE KICK_KEY

**Sample Output 4**

    KICKING

**Sample Input 5**

    IDLE PUNCH_END

**Sample Output 5**

    IDLE

**Sample Input 6**

    IDLE KICK_END

**Sample Output 6**

    IDLE

**Sample Input 7**

    IDLE TOUCH_FLOOR

**Sample Output 7**

    IDLE

**Sample Input 8**

    WALKING JOYSTICK_UP

**Sample Output 8**

    JUMPING

**Sample Input 9**

    WALKING JOYSTICK_LEFT/RIGHT

**Sample Output 9**

    WALKING

**Sample Input 10**

    WALKING JOYSTICK_CENTER

**Sample Output 10**

    IDLE

**Sample Input 11**

    WALKING PUNCH_KEY

**Sample Output 11**

    PUNCHING

**Sample Input 12**

    WALKING KICK_KEY

**Sample Output 12**

    KICKING

**Sample Input 13**

    WALKING PUNCH_END

**Sample Output 13**

    WALKING

**Sample Input 14**

    WALKING KICK_END

**Sample Output 14**

    WALKING

**Sample Input 15**

    WALKING TOUCH_FLOOR

**Sample Output 15**

    WALKING

**Sample Input 16**

    JUMPING JOYSTICK_UP

**Sample Output 16**

    JUMPING

**Sample Input 17**

    JUMPING JOYSTICK_LEFT/RIGHT

**Sample Output 17**

    JUMPING

**Sample Input 18**

    JUMPING JOYSTICK_CENTER

**Sample Output 18**

    JUMPING

**Sample Input 19**

    JUMPING PUNCH_KEY

**Sample Output 19**

    PUNCHING

**Sample Input 20**

    JUMPING KICK_KEY

**Sample Output 20**

    KICKING

**Sample Input 21**

    JUMPING PUNCH_END

**Sample Output 21**

    JUMPING

**Sample Input 22**

    JUMPING KICK_END

**Sample Output 22**

    JUMPING

**Sample Input 23**

    JUMPING TOUCH_FLOOR

**Sample Output 23**

    IDLE

**Sample Input 24**

    KICKING JOYSTICK_UP

**Sample Output 24**

    KICKING

**Sample Input 25**

    KICKING JOYSTICK_LEFT/RIGHT

**Sample Output 25**

    KICKING

**Sample Input 26**

    KICKING JOYSTICK_CENTER

**Sample Output 26**

    KICKING

**Sample Input 27**

    KICKING PUNCH_KEY

**Sample Output 27**

    KICKING

**Sample Input 28**

    KICKING KICK_KEY

**Sample Output 28**

    KICKING

**Sample Input 29**

    KICKING PUNCH_END

**Sample Output 29**

    KICKING

**Sample Input 30**

    KICKING KICK_END

**Sample Output 30**

    IDLE

**Sample Input 31**

    KICKING TOUCH_FLOOR

**Sample Output 31**

    KICKING

**Sample Input 32**

    PUNCHING JOYSTICK_UP

**Sample Output 32**

    PUNCHING

**Sample Input 33**

    PUNCHING JOYSTICK_LEFT/RIGHT

**Sample Output 33**

    PUNCHING

**Sample Input 34**

    PUNCHING JOYSTICK_CENTER

**Sample Output 34**

    PUNCHING

**Sample Input 35**

    PUNCHING PUNCH_KEY

**Sample Output 35**

    PUNCHING

**Sample Input 36**

    PUNCHING KICK_KEY

**Sample Output 36**

    PUNCHING

**Sample Input 37**

    PUNCHING PUNCH_END

**Sample Output 37**

    IDLE

**Sample Input 38**

    PUNCHING KICK_END

**Sample Output 38**

    PUNCHING

**Sample Input 39**

    PUNCHING TOUCH_FLOOR

**Sample Output 39**

    PUNCHING

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
