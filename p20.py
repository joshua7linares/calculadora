
def mult(a1,a2,b1,b2):
  dr=a1*a2-b1*b2
  di=a1*b2+b1*a2
  print "el resultado de la multiplicacion es: "
  mostrar_r(dr,di)

def mostrar_r(a,b):
  if(b<0):
   print a,b,"i"
  else:
    print a,"+",b,"i"

def m(a1,a2,b1,b2):
  if (b1<0 and b2<0):
   print "Z1=",a1,b1,"i"
   print "Z2=",a2,b2,"i"
  if(b1<0 and b2>0):
    print "Z1=",a1,b1,"i"
    print "Z2=",a2,"+",b2,"i"
  if(b1>0 and b2<0):
    print "Z1=",a1,"+",b1,"i"
    print "Z2=",a2,b2,"i"  
  if(b1>0 and b2>0):
    print "Z1=",a1,"+",b1,"i"
    print "Z2=",a2,"+",b2,"i"


print "Ingresa el primer numero complejo"
a1=input("parte real")
b1=input("parte imaginaria")


print "Ingresa el segundo numero complejo"
a2=input("parte real")
b2=input("parte imaginaria")


opc=input("1.Multiplicacion  2.Calcular el modulo") 
if(opc==1):
   m(a1,a2,b1,b2)
   mult(a1,a2,b1,b2)


if(opc==2):
   m(a1,a2,b1,b2)
