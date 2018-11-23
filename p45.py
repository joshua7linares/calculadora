
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
      print n,"es numero un primo"
  else:
      print n," no es numero primo"

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
div(n)
primo(n)
print "conjetura de collatz para", n
collatz(n)

