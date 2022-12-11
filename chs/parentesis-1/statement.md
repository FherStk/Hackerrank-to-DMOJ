Els parèntesis permeten definir l'ordre de les operacions en una
expressió.

Per exemple: `3 * ( 2 + 4 )` és distint a `( 3 * 2 ) + 4`

Els parèntesis han d'estar ben emparellats: un pàrentesi que s'obre s'ha
de tancar, i no es pot tancar un parèntesi si no s'ha obert abans.

Volem fer un programa que ens indiqui si hi ha algun error
d'emparellament de parèntesis en una expressió. El programa informarà
de:

  - Cada parèntesi tancat que no s'hagi obert prèviament, indicant la
    posició d'aquest parèntesi

  - La quantitat de parèntesis oberts que no s'hagin tancat

**Input Format**

L'entrada consisteix en una expressió. Els elements de l'expressió estan
separats per espais en blanc.

L'expressió finalitza amb la paraula `END`.

**Constraints**

\-

**Output Format**

S'imprimirà:

  - `ERROR: parentesi {posicio} mal tancat` per cada parèntesi mal
    tancat, on `{posicio}` és la posició d'aquest parèntesi

  - `ERROR: falta tancar {quantitat} parentesis` si hi ha parèntesis per
    tancar, on `{quantitat}` és la quantitat de parèntesis que falta
    tancar

Si els parèntesis estan ben emparellats, no s'ha d'imprimir res.

**Suggerència per a la solució**

Un possible solució al problema consisteix en:

  - Crear tres comptadors:
      - un per als parèntesis `oberts`
      - un per als `tancats`
      - un per al `total` de parèntesis (oberts i tancats)
  - Aleshores, es van llegint una a una les paraules de l'expressió.
      - Si la paraula llegida es un parèntesi obert `(`
          - es suma 1 al comptador de parèntesis `oberts`
          - també es suma 1 al `total` de parèntesis.
      - Si es llegeix un parèntesi tancat `)`
          - es suma 1 al de `tancats`
          - es suma 1 al de `total`
          - A més a més, mirem si el comptador de `tancats` és major al
            d'`oberts`
              - si és així, és que hi ha un error de parèntesi mal
                tancat. Imprimim l'error, i restem 1 al comptador de
                `tancats`
  - Un cop s'ha acabat de llegir tota l'expressió, s'haurien d'haver
    comptat el mateix número d'`oberts` que de `tancats`. Si no és així,
    és que falten parèntesis per tancar.

**Sample Input 0**

    ( 2 + 1 ) * 4     END

**Explanation 0**

Els parèntesis estan ben emparellats

**Sample Input 1**

    ( ( 2 + 1 ) * 4 )    END

**Explanation 1**

Els parèntesis estan ben emparellats

**Sample Input 2**

    2 + 1 ) * 4     END

**Sample Output 2**

    ERROR: parentesi 1 mal tancat

**Sample Input 3**

    ( 2 + 1 ) * 4 )     END

**Sample Output 3**

    ERROR: parentesi 3 mal tancat

**Sample Input 4**

    2 + 1 ) * 4 )     END

**Sample Output 4**

    ERROR: parentesi 1 mal tancat
    ERROR: parentesi 2 mal tancat

**Sample Input 5**

    ( 2 + 1 ) * 4 )     END

**Sample Output 5**

    ERROR: parentesi 3 mal tancat

**Sample Input 6**

    ( 2 + 2 ) * 3 ) + ( 3 + 2 ) * 3 )        END

**Sample Output 6**

    ERROR: parentesi 3 mal tancat
    ERROR: parentesi 6 mal tancat

**Sample Input 7**

    ( 2 + 1 * 4     END

**Sample Output 7**

    ERROR: falta tancar 1 parentesis

**Sample Input 8**

    ( 2 + ( 1 * 4     END

**Sample Output 8**

    ERROR: falta tancar 2 parentesis

**Sample Input 9**

    ( 2 + ( 1 + ( 3 * 4 )     END

**Sample Output 9**

    ERROR: falta tancar 2 parentesis

**Sample Input 10**

    ( 2 * ( 2 * ( 2 - 2 ) * ( 2 - 2 )   END

**Sample Output 10**

    ERROR: falta tancar 2 parentesis

**Sample Input 11**

    2 - ( 2 * 2 ) + ( 2 - 2      END

**Sample Output 11**

    ERROR: falta tancar 1 parentesis

**Sample Input 12**

    2 - ( 2 * 2 ) ) * ( 2 + 2     END

**Sample Output 12**

    ERROR: parentesi 3 mal tancat
    ERROR: falta tancar 1 parentesis

**Sample Input 13**

    2 * 2 ) + ( 2 - 2       END

**Sample Output 13**

    ERROR: parentesi 1 mal tancat
    ERROR: falta tancar 1 parentesis

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
