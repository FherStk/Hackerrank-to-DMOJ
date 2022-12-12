
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=3)
p.pk = None
p.code="a-hello-world"
p.name="[ac081] Hello World ASCII-art  #literals"
p.summary="Imprimeix el missatge Hello World"
p.description='''Imprimeix "HELLO WORLD" en ASCII-Art

**Input Format**

\-

**Constraints**

\-

**Output Format**

\-

**Sample Output 0**

    "%   *&  %)&>*%  =+     &!     /&![%{\    +,       ?<  .:;*!<,  ])<;]>   )!     /<-[\>
    <;   {<  -%      -%     <%     :;   [;    {;       "*  ?{   ?!  ?*   \|  :=     \|   ?    ,![=+((  }:;=.   <;     ?-     }[   }*     ?]  -  '*   &:   [.  +;=-:,   =]     )"    ;)
    *)   .>  -]      {!     |;     =<   -.     {; |(| <%   ,|   (%  -,  .\   }-     ?/   +?
    %+   *&  })=(\{  "<}&%  &[/|>  \+]&"!/      <\' '(+    '&![%{'  [%   ?<  %|<?+  ;=?%&'

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
