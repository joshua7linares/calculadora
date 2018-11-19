
print "linares alonso joshua "
print " determina si un numero es primo o no"
m=int(2)
band="true"
numero=int(input("ingresa un numero: "))
while band=="true" and m!=numero:
    if numero%m==0:
        band="false"
    else:
        m=m+1


       
if band=="true":
    print "el numero es primo"
else:
    print "el numero no es primo"
