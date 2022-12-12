
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="c5-l3-2-diccionari"
p.name="[C5-L3-2] Diccionari"
p.summary="Diccionari"
p.description='''Quan programem jocs que utilitzen paraules (com l'Scrabble, Sopa de
lletres, Penjat, ... ), ens pot ser molt útil tenir una llista amb totes
les possibles paraules.

A Linux, tenim l'arxiu /usr/share/dict amb una completa llista de
paraules, i podríem progamar un mètode per a cercar-hi una paraula.

També disposem del recurs de la metaprogramació, que consisteix en
programes que escriuen altres programes. Fent ús d'aquesta eina, podem
fer un programa que generi un programa en Java que contingui un array
amb les paraules del diccionari.

**Input Format**

Una llista de paraules, separades per salts de línia.

La llista de paraules acaba amb '**END**'

**Constraints**

No hi ha restriccions significatives.

**Output Format**

Es generarà una programa Java amb una classe anomenada "Dictionari", que
inicialitzi un array d'strings amb les paraules, anomenat "words".

**Sample Input 0**

    una
    llista
    de
    paraules
    __END__

**Sample Output 0**

    class Dictionari {
        String[] words = {
            "una",
            "llista",
            "de",
            "paraules"
        };
    }

**Sample Input 1**

    festival
    triangle
    municipi
    batalla
    voleibol
    __END__

**Sample Output 1**

    class Dictionari {
        String[] words = {
            "festival",
            "triangle",
            "municipi",
            "batalla",
            "voleibol"
        };
    }

**Sample Input 2**

    metaprogramming
    __END__

**Sample Output 2**

    class Dictionari {
        String[] words = {
            "metaprogramming"
        };
    }

**Sample Input 3**

    metaprogramming
    rocks
    __END__

**Sample Output 3**

    class Dictionari {
        String[] words = {
            "metaprogramming",
            "rocks"
        };
    }

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
