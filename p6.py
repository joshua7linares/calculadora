#recibe una matriz y la muestra
print "creacion de matrices "
print "Linares Alonso Joshua A."
f=input("ingresa el numero de filas: ")
c=input("ingresa el numero de columnas: ")
matriz=[]
for i in range (f):
    matriz.append([0]*c)

for i in range(f):
    for j in range(c):
      print "fila: ", i+1, "coluumna: ", j+1
      matriz[i][j]=input("ingresa valor: ")

for i in matriz:
   for j in i:
      print j,
   print 
