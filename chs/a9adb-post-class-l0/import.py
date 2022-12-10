
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="a9adb-post-class-l0"
p.name="[a9adb] Post #class #L0"
p.summary="Post"
p.description='''Implementa el constructor de la classe Post.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    ------------------------------------
    | @realdonaltrump                  |
    | Make America Great Again #MAGA   |
    | <3 2000000        & 10000000     |
    ------------------------------------
    ------------------------------------
    | @realdonaltrump                  |
    | You are fake news                |
    | <3 5986587        & 325646       |
    ------------------------------------
    ------------------------------------
    | @realdonaltrump                  |
    | Global warming is a HOAX         |
    | <3 200            & 1000         |
    ------------------------------------
'''
p.is_public=True
p.date=timezone.now()
p.save()
