print "Traza de una matriz "
print "Linares Alonso Joshua A."
matriz1=[]
res=0

def crear(f,c,matriz):
  for i in range (f):
     matriz.append([0]*c)

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

def resul(res,matriz1,f1,c1):
   for i in range(f1):
     for j in range(c1):
         if i==j:
            res=res+matriz1[i][j]
   print "La traza es: ", res

f1=input("ingresa el numero de filas: ")
c1=input("ingresa el numero de columnas: ")

while f1!=c1:
     print "la matriz debe ser cuadrada"
     f2=input("ingresa el numero de filas: ")
     c2=input("ingresa el numero de columnas: ")
     f1=f2
     c1=c2

crear(f1,c1,matriz1)
ingresar(f1,c1,matriz1)
mostrar(matriz1)
resul(res,matriz1,f1,c1)   
