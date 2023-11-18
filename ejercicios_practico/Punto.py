import math

class Punto:

  def __init__(self, x = 0, y = 0) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f"({self.x},{self.y})"
  
  def cuadrante(self):

    if(self.x > 0 and self.y > 0):
      return "1er cuadrante"
    elif(self.x < 0 and self.y > 0):
      return "2do cuadrante"
    elif(self.x < 0 and self.y < 0):
      return "3er cuadrante"
    elif(self.x > 0 and self.y < 0):
      return "4to cuadrante"
    else:
      return "Ordenada al origen"
  
  def crear_vector(self, p):
    componente_a = p.x - self.x 
    componente_b = p.y - self.y 
    return f"({componente_a}, {componente_b})"
  
  def distancia(self, p):
    componente_a = p.x - self.x 
    componente_b = p.y - self.y 
    distancia = math.sqrt( ( componente_a**2 + componente_b**2 ) )
    return f"{round(distancia, 2)}"