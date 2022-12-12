
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="el-club-de-la-lucha"
p.name="El club de la lucha #arrays"
p.summary="El club de la lucha"
p.description='''En el club de la lucha, los combatientes luchan hasta agotar sus
fuerzas.

A partir de los nombres de todos los miembros del club y sus fuerzas,
determina quien quedará en pie después de una serie de combates.

En cada combate, los dos luchadores pierden la misma cantidad de fuerza
hasta que uno queda completamente agotado.

**Input Format**

El primer número  indica el número de luchadores. A continuación vienen
los  nombres de cada luchador (una palabra). A continuación vienen las 
fuerzas de cada luchador (un entero).

El siguiente número  indica la cantidad de combates. Por cada combate se
indican los nombres de cada luchador.

**Constraints**

\-

**Output Format**

Se imprimirán los nombres y las fuerzas de los luchadores que aun sigan
en pie, cada uno en una línea, y con el formato: 

**Sample Input 0**

    4
    Richard Tyler Angel Bob 
    20      10    30    15
    
    3
    Richard Tyler
    Angel Bob
    Richard Bob

**Sample Output 0**

    Richard: 10
    Angel: 15

**Sample Input 1**

    5
    AAA BBB CCC DDD EEE
    60  40  20  50  30
    
    5
    AAA CCC
    BBB DDD
    EEE BBB
    DDD AAA
    CCC EEE

**Sample Output 1**

    AAA: 30
    EEE: 30

**Sample Input 2**

    10
    A B C D E F G H I J
    5 6 3 5 4 9 9 8 2 1
    
    11
    A B
    C E
    F I
    J C
    G D
    H B
    I A
    F C
    I B
    J E
    F H

**Sample Output 2**

    G: 4

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
