
ni=int(input("limite inferior del intervalo: "))
ns=int(input("limite superior del intervalo: "))
m=int(2)
band="true"


def primo(ni,ns,m,band):
   for i in range(ni,ns+1):
      while band=="true" and m!=i:
         if i%m==0:
            band="false"
         else:
             m=m+1       
      if band=="true":
         m=2
         print i

      else:
         m=2
         band="true"
   

print "los numeros primos en este intervalo son: "
primo(ni,ns,m,band)
