
print "Traza de una matriz "
print "Linares Alonso Joshua A."
matriz1=[]
res=0

def crear(f,c,matriz):
  for i in range (3):
     matriz.append([0]*3)

def ingresar(f,c,matriz):
  for i in range(f):
     for j in range(c):
       print "fila: ", i+1, "coluumna: ", j+1
       matriz[i][j]=input("ingresa valor: ")

def mostrar(matriz):  
 for i in matriz:
    for j in i:
      print j,
    print

def res(matriz):
  d1=matriz[0][0]*matriz[1][1]*matriz[2][2]
  d2=matriz[0][1]*matriz[1][2]*matriz[2][0]
  d3=matriz[1][0]*matriz[2][1]*matriz[0][2]
  d4=matriz[0][2]*matriz[1][1]*matriz[2][0]
  d5=matriz[1][0]*matriz[0][1]*matriz[2][2]
  d6=matriz[1][2]*matriz[2][1]*matriz[0][0]
  res=(d1+d2+d3)-(d4+d5+d6)
  if res==0:
   print "esta matriz no tiene inversa"
  else:
    print "esta matriz si tiene inversa"


f1=3
c1=3


crear(f1,c1,matriz1)
ingresar(f1,c1,matriz1)
mostrar(matriz1)
res(matriz1)








