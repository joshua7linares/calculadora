#distingue entre los numeros que son divisores y los que no lo son
n=int(input("ingresa un valor:"))
def div(n):
 m=1
 while m!=n:
   if n%m==0:
     print m, "es divisor"
     m=m+1
   else:
     print  m, "no es divisor" 
     m=m+1

div(n)     
