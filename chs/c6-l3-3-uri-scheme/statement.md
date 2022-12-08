Completa la classe URL, i el mètode main()

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
