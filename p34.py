matriz1=[]
res=0
print "Linares Alonso Joshua A."
opc=input("que deseas hacer" "1.Determinante 2x2""2.Determinante 3x3")
def crear2(matriz):
  for i in range (2):
     matriz.append([0]*2)

def ingresar2(matriz):
  for i in range(2):
     for j in range(2):
       print "fila: ", i+1, "coluumna: ", j+1
       matriz[i][j]=input("ingresa valor: ")

def mostrar2(matriz):  
 for i in matriz:
    for j in i:
      print j,
    print

def resul2(matriz1,res):
      res=matriz1[0][0]*matriz1[1][1]-matriz1[0][1]*matriz1[1][0]
      print "el resultado es: ", res

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
  print "el determinante es: ",res


f1=3
c1=3




if opc==1:
  crear2(matriz1)
  ingresar2(matriz1)
  mostrar2(matriz1)
  resul2(matriz1,res)

if opc==2:
   crear(f1,c1,matriz1)
   ingresar(f1,c1,matriz1)
   mostrar(matriz1)
   res(matriz1)





