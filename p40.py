print "Linares Alonso Joshua A."
print "producto de los terminos de una fila elegida en una matriz"

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

def flc(f,c,matriz):
   fe=input("cual fila escoges para multiplicar sus valores: ")
   res=1
   for i in range(f):
     for j in range(c):
         if i==fe-1:
            res=res*matriz[i][j]
   print "el resultado es:  ", res 



f=input("ingresa el numero de filas: ")
c=input("ingresa el numero de columnas: ")
crear(f,c,matriz)
mostrar(matriz)
flc(f,c,matriz)

