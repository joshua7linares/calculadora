
#calculo del punto intermedio
class PIN:
  def __init__(self):
    self.x1=0
    self.x2=0
    self.y1=0
    self.y2=0
    self.x=0
    self.y=0 
    self.xm=0
    self.ym=0
    self.m=0
    self.d=0
  def ingresar(self):
    self.x1=input("ingresa la coordenada x del primer punto: ")
    self.y1=input("ingresa la coordenada y del primer punto: ")
    self.x2=input("ingresa la coordenada x del segundo punto: ")
    self.y2=input("ingresa la coordenada y del segundo punto: ")
 
  def punto_intermedio(self):
    self.xm=(self.x1+self.x2)/2
    self.ym=(self.y1+self.y2)/2
    print "el punto intermendio es: "
    print "xm=", self.xm
    print "ym=", self.ym

  def ecuacion(self):
    self.m=(self.x2-self.x1)/(self.y2-self.y1)
    a=self.y1-(self.m*self.x1)
    if a<0:
      print "y=",self.m,"x",a
    else:
      print "y=",self.m,"x","+",a

  def distancia(self):
    self.x=pow(self.x2-self.x1,2)
    self.y=pow(self.y2-self.y1,2)
    self.d=pow(self.x+self.y,0.5)
    print self.d


d1=PIN()
d1.ingresar()
opc=input ("que deseas realizar: 1.Calcular el punto intermedio 2.Generar la ecuacion de la recta 3.calcular la distancia entre los dos puntos" )
if opc==1:
  d1.punto_intermedio()
if opc==2:
  d1.ecuacion()
if opc==3:
  d1.distancia()

