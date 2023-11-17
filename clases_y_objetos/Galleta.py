# La clase es como un molde para crear objetos
class Galleta:
  # Atributo de la Clase
  chocolate = False

  # Constructor
  def __init__(self, sabor= None, forma= None) -> None:
    self.sabor = sabor
    self.forma = forma
    if sabor is not None and forma is not None:
      print(f"galleta creada {sabor} y {forma}")

  # Métodos
  def chocolatear(self):
    self.chocolate = True

  def tiene_chocolate(self):
    if(self.chocolate):
      print("La galleta está chocolateada")
    else:
      print("La galleta no está chocolateada")


# instanciando el objeto
galleta1 = Galleta("salada", "cuadrada")
print(type(galleta1))

galleta1.tiene_chocolate()
galleta1.chocolatear()
galleta1.tiene_chocolate()
