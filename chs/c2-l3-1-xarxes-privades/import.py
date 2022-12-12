
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c2-l3-1-xarxes-priva"
p.name="[C2-L4-2] Xarxes privades #if"
p.summary="Xarxes privades"
p.description='''A l'arquitectura d'adreçament d'Internet, una xarxa privada és una xarxa
que utilitza l'espai d'adreces IP privades:

  - 10.0.0.0 - 10.255.255.255
  - 172.16.0.0 - 172.31.255.255
  - 192.168.0.0 - 192.168.255.255

Les adreces privades no s'asignen a cap organització concreta i
qualsevol persona pot utilitzar aquestes adreces sense l'aprovació d'un
Registre Regional d'Internet.

La xarxa a la que pertany un ordinador es calcula a partir de la seva IP
i la seva màscara de xarxa:

1.  Es passa cada nombre de la ip a un octet binari, i es coloquen
    consecutivament els quatre octets.
2.  Es crea un nombre binari amb tants 1 com indica la màscara i es
    completa amb 0 fins a 32 bits.
3.  Es realitza la operació AND entre el primer i el segon nombre. El
    valor resultant és la IP on comença la xarxa
4.  Es crea un nombre binari amb tants 0 com indica la màscara i es
    completa amb 1 fins a 32 bits.
5.  Es realitza la operació OR entre el primer i el segon nombre. El
    valor resultant és la IP on acaba la xarxa

![image](1556701591-d5c4f2c2f1-netmask.png)

**Input Format**

La entrada consta dels quatre octets d'una adreça IP i una màscara de
xarxa, separats per espais en blanc.

**Constraints**

La IP i la màscara són vàlides

**Output Format**

S'imprimirà la primera adreça de la xarxa, la última adreça, i
s'indicarà si és una adreça pública o privada.

**Sample Input 0**

    192 168 55 118
    24

**Sample Output 0**

    First IP: 192.168.55.0
    Last IP: 192.168.55.255
    Private

**Sample Input 1**

    192 168 55 118
    11

**Sample Output 1**

    First IP: 192.160.0.0
    Last IP: 192.191.255.255
    Public

**Sample Input 2**

    10 2 2 1
    11

**Sample Output 2**

    First IP: 10.0.0.0
    Last IP: 10.31.255.255
    Private

**Sample Input 3**

    172 16 2 1
    22

**Sample Output 3**

    First IP: 172.16.0.0
    Last IP: 172.16.3.255
    Private

**Sample Input 4**

    35 16 23 214
    24

**Sample Output 4**

    First IP: 35.16.23.0
    Last IP: 35.16.23.255
    Public

**Sample Input 5**

    35 16 23 214
    8

**Sample Output 5**

    First IP: 35.0.0.0
    Last IP: 35.255.255.255
    Public

**Sample Input 6**

    8 8 8 8
    30

**Sample Output 6**

    First IP: 8.8.8.8
    Last IP: 8.8.8.11
    Public

**Sample Input 7**

    172 32 16 0
    12

**Sample Output 7**

    First IP: 172.32.0.0
    Last IP: 172.47.255.255
    Public

**Sample Input 8**

    172 15 255 0
    22

**Sample Output 8**

    First IP: 172.15.252.0
    Last IP: 172.15.255.255
    Public

**Sample Input 9**

    10 0 0 1
    6

**Sample Output 9**

    First IP: 8.0.0.0
    Last IP: 11.255.255.255
    Public

**Sample Input 10**

    235 84 63 17
    19

**Sample Output 10**

    First IP: 235.84.32.0
    Last IP: 235.84.63.255
    Public

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
