En les enquestes poden haver preguntes condicionades. Són preguntes que
només es fan si s'ha donat una determinada resposta en una pregunta
anterior.

En una enquesta sobre *frameworks* es pregunta als participants si en
coneixen algun, i en cas afirmatiu se'ls pregunta quin.

    Benvingut a l'enquesta.
    Coneixes algun framework?
    > no
    Gracies per contestar

    Benvingut a l'enquesta.
    Coneixes algun framework?
    > si
    Quin?
    > react
    S'ha registrat la resposta: react
    Gracies per contestar

**Input Format**

L'entrada té dues opcions:

  - un únic `no`

  - un `si` i una nova línia de text

**Constraints**

\-

**Output Format**

S'imprimirà l'enquesta en el format apuntat als casos de prova

**Sample Input 0**

``` 
no
```

**Sample Output 0**

    Benvingut a l'enquesta.
    Coneixes algun framework?
    Gracies per contestar

**Sample Input 1**

    si
    vue.js

**Sample Output 1**

    Benvingut a l'enquesta.
    Coneixes algun framework?
    Quin?
    S'ha registrat la resposta: vue.js
    Gracies per contestar

**Sample Input 2**

    si
    svelte

**Sample Output 2**

    Benvingut a l'enquesta.
    Coneixes algun framework?
    Quin?
    S'ha registrat la resposta: svelte
    Gracies per contestar

**Sample Input 3**

    si
    Spring

**Sample Output 3**

    Benvingut a l'enquesta.
    Coneixes algun framework?
    Quin?
    S'ha registrat la resposta: Spring
    Gracies per contestar

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
