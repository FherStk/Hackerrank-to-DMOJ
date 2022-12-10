
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="b46d0-postsstream-class-l0"
p.name="[b46d0] PostsStream #class #L0"
p.summary="PostsStream"
p.description='''Crea els objectes necessaris.

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Input 0**

    3
    @popeye http://img.io/1234.jpg Hola que tal
    @olivia http://img.io/facb.jpg Adios adios
    @brutus http://img.io/9k8h.jpg Hasta luego

**Sample Output 0**

    @popeye
    Hola que tal
    ------------------------------
    @olivia
    Adios adios
    ------------------------------
    @brutus
    Hasta luego
    ------------------------------

**Sample Input 1**

    2
    @user_one null Blank message
    @user_two null Empty message

**Sample Output 1**

    @user_one
    Blank message
    ------------------------------
    @user_two
    Empty message
    ------------------------------
'''
p.is_public=True
p.date=timezone.now()
p.save()
