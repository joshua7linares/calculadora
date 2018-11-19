
#determina si un nuemro es perfecto
n=int(input("ingresa un valor:"))
def div(n):
 suma=0
 m=1
 while m!=n:
   if n%m==0:
     suma=suma+m
     m=m+1
   else:  
     m=m+1
 if suma==n:
   print n, "es un numero perfecto"
 else:
   print n, "no es un numero perfecto" 

div(n)    

