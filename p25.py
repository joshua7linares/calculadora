
print "Ecuacion de primer grado: ax+b"
class Ecu1er():
  def __init(self):
    self.a=0
    self.b=0
    self.x=0
  def ingresar(self):
    self.a=input("ingresa el valor de a: ")  
    self.b=input("ingresa el valor de b: ")

  def incognita(self):  
    self.x=-(self.b/self.a)
    print "la solucion a la ecuacion es: ", self.x


ec=Ecu1er()
ec.ingresar()
ec.incognita()

