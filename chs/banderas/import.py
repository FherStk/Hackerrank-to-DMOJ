
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="banderas"
p.name="[C3-L3-2] Banderes #for"
p.summary="Banderes"
p.description='''Donat un tipus de bandera i un tamany, dibuixar una bandera d'aquest
tamany.

Tipus de banderes:

    Bandera 1
    Per sota de la diagonal ~, la resta *
    
    ******
    ~*****
    ~~****
    ~~~***
    ~~~~**
    ~~~~~*
    
    
    Bandera 2
    La meitat superior *, la meitat inferior -
    
    ******
    ******
    ******
    ~~~~~~
    ~~~~~~
    ~~~~~~
    
    
    Bandera 3
    La meitat dreta *, la meitat esquerra -
    
    ***~~~
    ***~~~
    ***~~~
    ***~~~
    ***~~~
    ***~~~
    
    
    Bandera 4
    La diagonal *, la resta ~
    
    *~~~~~
    ~*~~~~
    ~~*~~~
    ~~~*~~
    ~~~~*~
    ~~~~~*
    
    
    Bandera 5
    Primera línia *, la següent ~, successivament
    
    ******
    ~~~~~~
    ******
    ~~~~~~
    ******
    ~~~~~~
    
    
    Bandera 6
    Primer terç horitzontal *, segon terç ~, tercer *
    
    ******
    ******
    ~~~~~~
    ~~~~~~
    ******
    ******
    
    
    Bandera 7
    Primer terç vertical ~, segon terç *, tercer ~
    
    ~~**~~
    ~~**~~
    ~~**~~
    ~~**~~
    ~~**~~
    ~~**~~
    
    
    Bandera 8
    Primera columna *, la següent ~, successivament
    
    *~*~*~
    *~*~*~
    *~*~*~
    *~*~*~
    *~*~*~
    *~*~*~

**Input Format**

Un enter  indicant el tipus de bandera, i un enter  indicant el tamany.

**Constraints**

1 \<= N \<= 100

N%2 == 0

N%3 == 0

1\<= T \<= 8

**Output Format**

La bandera corresponent, del tamany indicat.

**Sample Input 0**

    1 6

**Sample Output 0**

    ******
    ~*****
    ~~****
    ~~~***
    ~~~~**
    ~~~~~*

**Sample Input 1**

    1 12

**Sample Output 1**

    ************
    ~***********
    ~~**********
    ~~~*********
    ~~~~********
    ~~~~~*******
    ~~~~~~******
    ~~~~~~~*****
    ~~~~~~~~****
    ~~~~~~~~~***
    ~~~~~~~~~~**
    ~~~~~~~~~~~*

**Sample Input 2**

    1 18

**Sample Output 2**

    ******************
    ~*****************
    ~~****************
    ~~~***************
    ~~~~**************
    ~~~~~*************
    ~~~~~~************
    ~~~~~~~***********
    ~~~~~~~~**********
    ~~~~~~~~~*********
    ~~~~~~~~~~********
    ~~~~~~~~~~~*******
    ~~~~~~~~~~~~******
    ~~~~~~~~~~~~~*****
    ~~~~~~~~~~~~~~****
    ~~~~~~~~~~~~~~~***
    ~~~~~~~~~~~~~~~~**
    ~~~~~~~~~~~~~~~~~*

**Sample Input 3**

    1 24

**Sample Output 3**

    ************************
    ~***********************
    ~~**********************
    ~~~*********************
    ~~~~********************
    ~~~~~*******************
    ~~~~~~******************
    ~~~~~~~*****************
    ~~~~~~~~****************
    ~~~~~~~~~***************
    ~~~~~~~~~~**************
    ~~~~~~~~~~~*************
    ~~~~~~~~~~~~************
    ~~~~~~~~~~~~~***********
    ~~~~~~~~~~~~~~**********
    ~~~~~~~~~~~~~~~*********
    ~~~~~~~~~~~~~~~~********
    ~~~~~~~~~~~~~~~~~*******
    ~~~~~~~~~~~~~~~~~~******
    ~~~~~~~~~~~~~~~~~~~*****
    ~~~~~~~~~~~~~~~~~~~~****
    ~~~~~~~~~~~~~~~~~~~~~***
    ~~~~~~~~~~~~~~~~~~~~~~**
    ~~~~~~~~~~~~~~~~~~~~~~~*

**Sample Input 4**

    2 12

**Sample Output 4**

    ************
    ************
    ************
    ************
    ************
    ************
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~

**Sample Input 5**

    2 18

**Sample Output 5**

    ******************
    ******************
    ******************
    ******************
    ******************
    ******************
    ******************
    ******************
    ******************
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~

**Sample Input 6**

    2 24

**Sample Output 6**

    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~

**Sample Input 7**

    3 12

**Sample Output 7**

    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~
    ******~~~~~~

**Sample Input 8**

    3 18

**Sample Output 8**

    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~
    *********~~~~~~~~~

**Sample Input 9**

    3 24

**Sample Output 9**

    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~
    ************~~~~~~~~~~~~

**Sample Input 10**

    4 12

**Sample Output 10**

    *~~~~~~~~~~~
    ~*~~~~~~~~~~
    ~~*~~~~~~~~~
    ~~~*~~~~~~~~
    ~~~~*~~~~~~~
    ~~~~~*~~~~~~
    ~~~~~~*~~~~~
    ~~~~~~~*~~~~
    ~~~~~~~~*~~~
    ~~~~~~~~~*~~
    ~~~~~~~~~~*~
    ~~~~~~~~~~~*

**Sample Input 11**

    4 18

**Sample Output 11**

    *~~~~~~~~~~~~~~~~~
    ~*~~~~~~~~~~~~~~~~
    ~~*~~~~~~~~~~~~~~~
    ~~~*~~~~~~~~~~~~~~
    ~~~~*~~~~~~~~~~~~~
    ~~~~~*~~~~~~~~~~~~
    ~~~~~~*~~~~~~~~~~~
    ~~~~~~~*~~~~~~~~~~
    ~~~~~~~~*~~~~~~~~~
    ~~~~~~~~~*~~~~~~~~
    ~~~~~~~~~~*~~~~~~~
    ~~~~~~~~~~~*~~~~~~
    ~~~~~~~~~~~~*~~~~~
    ~~~~~~~~~~~~~*~~~~
    ~~~~~~~~~~~~~~*~~~
    ~~~~~~~~~~~~~~~*~~
    ~~~~~~~~~~~~~~~~*~
    ~~~~~~~~~~~~~~~~~*

**Sample Input 12**

    4 24

**Sample Output 12**

    *~~~~~~~~~~~~~~~~~~~~~~~
    ~*~~~~~~~~~~~~~~~~~~~~~~
    ~~*~~~~~~~~~~~~~~~~~~~~~
    ~~~*~~~~~~~~~~~~~~~~~~~~
    ~~~~*~~~~~~~~~~~~~~~~~~~
    ~~~~~*~~~~~~~~~~~~~~~~~~
    ~~~~~~*~~~~~~~~~~~~~~~~~
    ~~~~~~~*~~~~~~~~~~~~~~~~
    ~~~~~~~~*~~~~~~~~~~~~~~~
    ~~~~~~~~~*~~~~~~~~~~~~~~
    ~~~~~~~~~~*~~~~~~~~~~~~~
    ~~~~~~~~~~~*~~~~~~~~~~~~
    ~~~~~~~~~~~~*~~~~~~~~~~~
    ~~~~~~~~~~~~~*~~~~~~~~~~
    ~~~~~~~~~~~~~~*~~~~~~~~~
    ~~~~~~~~~~~~~~~*~~~~~~~~
    ~~~~~~~~~~~~~~~~*~~~~~~~
    ~~~~~~~~~~~~~~~~~*~~~~~~
    ~~~~~~~~~~~~~~~~~~*~~~~~
    ~~~~~~~~~~~~~~~~~~~*~~~~
    ~~~~~~~~~~~~~~~~~~~~*~~~
    ~~~~~~~~~~~~~~~~~~~~~*~~
    ~~~~~~~~~~~~~~~~~~~~~~*~
    ~~~~~~~~~~~~~~~~~~~~~~~*

**Sample Input 13**

    5 12

**Sample Output 13**

    ************
    ~~~~~~~~~~~~
    ************
    ~~~~~~~~~~~~
    ************
    ~~~~~~~~~~~~
    ************
    ~~~~~~~~~~~~
    ************
    ~~~~~~~~~~~~
    ************
    ~~~~~~~~~~~~

**Sample Input 14**

    5 18

**Sample Output 14**

    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~
    ******************
    ~~~~~~~~~~~~~~~~~~

**Sample Input 15**

    5 24

**Sample Output 15**

    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~

**Sample Input 16**

    6 12

**Sample Output 16**

    ************
    ************
    ************
    ************
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ~~~~~~~~~~~~
    ************
    ************
    ************
    ************

**Sample Input 17**

    6 18

**Sample Output 17**

    ******************
    ******************
    ******************
    ******************
    ******************
    ******************
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~
    ******************
    ******************
    ******************
    ******************
    ******************
    ******************

**Sample Input 18**

    6 24

**Sample Output 18**

    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************
    ************************

**Sample Input 19**

    7 12

**Sample Output 19**

    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~
    ~~~~****~~~~

**Sample Input 20**

    7 18

**Sample Output 20**

    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~
    ~~~~~~******~~~~~~

**Sample Input 21**

    7 24

**Sample Output 21**

    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~
    ~~~~~~~~********~~~~~~~~

**Sample Input 22**

    8 12

**Sample Output 22**

    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~
    *~*~*~*~*~*~

**Sample Input 23**

    8 18

**Sample Output 23**

    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~

**Sample Input 24**

    8 24

**Sample Output 24**

    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~
    *~*~*~*~*~*~*~*~*~*~*~*~

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
