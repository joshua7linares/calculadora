print "Linares Alonso Joshua A."
v1=[0,0,0]
v2=[0,0,0]
v3=[0,0,0]
#ingreso de los valores
def intov(v):
   for i in range(0,3):
       v[i]=input("ingresa valor: ")
   print v
#operador
def pv(v1,v2,v3):
    a=v1[1]*v2[2]-v1[2]*v2[1]
    b=v1[2]*v2[0]-v1[0]*v2[2]
    c=v1[0]*v2[1]-v1[1]*v2[0]
    v3[0]=a
    v3[1]=b
    v3[2]=c
    print "El producto vectorial es: "
    print v3

def suma(v):
    res=0
    for i in range(0,3):
        res=res+v[i]
   
    print res

def pe(v1,v2,v3):
    for i in range (0,3):
       v3[i]=v1[i]*v2[i]
    print "el producto escalar es: "
    suma(v3)

def suma_al(v1,v2,v3):
  for i in range(0,3):
    v3[i]=v1[i]+v2[i]
  print v3

print "componentes del primer vector: "   
intov(v1)
print "componentes del segundo vector"
intov(v2)

opc=input("que operacion deseas realizar: 1.suma  2.producto escalar 3.producto vectorial")
if opc==1:
   suma_al(v1,v2,v3)
if opc==2:
   pe(v1,v2,v3)
if opc==3:
   pv(v1,v2,v3)
