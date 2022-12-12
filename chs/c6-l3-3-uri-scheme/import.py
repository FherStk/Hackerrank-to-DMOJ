
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="c6-l3-3-uri-scheme"
p.name="[b60ca] URI Scheme #class"
p.summary="URI Scheme"
p.description='''Completa la classe URL, i el mètode main()

**Input Format**

La entrada consta de 5 línies:

  - protocol
  - domain
  - path
  - query
  - fragment

**Constraints**

\-

**Output Format**

S'imprimirà la URL ben formada.

**Sample Input 0**

    http
    www.mydomain.com
    /path/to
    query=true
    fragment1

**Sample Output 0**

    http://www.mydomain.com/path/to?query=true#fragment1

**Sample Input 1**

    https
    anotherdomain.cat
    /path/to/page
    q=1&s=1
    frag

**Sample Output 1**

    https://anotherdomain.cat/path/to/page?q=1&s=1#frag

**Sample Input 2**

    https
    domainname.org
    /document
    t=www&s=1
    new

**Sample Output 2**

    https://domainname.org/document?t=www&s=1#new

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
'''
p.is_public=False
p.date=timezone.now()
p.save()
