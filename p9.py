
print "Determinante de una matriz 2x2 "
print "Linares Alonso Joshua A."
matriz1=[]
res=0

def crear(matriz):
  for i in range (2):
     matriz.append([0]*2)

def ingresar(matriz):
  for i in range(2):
     for j in range(2):
       print "fila: ", i+1, "coluumna: ", j+1
       matriz[i][j]=input("ingresa valor: ")

def mostrar(matriz):  
 for i in matriz:
    for j in i:
      print j,
    print

def resul(matriz1,res):
      res=matriz1[0][0]*matriz1[1][1]-matriz1[0][1]*matriz1[1][0]
      print "el resultado es: ", res


crear(matriz1)
ingresar(matriz1)
mostrar(matriz1)
resul(matriz1,res)
