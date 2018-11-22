#calcula la suma de los valores de una columna
print "Linares Alonso Joshua A."
f=input("ingresa el numero de filas: ")
c=input("ingresa el numero de columnas: ")
ce=input("cual columna escoges para sumar sus valores: ")
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

res=0
for i in range(f):
     for j in range(c):
         if j==ce-1:
            res=res+matriz[i][j]
print "el resultado es:  ", res


