
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="valors-correctes"
p.name="Valors correctes  #variables"
p.summary="Valors correctes"
p.description='''Assigna els valors adequats a les següents variables, per tal d'obtenir
el resultat que s'indica a **Sample Output**.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    true
    35.6
    2000.0
    true
    true
'''
p.is_public=True
p.date=timezone.now()
p.save()
