import sys
from ejercicios_practico.Punto import Punto
from ejercicios_practico.Rectangulo import Rectangulo

def main() -> int:
  pA = Punto(2, 3)
  pB = Punto(5, 5)
  pC = Punto(-3, -1)
  pD = Punto(0, 0)

  print("-------- Punto ---------")
  print(f"1) A: {pA} B: {pB} C: {pC} D: {pD}")
  print(f"2) A: {pA.cuadrante()} B: {pB.cuadrante()} C: {pC.cuadrante()} D: {pD.cuadrante()}")
  print(f"3) AB: {pA.crear_vector(pB)}  BA: {pB.crear_vector(pA)}")
  print(f"4) distancia A a B: {pA.distancia(pB)} distancia B a A: {pB.distancia(pA)}")
  print(f"5) B: {pD.distancia(pB)}")
  print("----- Rectangulo ------")
  r = Rectangulo(pA, pB)
  print(f"- base: {r.base()}\n- altura: {r.altura()}\n- area: {r.area()}")


if __name__ == '__main__':
  sys.exit(main())