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

def traza(f,c, matriz):
   res=0
   for i in range(f):
     for j in range(c):
         if i==j:
            res=res+matriz[i][j]
   print "La traza es: ", res

     

def sumaf(f,c,matriz):
   fe=input("cual fila escoges para sumar sus valores: ")
   res=0
   for i in range(f):
     for j in range(c):
         if i==fe-1:
            res=res+matriz[i][j]
   print "el resultado es:  ", res


def sumac(f,c,matriz):
   ce=input("cual fila escoges para sumar sus valores: ")
   res=0
   for i in range(f):
     for j in range(c):
         if j==ce-1:
            res=res+matriz[i][j]
   print "el resultado es:  ", res 




f=input("ingresa el numero de filas: ")
c=input("ingresa el numero de columnas: ")
crear(f,c,matriz)
mostrar(matriz)
opc=input("que deseas hacer: 1.Calcular la traza de la matriz  2.Sumar los valores de una columna   3.sumar los valores de una fila ")

if opc==1:
    traza(f,c,matriz)
if opc==2:
    sumac(f,c,matriz)
if opc==3:
   sumaf(f,c,matriz)






