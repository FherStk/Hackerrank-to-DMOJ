Els cotxes autònoms ha de prendre decisions sobre la conducció a partir
del les dades que perceben els seus sensors de l'entorn.

![image](1557227574-8acd780630-path3911-4.png)

El nostre cotxe elèctric ha de decidir si pot continuar la marxa en
funció de les dades que li arriben del sensors. Aquestes dades són:

  - Estat del semàfor: r = vermell, g = verd, o = àmbar
  - Vianants creuant el carrer: true, false
  - Agent de circulació: 0 = no hi ha agent, 1 = ens dona pas, 2 = ens
    fa stop

La decisió de continuar o no, en base a les combinacions de les dades
del sensor es reflecteix en aquesta taula:

    semafor   r r r r r r g g g g g g o o o o o o
    vianants  f f f t t t f f f t t t f f f t t t
    agent     0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2    
    ---------------------------------------------
    creuar    f t f f f f t t f f f f t t f f f f

**Input Format**

En primer lloc l'estat del semàfor S, després la presència de vianants
V, finalment l'estat de l'agent de circulació A.

**Constraints**

S = { r | g | b}

V = { true | false }

A = { 0 | 1 | 2 }

**Output Format**

S'imprimirà "CONTINUAR" o "NO CONTINUAR"

**Sample Input 0**

    r false 0

**Sample Output 0**

    NO CONTINUAR

**Sample Input 1**

    r false 1

**Sample Output 1**

    CONTINUAR

**Sample Input 2**

    r false 2

**Sample Output 2**

    NO CONTINUAR

**Sample Input 3**

    r true 0

**Sample Output 3**

    NO CONTINUAR

**Sample Input 4**

    r true 1

**Sample Output 4**

    NO CONTINUAR

**Sample Input 5**

    r true 2

**Sample Output 5**

    NO CONTINUAR

**Sample Input 6**

    g false 0

**Sample Output 6**

    CONTINUAR

**Sample Input 7**

    g false 1

**Sample Output 7**

    CONTINUAR

**Sample Input 8**

    g false 2

**Sample Output 8**

    NO CONTINUAR

**Sample Input 9**

    g true 0

**Sample Output 9**

    NO CONTINUAR

**Sample Input 10**

    g true 1

**Sample Output 10**

    NO CONTINUAR

**Sample Input 11**

    g true 2

**Sample Output 11**

    NO CONTINUAR

**Sample Input 12**

    o false 0

**Sample Output 12**

    CONTINUAR

**Sample Input 13**

    o false 1

**Sample Output 13**

    CONTINUAR

**Sample Input 14**

    o false 2

**Sample Output 14**

    NO CONTINUAR

**Sample Input 15**

    o true 0

**Sample Output 15**

    NO CONTINUAR

**Sample Input 16**

    o true 1

**Sample Output 16**

    NO CONTINUAR

**Sample Input 17**

    o true 2

**Sample Output 17**

    NO CONTINUAR

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
