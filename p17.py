
#determina los divisores comunes de un par de numeros
print "ingresa dos valores enteros diferentes"
a=input("ingresa el primer valor: ")
b=input("ingresa el segundo valor: ")

if a==b:
  print "los valores deben ser distintos"
  a=input("ingresa el primer valor: ")
  b=input("ingresa el segundo valor: ")
n=1
m=0
c=0
while n<=b:
  if a%n==0 and b%n==0:
    c=n
    print n
    m=m+1
    n=n+1
  else:
    n=n+1

print "numero de divisores comunes: ",m
print "el maximo comun divisor es: ", c

