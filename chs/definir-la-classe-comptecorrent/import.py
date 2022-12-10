
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="definir-la-classe-comptecorrent"
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
'''
p.is_public=True
p.date=timezone.now()
p.save()
