#determina los divisores de un numero
n=int(input("ingresa un valor:"))
def div(n):
 m=1
 while m!=n:
   if n%m==0:
     print m
     m=m+1
   else:  
     m=m+1

print "los divisores de este numero son: "
div(n) 
