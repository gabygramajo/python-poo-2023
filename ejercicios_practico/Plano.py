# import Punto
from Punto import Punto

class Plano:
  def __init__(self) -> None:
    pass

  def dibujar_punto(self, p1, p2):
    y = 10
    x = -21
    for row in range(0, 21):
      y -= 1
      for col in range(0, 41):
        x += 1

        if(x == p1.x and y == p1.y):
          print("*", end="")
          continue

        if(x == p2.x and y == p2.y):
          print("*", end="")
          continue

        if(y == 0 and x != 0):
          print("-", end="")
          continue

        if(x == 0):
          print("|", end="")
          continue

        print(" ", end="")

      print("", end="\n")
      x = -21


plano1 = Plano()

p1 = Punto(2, 2)
p2 = Punto(5, 6)

plano1.dibujar_punto(p1, p2)