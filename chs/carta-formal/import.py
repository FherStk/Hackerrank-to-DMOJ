
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="carta-formal"
p.name="Carta formal  #scanner"
p.summary="Carta formal"
p.description='''Desitjem enviar una carta formal als nostres clients, i volem generar de
forma automàtica l'encapçalament per a cada client.

A la nostra base de dades de client tenim els camps: tractament, nom,
cognom1 i cognom2.

Fes un programa que generi aquest encapçalament amb el format que
s'observa a **Sample Output**

**Input Format**

L'entrada consta de 4 línies:

    tractament
    nom
    cognom1
    cognom2

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    Senyor
    Antoni
    Perez
    Sales

**Sample Output 0**

    Senyor Perez Sales, Antoni
    
    El principal objectiu de la present carta...

**Sample Input 1**

    Excelentissima senyora
    Maria Antonia
    de la Fuente
    Rodriguez

**Sample Output 1**

    Excelentissima senyora de la Fuente Rodriguez, Maria Antonia
    
    El principal objectiu de la present carta...

**Sample Input 2**

    Sra.
    Juana
    Garcia
    Romero

**Sample Output 2**

    Sra. Garcia Romero, Juana
    
    El principal objectiu de la present carta...
'''
p.is_public=True
p.date=timezone.now()
p.save()
