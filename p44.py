
print "linares alonso joshua "

def collatz(n):
  while n>1:
    if n%2==0:
      n=n/2
      print n
    else:
      n=n*3+1
      print n

def primo(n):
  m=int(2)
  band="true"
  while band=="true" and m!=n:
      if n%m==0:
          band="false"
      else:
          m=m+1
       
  if band=="true":
      print "el numero es primo"
  else:
      print "el numero no es primo"

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





n=input("ingresa un numero: ")
opc=input("que deseas hacer con el valor introducido: 1.Aplicarle la conjetura de collatz 2.Verificar si es un numero primo 3.Verificar si es un numero perfecto")

if opc==1:
  collatz(n)
if opc==2:
   primo(n)
if opc==3:
   div(n)

