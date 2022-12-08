Donades tres dates, digues si la segona és posterior a la primera i
anterior a la tercera.

**Input Format**

L'entrada consisteix en tres dates en format `dd / mm / yyyy`.

Les tres dates són distintes.

**Constraints**

\-

**Output Format**

S'imprimirà `true` si la segona data és posterior a la primera i
anterior a la tercera, i `false` en cas contrari.

**Suggerència per a la solució**

Cal llegir el dia, mes i any de cada data amb `nextInt()`. S'hauràn de
descartar les barres `/` amb `next()`.

Una possible idea per a la solució és presuposar que la segona data està
enmig, i després veure si es compleix alguna condició que impliqui que
realment no està enmig.

    // suposem que està enmig
    boolean enmig = true;
    
    // mirem si hi ha alguna condició
    // que contradigui la presuposició incial
    if (any1 > any2) {
        enmig = false;
    } else if (any2 > any3) {
        enmig = false;
    }
    // resta de condicions
    
    // imprimim el resultat
    System.out.println(enmig);

**Sample Input 0**

    7 / 1 / 1999      17 / 10 / 2050      7 / 1 / 2020

**Sample Output 0**

    false

**Sample Input 1**

    7 / 1 / 1999      7 / 1 / 2020      7 / 1 / 2050

**Sample Output 1**

    true

**Sample Input 2**

    7 / 1 / 1999      7 / 10 / 2020      17 / 1 / 2020

**Sample Output 2**

    false

**Sample Input 3**

    7 / 1 / 1999      7 / 12 / 1999      7 / 1 / 2020

**Sample Output 3**

    true

**Sample Input 4**

    7 / 1 / 1999      17 / 1 / 2050      27 / 1 / 2020

**Sample Output 4**

    false

**Sample Input 5**

    7 / 1 / 1999      17 / 12 / 2020      17 / 1 / 1999

**Sample Output 5**

    false

**Sample Input 6**

    7 / 1 / 1999      27 / 10 / 1999      17 / 10 / 2020

**Sample Output 6**

    true

**Sample Input 7**

    7 / 1 / 2020      7 / 1 / 1999      17 / 1 / 2020

**Sample Output 7**

    false

**Sample Input 8**

    7 / 1 / 2020      17 / 1 / 2020      7 / 1 / 2050

**Sample Output 8**

    true

**Sample Input 9**

    7 / 1 / 2020      27 / 1 / 2050      17 / 10 / 1999

**Sample Output 9**

    false

**Sample Input 10**

    7 / 1 / 2050      7 / 12 / 2050      27 / 12 / 2050

**Sample Output 10**

    true

**Sample Input 11**

    7 / 1 / 2050      27 / 10 / 2050      17 / 10 / 2020

**Sample Output 11**

    false

**Sample Input 12**

    7 / 10 / 2020      7 / 12 / 2020      7 / 1 / 2050 

**Sample Output 12**

    true

**Sample Input 13**

    7 / 10 / 2050      17 / 10 / 2020      7 / 1 / 2050 

**Sample Output 13**

    false

**Sample Input 14**

    7 / 12 / 2020      17 / 10 / 2050      7 / 12 / 2050 

**Sample Output 14**

    true

**Sample Input 15**

    17 / 1 / 1999      27 / 10 / 2050      7 / 1 / 1999 

**Sample Output 15**

    false

**Sample Input 16**

    17 / 10 / 1999      7 / 1 / 2020      7 / 1 / 2050 

**Sample Output 16**

    true

**Sample Input 17**

    17 / 10 / 2020      27 / 1 / 1999      17 / 10 / 1999 

**Sample Output 17**

    false

**Sample Input 18**

    17 / 10 / 2050      27 / 10 / 2050      17 / 12 / 2050 

**Sample Output 18**

    true

**Sample Input 19**

    17 / 12 / 2020      7 / 12 / 2020      27 / 10 / 1999 

**Sample Output 19**

    false

**Sample Input 20**

    27 / 1 / 1999      7 / 1 / 2020      7 / 1 / 2050 

**Sample Output 20**

    true

**Sample Input 21**

    27 / 1 / 2020      7 / 12 / 2050      7 / 1 / 1999 

**Sample Output 21**

    false

**Sample Input 22**

    27 / 10 / 1999      7 / 1 / 2020      7 / 1 / 2050 

**Sample Output 22**

    true

**Sample Input 23**

    27 / 10 / 1999      27 / 10 / 2020      17 / 12 / 1999 

**Sample Output 23**

    false

**Sample Input 24**

    27 / 12 / 1999      7 / 1 / 2020      7 / 1 / 2050 

**Sample Output 24**

    true

**Sample Input 25**

    27 / 12 / 1999      27 / 10 / 2020      7 / 1 / 2020 

**Sample Output 25**

    false

**Sample Input 26**

    27 / 12 / 2020      7 / 1 / 2050      7 / 10 / 2050 

**Sample Output 26**

    true

**Sample Input 27**

    27 / 12 / 2020      27 / 10 / 2050      7 / 12 / 2020 

**Sample Output 27**

    false
