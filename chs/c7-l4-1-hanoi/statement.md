Escriu un algorisme recursiu per a solucionar el joc de les Torres de
Hanoi

**Input Format**

La entrada consisteix en el número de discs

**Constraints**

1 \<= N \<= 10

**Output Format**

Predefinit

**Sample Input 0**

``` 
3
```

**Sample Output 0**

``` 
   #      |      |   
  ###     |      |   
 #####    |      |   
---------------------
   |      |      |   
  ###     |      |   
 #####    |      #   
---------------------
   |      |      |   
   |      |      |   
 #####   ###     #   
---------------------
   |      |      |   
   |      #      |   
 #####   ###     |   
---------------------
   |      |      |   
   |      #      |   
   |     ###   ##### 
---------------------
   |      |      |   
   |      |      |   
   #     ###   ##### 
---------------------
   |      |      |   
   |      |     ###  
   #      |    ##### 
---------------------
   |      |      #   
   |      |     ###  
   |      |    ##### 
---------------------
```

**Sample Input 1**

``` 
2
```

**Sample Output 1**

``` 
  #    |    |  
 ###   |    |  
---------------
  |    |    |  
 ###   #    |  
---------------
  |    |    |  
  |    #   ### 
---------------
  |    |    #  
  |    |   ### 
---------------
```

**Sample Input 2**

``` 
4
```

**Sample Output 2**

``` 
    #        |        |    
   ###       |        |    
  #####      |        |    
 #######     |        |    
---------------------------
    |        |        |    
   ###       |        |    
  #####      |        |    
 #######     #        |    
---------------------------
    |        |        |    
    |        |        |    
  #####      |        |    
 #######     #       ###   
---------------------------
    |        |        |    
    |        |        |    
  #####      |        #    
 #######     |       ###   
---------------------------
    |        |        |    
    |        |        |    
    |        |        #    
 #######   #####     ###   
---------------------------
    |        |        |    
    |        |        |    
    #        |        |    
 #######   #####     ###   
---------------------------
    |        |        |    
    |        |        |    
    #       ###       |    
 #######   #####      |    
---------------------------
    |        |        |    
    |        #        |    
    |       ###       |    
 #######   #####      |    
---------------------------
    |        |        |    
    |        #        |    
    |       ###       |    
    |      #####   ####### 
---------------------------
    |        |        |    
    |        |        |    
    |       ###       #    
    |      #####   ####### 
---------------------------
    |        |        |    
    |        |        |    
    |        |        #    
   ###     #####   ####### 
---------------------------
    |        |        |    
    |        |        |    
    #        |        |    
   ###     #####   ####### 
---------------------------
    |        |        |    
    |        |        |    
    #        |      #####  
   ###       |     ####### 
---------------------------
    |        |        |    
    |        |        |    
    |        |      #####  
   ###       #     ####### 
---------------------------
    |        |        |    
    |        |       ###   
    |        |      #####  
    |        #     ####### 
---------------------------
    |        |        #    
    |        |       ###   
    |        |      #####  
    |        |     ####### 
---------------------------
```

**Sample Input 3**

``` 
5
```

**Sample Output 3**

``` 
     #          |          |     
    ###         |          |     
   #####        |          |     
  #######       |          |     
 #########      |          |     
---------------------------------
     |          |          |     
    ###         |          |     
   #####        |          |     
  #######       |          |     
 #########      |          #     
---------------------------------
     |          |          |     
     |          |          |     
   #####        |          |     
  #######       |          |     
 #########     ###         #     
---------------------------------
     |          |          |     
     |          |          |     
   #####        |          |     
  #######       #          |     
 #########     ###         |     
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
  #######       #          |     
 #########     ###       #####   
---------------------------------
     |          |          |     
     |          |          |     
     #          |          |     
  #######       |          |     
 #########     ###       #####   
---------------------------------
     |          |          |     
     |          |          |     
     #          |          |     
  #######       |         ###    
 #########      |        #####   
---------------------------------
     |          |          |     
     |          |          |     
     |          |          #     
  #######       |         ###    
 #########      |        #####   
---------------------------------
     |          |          |     
     |          |          |     
     |          |          #     
     |          |         ###    
 #########   #######     #####   
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
     |          #         ###    
 #########   #######     #####   
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
    ###         #          |     
 #########   #######     #####   
---------------------------------
     |          |          |     
     |          |          |     
     #          |          |     
    ###         |          |     
 #########   #######     #####   
---------------------------------
     |          |          |     
     |          |          |     
     #          |          |     
    ###       #####        |     
 #########   #######       |     
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
    ###       #####        |     
 #########   #######       #     
---------------------------------
     |          |          |     
     |          |          |     
     |         ###         |     
     |        #####        |     
 #########   #######       #     
---------------------------------
     |          |          |     
     |          #          |     
     |         ###         |     
     |        #####        |     
 #########   #######       |     
---------------------------------
     |          |          |     
     |          #          |     
     |         ###         |     
     |        #####        |     
     |       #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |         ###         |     
     |        #####        |     
     #       #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
     |        #####       ###    
     #       #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          #     
     |        #####       ###    
     |       #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          #     
     |          |         ###    
   #####     #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
     |          #         ###    
   #####     #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
    ###         #          |     
   #####     #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     #          |          |     
    ###         |          |     
   #####     #######   ######### 
---------------------------------
     |          |          |     
     |          |          |     
     #          |          |     
    ###         |       #######  
   #####        |      ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          #     
    ###         |       #######  
   #####        |      ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          #     
     |          |       #######  
   #####       ###     ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |          |     
     |          #       #######  
   #####       ###     ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |        #####   
     |          #       #######  
     |         ###     ######### 
---------------------------------
     |          |          |     
     |          |          |     
     |          |        #####   
     |          |       #######  
     #         ###     ######### 
---------------------------------
     |          |          |     
     |          |         ###    
     |          |        #####   
     |          |       #######  
     #          |      ######### 
---------------------------------
     |          |          #     
     |          |         ###    
     |          |        #####   
     |          |       #######  
     |          |      ######### 
---------------------------------
```

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
