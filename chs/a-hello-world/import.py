
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
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
'''
p.is_public=True
p.date=timezone.now()
p.save()
