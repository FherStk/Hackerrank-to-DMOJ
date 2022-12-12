
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="definir-la-classe-co"
p.name="Definir la classe CompteCorrent #class"
p.summary="Definir la classe CompteCorrent"
p.description='''Defineix una classe anomenada CompteCorrent. Ha de tenir tres camps: un
enter , un String , i un boolean .

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
