
#ecuacion de una recta con dos puntos
class Recta:
  def __init__(self):
    self.x1=0
    self.x2=0
    self.y1=0
    self.y2=0
    self.m=0
 
  def ingresar(self):
    self.x1=input("ingresa la coordenada x del primer punto: ")
    self.y1=input("ingresa la coordenada y del primer punto: ")
    self.x2=input("ingresa la coordenada x del segundo punto: ")
    self.y2=input("ingresa la coordenada y del segundo punto: ")
 
  def ecuacion(self):
    self.m=(self.x2-self.x1)/(self.y2-self.y1)
    a=self.y1-(self.m*self.x1)
    if a<0:
      print "y=",self.m,"x",a
    else:
      print "y=",self.m,"x","+",a

d=Recta()
d.ingresar()
d.ecuacion()

