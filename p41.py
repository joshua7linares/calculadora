a=input("Ingresa una medida en metros: ")
def centimetros(a):
  print "en cm esto equivale a: ", a*100

def milimetros(a):
  print "en mm esto equivale a: ", a*1000

def kilometros(a):
   print "en km esto equivale a: ", a/1000

b=input(" a que quieres convertirlo: 1. centimetro  2. milimetros 3. kilometros")

if b==1:
  centimetros(a)

if b==2:
  milimetros(a)

if b==3:
  kilometros(a)  

