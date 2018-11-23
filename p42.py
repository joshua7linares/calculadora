print "Linares Alonso Joshua A."


matriz=[]
def crear(f,c,matriz):
   for i in range (f):
      matriz.append([0]*c)
   
   for i in range(f):
     for j in range(c):
      print "fila: ", i+1, "coluumna: ", j+1
      matriz[i][j]=input("ingresa valor: ")


def mostrar(matriz):
 for i in matriz:
   for j in i:
      print j,
   print    

def diagonal(f,c, matriz):
   res=1
   for i in range(f):
     for j in range(c):
         if i==j:
            res=res*matriz[i][j]
   print "La traza es: ", res

     

def flm(f,c,matriz):
   fe=input("cual fila escoges para multiplicar sus valores: ")
   res=1
   for i in range(f):
     for j in range(c):
         if i==fe-1:
            res=res*matriz[i][j]
   print "el resultado es:  ", res


def mlc(f,c,matriz):
   ce=input("cual columna escoges para multiplicar sus valores: ")
   res=1
   for i in range(f):
     for j in range(c):
         if j==ce-1:
            res=res*matriz[i][j]
   print "el resultado es:  ", res 




f=input("ingresa el numero de filas: ")
c=input("ingresa el numero de columnas: ")
crear(f,c,matriz)
mostrar(matriz)
opc=input("que deseas hacer: 1.producto de la diagonal principal 2.Producto de una columna 3.Producto de una fila ")

if opc==1:
    diagonal(f,c,matriz)
if opc==2:
    mlc(f,c,matriz)
if opc==3:
    flm(f,c,matriz)
