
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c3-l0-7-passwd"
p.name="[b1c26] passwd #for"
p.summary="passwd"
p.description='''![image](1571914537-1def2cb3c0-Untitleddrawing1.png)

L'arxiu /etc/passwd emmagatzema els usuaris del sistema. Cada línia
conté la informació d'un usuari i té els següents camps:

  - Username

  - Encrypted password. *Tradicionalment, aquest camp contenia el
    password encriptat de l'usuari. Els sistemes Unix moderns, guarden
    els passwords encriptats en un arxiu separat (/etc/shadow) que només
    pot ser accedit per usuaris privilegiats*

  - User identification number (UID)

  - Group identification number (GID)

  - Full name

  - Home directory

  - Shell

Realitzarem un programa que permeti generar automàticament una sèrie
d'usuaris amb el format de l'ariux passwd. Les dades dels usuaris es
generaran d'aquesta forma1:

  - : serà la paraula 'user' seguit de l' de l'usuari

  -  : usarem una funció HASH sencilla per a generar un password a
    partir de l'UID. Després encryptarem el password generat amb
    l'algoritme MD5.

  - : es generarà de forma consecutiva a partir del 1001

  - : serà sempre 1000

  - : La paraula "Usuari" + espai en blanc + 

  - : /home/

  - : /bin/bash

**Encriptació del password**

El password serà un número que es generarà a partir de l'UID de
l'usuari, usant aquesta funció HASH:

    HASH(UID) = (UID << 29 ^ UID << 17) >>> 1

Un cop generat el password, l'encriptarem amb l'algoritme MD5 que
implementa el paquet java.security.MessageDigest:

    String encrypted = Base64.getEncoder().encodeToString(MessageDigest.getInstance("md5").digest((String.valueOf(password)).getBytes()));

\* la variable  és el número que s'ha generat a partir de l'UID

Finalment, a l'arxiu /etc/passwd **cal indicar quin és l'algoritme
utilitzat**. En el cas d'MD5 s'indica amb la marca  just davant del
password encryptat.

NOTES:

*(1) L'algoritme MD5 implementat a MessageDigest NO és compatible amb
l'algoritme que usa GNU/Linux*

*(2) L'algoritme MD5 no és segur, caldria utilitzar SHA-512*

*(3) Generar contrasenyes a partir de dades conegudes, com l'UID, no és
segur. Cal generar contrasenyes aleatòries.*

**Input Format**

L'entrada consta d'un nombre enter que indica la quantitat d'usuaris a
generar.

**Constraints**

\-

**Output Format**

S'imprimiràn les dades dels usuaris amb el format de la l'arxiu
/etc/passwd.

**Sample Input 0**



**Sample Output 0**

    user1001:==:1001:1000:Usuari 1001:/home/user1001:/bin/bash
    user1002:+o4AcNq3dxAK9c4g==:1002:1000:Usuari 1002:/home/user1002:/bin/bash
    user1003:==:1003:1000:Usuari 1003:/home/user1003:/bin/bash

**Sample Input 1**



**Sample Output 1**

    user1001:==:1001:1000:Usuari 1001:/home/user1001:/bin/bash
    user1002:+o4AcNq3dxAK9c4g==:1002:1000:Usuari 1002:/home/user1002:/bin/bash
    user1003:==:1003:1000:Usuari 1003:/home/user1003:/bin/bash
    user1004:==:1004:1000:Usuari 1004:/home/user1004:/bin/bash
    user1005:/HtOA==:1005:1000:Usuari 1005:/home/user1005:/bin/bash

**Sample Input 2**



**Sample Output 2**

    user1001:==:1001:1000:Usuari 1001:/home/user1001:/bin/bash
    user1002:+o4AcNq3dxAK9c4g==:1002:1000:Usuari 1002:/home/user1002:/bin/bash
    user1003:==:1003:1000:Usuari 1003:/home/user1003:/bin/bash
    user1004:==:1004:1000:Usuari 1004:/home/user1004:/bin/bash
    user1005:/HtOA==:1005:1000:Usuari 1005:/home/user1005:/bin/bash
    user1006:+ZnY2rIaC0UQ0U4Q==:1006:1000:Usuari 1006:/home/user1006:/bin/bash
    user1007:==:1007:1000:Usuari 1007:/home/user1007:/bin/bash
    user1008:1QhZn+JsQi3tla3s8Vg0g==:1008:1000:Usuari 1008:/home/user1008:/bin/bash
    user1009:+scAvsw==:1009:1000:Usuari 1009:/home/user1009:/bin/bash
    user1010:+II+gef8G26KwIR40R3g==:1010:1000:Usuari 1010:/home/user1010:/bin/bash
    user1011:pDMQd4snmdM+tGP684mPQ==:1011:1000:Usuari 1011:/home/user1011:/bin/bash
    user1012:shtHMzZaVxLmzeBFXQ7uZcA==:1012:1000:Usuari 1012:/home/user1012:/bin/bash
    user1013:+i+1q5zA2NWzH+wcyOM0w==:1013:1000:Usuari 1013:/home/user1013:/bin/bash
    user1014:YSTN2cswThMECKAz350kQ==:1014:1000:Usuari 1014:/home/user1014:/bin/bash
    user1015:==:1015:1000:Usuari 1015:/home/user1015:/bin/bash
    user1016:==:1016:1000:Usuari 1016:/home/user1016:/bin/bash
    user1017:==:1017:1000:Usuari 1017:/home/user1017:/bin/bash
    user1018:==:1018:1000:Usuari 1018:/home/user1018:/bin/bash
    user1019:+eLkjV/d6yg==:1019:1000:Usuari 1019:/home/user1019:/bin/bash
    user1020:==:1020:1000:Usuari 1020:/home/user1020:/bin/bash
    user1021:+Cg==:1021:1000:Usuari 1021:/home/user1021:/bin/bash
    user1022:D7sIZngLxjwAsj0VVLd8g==:1022:1000:Usuari 1022:/home/user1022:/bin/bash
    user1023:==:1023:1000:Usuari 1023:/home/user1023:/bin/bash
    user1024:/og==:1024:1000:Usuari 1024:/home/user1024:/bin/bash
    user1025:+wMYM7kiFr8VE0c1Tg==:1025:1000:Usuari 1025:/home/user1025:/bin/bash

**Sample Input 3**



**Sample Output 3**

    user1001:==:1001:1000:Usuari 1001:/home/user1001:/bin/bash

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
