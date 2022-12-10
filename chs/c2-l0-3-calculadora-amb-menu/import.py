
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c2-l0-3-calculadora-amb-menu"
p.name="[d71d4] Calculadora amb menú #if #switch"
p.summary="Calculadora amb menú"
p.description='''Realitza un programa que soliciti dos nombres i mostri per pantalla el
següent menú:

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:

L'usuari escullirà una opció i el programa finalitzarà mostrant el
resultat per pantalla.

**Input Format**

L'entrada consta de 3 nombres:

  - Els dos primers  i  son els operands.

  - El tercer nombre  és l'opció del menú seleccionada

**Constraints**

Totes les operacions són enteres i no hi ha cap divisor que sigui 0.

**Output Format**

S'imprimirà el resultat de l'operació

**Sample Input 0**

    1 1     1

**Sample Output 0**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    2

**Sample Input 1**

    1 1     2

**Sample Output 1**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    0

**Sample Input 2**

    1 1     3

**Sample Output 2**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    1

**Sample Input 3**

    1 1     4

**Sample Output 3**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    1

**Sample Input 4**

    2 2     1

**Sample Output 4**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    4

**Sample Input 5**

    2 3     2

**Sample Output 5**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    -1

**Sample Input 6**

    2 5     3

**Sample Output 6**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    10

**Sample Input 7**

    10 5     4

**Sample Output 7**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    2

**Sample Input 8**

    3456 678     3

**Sample Output 8**

    MENU:
    1.-SUMAR
    2.-RESTAR
    3.-MULTIPLICAR
    4.-DIVIDIR
    Esculli una opcio:
    2343168
'''
p.is_public=True
p.date=timezone.now()
p.save()
