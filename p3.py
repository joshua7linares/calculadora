
# producto vectorial de dos vectores
v1=[0,0,0]
v2=[0,0,0]
v3=[0,0,0]
#ingreso de los valores
def intov(v):
   for i in range(0,3):
       v[i]=input("ingresa valor: ")
   print v
#operador
def op(v1,v2,v3):
    a=v1[1]*v2[2]-v1[2]*v2[1]
    b=v1[2]*v2[0]-v1[0]*v2[2]
    c=v1[0]*v2[1]-v1[1]*v2[0]
    v3[0]=a
    v3[1]=b
    v3[2]=c
    print "El producto vectorial es: "
    print v3
   
intov(v1)
intov(v2)
op(v1,v2,v3)
