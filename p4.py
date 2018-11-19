#detecta los valores pares dentro de un intervalo
print "Linares Alonso Joshua A."
a=input("ingresa el primer valor del intervalo: ")
b=input("ingresa el segundo valor del intervalo: ")
def ran(a,b):
  print "los numeros pares en el intervalo son: "
  for i in range(a,b+1):
    if i%2==0:
      print i

def con(a,b):
   while (a>b or a==b):
      print "Error. Ingresa de nuevo los limites del intervalo"
      a1=input("ingresa el primer valor del intervalo: ")
      b1=input("ingresa el segundo valor del intervalo: ")
      a=a1
      b=b1
   ran(a,b)

if a<b:
  ran(a,b)
else:
  con(a,b)
