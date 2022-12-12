
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c2-l1-2-lletres-scra"
p.name="[e3ecf] Lletres de l'Scrabble #if #switch"
p.summary="Lletres de l'Scrabble"
p.description='''![image](1571218848-eddd5026fa-captionit9103701852B81.jpg)

Donada una lletra, obté la seva puntuació d'Scrabble.

    Letter                             Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10

**Input Format**

Un caracter

**Constraints**

El caracter és una lletra de l'Scrabble

**Output Format**

La puntuació de la lletra

**Sample Input 0**



**Sample Output 0**



**Sample Input 1**



**Sample Output 1**



**Sample Input 2**



**Sample Output 2**



**Sample Input 3**



**Sample Output 3**



**Sample Input 4**



**Sample Output 4**



**Sample Input 5**



**Sample Output 5**



**Sample Input 6**



**Sample Output 6**



**Sample Input 7**



**Sample Output 7**



**Sample Input 8**



**Sample Output 8**



**Sample Input 9**



**Sample Output 9**



**Sample Input 10**



**Sample Output 10**



**Sample Input 11**



**Sample Output 11**



**Sample Input 12**



**Sample Output 12**



**Sample Input 13**



**Sample Output 13**



**Sample Input 14**



**Sample Output 14**



**Sample Input 15**



**Sample Output 15**



**Sample Input 16**



**Sample Output 16**



**Sample Input 17**



**Sample Output 17**



**Sample Input 18**



**Sample Output 18**



**Sample Input 19**



**Sample Output 19**



**Sample Input 20**



**Sample Output 20**



**Sample Input 21**



**Sample Output 21**



**Sample Input 22**



**Sample Output 22**



**Sample Input 23**



**Sample Output 23**



**Sample Input 24**



**Sample Output 24**



**Sample Input 25**



**Sample Output 25**



----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
