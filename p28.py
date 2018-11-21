
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

  def ingresar(self):
    self.x1=input("ingresa la coordenada x del primer punto: ")
    self.y1=input("ingresa la coordenada y del primer punto: ")
    self.x2=input("ingresa la coordenada x del segundo punto: ")
    self.y2=input("ingresa la coordenada y del segundo punto: ")
 
  def calculo(self):
    self.xm=(self.x1+self.x2)/2
    self.ym=(self.y1+self.y2)/2
    print "el punto intermendio es: "
    print "xm=", self.xm
    print "ym=", self.ym




d1=PIN()
d1.ingresar()
d1.calculo()

