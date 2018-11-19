
# producto escalar de dos vectores
v1=[0,0,0]
v2=[0,0,0]
v3=[0,0,0]

def intov(v):
   for i in range(0,3):
       v[i]=input("ingresa valor: ")
   print v

def suma(v):
    res=0
    for i in range(0,3):
        res=res+v[i]
   
    print res

def result(v1,v2,v3):
    for i in range (0,3):
       v3[i]=v1[i]*v2[i]
    print "el producto escalar es: "
    suma(v3)


intov(v1)
intov(v2)
result(v1,v2,v3)

