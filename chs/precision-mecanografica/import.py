
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="precision-mecanografica"
p.name="Precisión mecanográfica"
p.summary="Describe la precisión mecanográfica a partir del número de caracteres y los errores cometidos."
p.description='''En unas pruebas de mecanografía se pide teclear un texto y se mide la
precisión y la velocidad:

  - La PRECISIÓN se mide en **Porcentaje** entre el número de caracteres
    del texto y el número de errores cometidos.

  - La VELOCIDAD se mide en **Palabras Por Minuto** (se considera que
    **una palabra son 5 caracteres -sin importar si son letras, signos o
    espacios-**).

Dados los datos de una prueba, determina la precisión y la velocidad.

Los datos de una prueba consisten en el número de caracteres del texto,
el número de errores cometidos y el tiempo empleado **(en segundos)**.

**Input Format**

La entrada consta de tres números:

L: número de caracteres del texto

E: número de errores cometidos

T: tiempo empleado (en segundos)

**Constraints**

1 \<= L \<= 1000

0 \<= E \<= L

1 \<= T \<= 1000

**Output Format**

Se debe imprimir la Precisión (porcentaje de aciertos) y la Velocidad
(palabras por minuto), cada uno en una línea, y sin decimales.

**Sample Input 0**

    100 10 60

**Sample Output 0**

    90
    20

**Explanation 0**

Si en un texto de **100** caracteres se han cometido **10** errores y se
ha tardado **60** segundos, el resultado de la prueba es:

Precisión: **90**%

Velocidad: **20** PPM

**Sample Input 1**

    10 3 60

**Sample Output 1**

    70
    2

**Explanation 1**

Si en un texto de **10** caracteres se han cometido **3** errores y se
ha tardado **60** segundos, el resultado de la prueba es:

Precisión: **70**%

Velocidad: **2** PPM

**Sample Input 2**

    60 0 10

**Sample Output 2**

    100
    72

**Explanation 2**

Si en un texto de **60** caracteres se han cometido **0** errores y se
ha tardado **10** segundos, el resultado de la prueba es:

Precisión: **100**%

Velocidad: **72** PPM

**Sample Input 3**

    300 37 65

**Sample Output 3**

    87
    55

**Sample Input 4**

    789 7 165

**Sample Output 4**

    99
    57

**Sample Input 5**

    60 60 6

**Sample Output 5**

    0
    120
'''
p.is_public=True
p.date=timezone.now()
p.save()
