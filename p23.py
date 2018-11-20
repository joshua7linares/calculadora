
print "Ecuacion de segundo grado: ax^2+bx+c=0"
class Ecu2d0():
  def __init(self):
    self.a=0
    self.b=0
    self.c=0
    self.dis=0
    self.x=0
    self.y=0

  def ingresar(self):
    self.a=input("ingresa el valor de a: ")  
    self.b=input("ingresa el valor de b: ")
    self.c=input("ingresa el valor de c: ")
 
  def raices(self):  
    self.dis=pow(self.b,2)-(4*self.a*self.c)
    if self.dis==0:
      print "la ecuacion soluciones reales y repetidas (solo tiene una solucion)"
    if self.dis<0:
      print "la ecuacion no tiene raices en el campo de los reales (soluciones complejas)"
    if self.dis>0:
      print "la ecuacion tiene dos soluciones reale y diferentes"   
 
  def incognitas(self):
       s=self.b/(2*self.a)
       if self.dis==0:
         self.x=-s
         print "la solucion es: ", self.x
       if self.dis>0:
          self.x=-s+pow(self.dis,0.5)/(2*self.a)  
          print "primera solucion: ",self.x
          self.y=-s-pow(self.dis,0.5)/(2*self.a)
          print "segunda solucion: ",self.y

ec=Ecu2d0()
ec.ingresar()
ec.raices()
ec.incognitas()

