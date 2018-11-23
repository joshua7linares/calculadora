print "Linares Alonso Joshua A."
print "producto de los terminos de la diagonal principal de una matriz"

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
   print "el resultado es: ", res


f=input("ingresa el numero de filas: ")
c=input("ingresa el numero de columnas: ")
crear(f,c,matriz)
mostrar(matriz)
diagonal(f,c,matriz)

