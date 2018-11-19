
#detecta los multiplo de un numero dentro de un intervalo
print "Linares Alonso Joshua A."
a=input("ingresa el primer valor del intervalo: ")
b=input("ingresa el segundo valor del intervalo: ")
c=input("ingresa valor cuyos multiplos deban ser localizados: ")

def ran(a,b,c):
  print "los multiplos en el intervalo son: "
  for i in range(a,b+1):
    if i%c==0 or i==c:
      print i

def con(a,b,c):
   while (a>b or a==b):
      print "Error. Ingresa de nuevo los limites del intervalo"
      a1=input("ingresa el primer valor del intervalo: ")
      b1=input("ingresa el segundo valor del intervalo: ")
      c1=input("ingresa valor cuyos multiplos deban ser localizados: ")
      a=a1
      b=b1
      c=c1
   ran(a,b,c)

if a<b:
  ran(a,b,c)
else:
  con(a,b,c)
