
class Distancia:
  def __init__(self):
    self.x1=0
    self.x2=0
    self.y1=0
    self.y2=0
    self.x=0
    self.y=0 
    self.d=0 
 
  def ingresar(self):
    self.x1=input("ingresa la coordenada x del primer punto: ")
    self.y1=input("ingresa la coordenada y del primer punto: ")
    self.x2=input("ingresa la coordenada x del segundo punto: ")
    self.y2=input("ingresa la coordenada y del segundo punto: ")

  def calculo(self):
    self.x=pow(self.x2-self.x1,2)
    self.y=pow(self.y2-self.y1,2)
    self.d=pow(self.x+self.y,0.5)
    print self.d

def main():
   d1=Distancia()
   d1.ingresar()
   d1.calculo()

main()

