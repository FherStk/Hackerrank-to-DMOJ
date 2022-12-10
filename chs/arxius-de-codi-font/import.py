
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id=1)
p.pk = None
p.code="arxius-de-codi-font"
p.name="Arxius de codi font  #scanner"
p.summary="Arxius de codi font"
p.description='''![image](1601159416-d284b37cf1-srctypes.png)

Cada llenguatge de programació té les seves pròpies extensions per als
arxius de codi font.

Els de Java són , els JavaScript són , en Python és , en
C++ és  ...

Donada una llista d'arxius amb el nom i tipus, imprimeix la llista en
l'ordre invers, i les columnes intercanviades (primer tipus i després
nom).

**Input Format**

L'entrada consta de **quatre** línies.

En cada línia hi ha una paraula que es el  de l'arxiu (amb l'extensió
inclosa), y la resta de la línia és el  d'arxiu.

**Constraints**

\-

**Output Format**

S'imprimirà cada arxiu en una línia, primer el  i després el 

**Sample Input 0**

    main.cpp Archivo C++
    Main.java Archivo Java
    program.py Archivo Python
    script.js Archivo JavaScript

**Sample Output 0**

    Archivo JavaScript script.js 
    Archivo Python program.py 
    Archivo Java Main.java 
    Archivo C++ main.cpp 

**Sample Input 1**

    index.php Archivo PHP
    sample.cs Archivo C#
    app.swift Archivo Swift
    MainActivity.kt Archivo Kotlin

**Sample Output 1**

    Archivo Kotlin MainActivity.kt
    Archivo Swift app.swift
    Archivo C# sample.cs
    Archivo PHP index.php

**Sample Input 2**

    index.ts Archivo TypeScript
    out.asm Archivo assembler
    query.sql Archivo Structured Query Language
    main.rs Archivo Rust

**Sample Output 2**

    Archivo Rust main.rs
    Archivo Structured Query Language query.sql
    Archivo assembler out.asm
    Archivo TypeScript index.ts
'''
p.is_public=True
p.date=timezone.now()
p.save()
