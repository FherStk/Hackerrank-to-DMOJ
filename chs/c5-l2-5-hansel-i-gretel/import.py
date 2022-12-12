
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c5-l2-5-hansel-i-gre"
p.name="[C5-L2-5] Hansel i Gretel"
p.summary="Hansel i Gretel"
p.description='''Hänsel i Gretel són dos germans d'una família de llenyataires molt
pobra. La madrastra convenç el seu pare d'abandonar-los al bosc per no
haver de repartir amb ells el menjar familiar però ells poden tornar a
casa seguint un rastre de pedretes que havien deixat al camí. Els nens
repeteixen l'operació i aquest cop el rastre està fet d'engrunes de pa,
que es mengen els ocells i per tant els nens es perden...

Ajuda a Hansel i Gretel a fer el camí de tornada a casa\!

**Input Format**

La entrada consisteix en un mapa del bosc on es marca la casa, les
engrunes de pa i el lloc on s'han perdut Hansel i Gretel.

La casa està marcada amb la lletra 'A', les engrunes amb un punt '.', i
Hansel i Gretel amb una 'H'.

El mapa està envoltat d'un marc amb coixinets '\#'.

**Constraints**

El camí de punts només avança a en direcció Nord, Sud, Est o Oest. Per a
cada punt només hi ha una direcció possible.

Es considera que Hansel i Gretel han arribat a la casa quan la lletra
'H', està tocant la lletra 'A'.

**Output Format**

S'imprimirà el mapa del bosc a cada passa que hagin donat Hansel i
Gretel recuperant les engrunes de pa.

**Sample Input 0**

    7
    #########
    #       #
    # A..   #
    #   .   #
    #   ..H #
    #       #
    #########

**Sample Output 0**

    #########
    #       #
    # A..   #
    #   .   #
    #   ..H #
    #       #
    #########
    #########
    #       #
    # A..   #
    #   .   #
    #   .H  #
    #       #
    #########
    #########
    #       #
    # A..   #
    #   .   #
    #   H   #
    #       #
    #########
    #########
    #       #
    # A..   #
    #   H   #
    #       #
    #       #
    #########
    #########
    #       #
    # A.H   #
    #       #
    #       #
    #       #
    #########
    #########
    #       #
    # AH    #
    #       #
    #       #
    #       #
    #########

**Sample Input 1**

    5
    ######
    #A.. #
    #  . #
    #H.. #
    ######

**Sample Output 1**

    ######
    #A.. #
    #  . #
    #H.. #
    ######
    ######
    #A.. #
    #  . #
    # H. #
    ######
    ######
    #A.. #
    #  . #
    #  H #
    ######
    ######
    #A.. #
    #  H #
    #    #
    ######
    ######
    #A.H #
    #    #
    #    #
    ######
    ######
    #AH  #
    #    #
    #    #
    ######

**Sample Input 2**

    7
    #########
    # A     #
    # ...   #
    #   .   #
    #   ... #
    #     H #
    #########

**Sample Output 2**

    #########
    # A     #
    # ...   #
    #   .   #
    #   ... #
    #     H #
    #########
    #########
    # A     #
    # ...   #
    #   .   #
    #   ..H #
    #       #
    #########
    #########
    # A     #
    # ...   #
    #   .   #
    #   .H  #
    #       #
    #########
    #########
    # A     #
    # ...   #
    #   .   #
    #   H   #
    #       #
    #########
    #########
    # A     #
    # ...   #
    #   H   #
    #       #
    #       #
    #########
    #########
    # A     #
    # ..H   #
    #       #
    #       #
    #       #
    #########
    #########
    # A     #
    # .H    #
    #       #
    #       #
    #       #
    #########
    #########
    # A     #
    # H     #
    #       #
    #       #
    #       #
    #########

**Sample Input 3**

    8
    ##########
    #  ....H #
    #  .     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########

**Sample Output 3**

    ##########
    #  ....H #
    #  .     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #  ...H  #
    #  .     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #  ..H   #
    #  .     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #  .H    #
    #  .     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #  H     #
    #  .     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #  H     #
    #  ......#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #  H.....#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #   H....#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #    H...#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #     H..#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #      H.#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #       H#
    #A      .#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #        #
    #A      H#
    #.      .#
    #........#
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.      H#
    #........#
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #.......H#
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #......H #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #.....H  #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #....H   #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #...H    #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #..H     #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #.H      #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #.       #
    #H       #
    ##########
    ##########
    #        #
    #        #
    #        #
    #A       #
    #H       #
    #        #
    ##########

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
