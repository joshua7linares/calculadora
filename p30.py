
# ubica el centro y calcula el radio de una circunferencia que pase por los dos puntos ingresados por el usuario
class Cir:
  def __init__(self):
    self.x1=0
    self.x2=0
    self.y1=0
    self.y2=0 
    self.xr=0
    self.yr=0
    self.xc=0
    self.yc=0
    self.r=0

  def ingresar(self):
    self.x1=input("ingresa la coordenada x del primer punto: ")
    self.y1=input("ingresa la coordenada y del primer punto: ")
    self.x2=input("ingresa la coordenada x del segundo punto: ")
    self.y2=input("ingresa la coordenada y del segundo punto: ")

  def ucentro(self):
    self.xc=(self.x1+self.x2)/2
    self.yc=(self.y1+self.y2)/2
    print "el centro de la circunferencia es: "
    print "xc", self.xc
    print "yc", self.yc
 
  def calradio(self):
    self.xr=pow(self.x2-self.xc,2)
    self.yr=pow(self.y2-self.yc,2)
    self.r=pow(self.xr+self.yr,0.5)
    print "el radio es: ", self.r


c=Cir()
c.ingresar()
c.ucentro()
c.calradio()

