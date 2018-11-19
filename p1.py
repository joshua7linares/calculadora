
print "suma de vectores en tres dimensiones"
print "linares alonso joshua "
v1=[0,0,0]
v2=[0,0,0]
v3=[0,0,0]
def intov(v):
  for i in range(0,3):
    v[i]=input("introduce valor: ")
  print v  

def suma(v1,v2,v3):
  for i in range(0,3):
    v3[i]=v1[i]+v2[i]
  print v3
 
print "primer vector"
intov(v1)
print "segundo vector"
intov(v2)
print "resultado de la suma"
suma(v1,v2,v3)

