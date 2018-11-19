
print "resta de matrices "
print "Linares Alonso Joshua A."
matriz1=[]
matriz2=[]
res=[]

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

def resul(res,matriz1,matriz2,f1,c1):
   for i in range(f1):
     for j in range(c1):
         res[i][j]=matriz1[i][j]-matriz2[i][j]
   mostrar(res)  


print "primera matriz"
f1=input("ingresa el numero de filas: ")
c1=input("ingresa el numero de columnas: ")
print "segunda matriz"
f2=input("ingresa el numero de filas: ")
c2=input("ingresa el numero de columnas: ")

if f1==f2 and c1==c2:
   crear(f1,c1,matriz1)
   ingresar(f1,c1,matriz1)
   mostrar(matriz1)
   crear(f2,c2,matriz2)
   ingresar(f2,c2,matriz2)
   mostrar(matriz2)
   crear(f1,c1,res)
   print "el resultado es: "
   resul(res,matriz1,matriz2,f1,c1)

else:
  print "las matrices deben ser del mismo orden"   
