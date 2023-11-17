class Perro:
  # Atributo de Clase
  tipo_de_mastoca = "Perro"
  cont = 0
  __ID = 0

  def __init__(self, nombre, raza) -> None:
    # Atributos de instancia
    self.nombre = nombre
    self.raza = raza
    # Contador de instancias
    Perro.cont += 1
    Perro.__ID += 1

  def __obtener_id(self):
    return self.__ID

  def mostrar_cant_de_instancias(self)-> str:
    return self.cont

  def mostrar_id(self)-> str:
    return self.__obtener_id()

perros = [
    {"nombre": "Rocky", "raza": "Ovejero Alemán"},
    {"nombre": "Bella", "raza": "Labrador Retriever"},
    {"nombre": "Max", "raza": "Golden Retriever"},
    {"nombre": "Luna", "raza": "Bulldog Francés"},
    {"nombre": "Charlie", "raza": "Chihuahua"},
    {"nombre": "Daisy", "raza": "Dachshund"},
    {"nombre": "Cooper", "raza": "Beagle"},
    {"nombre": "Lucy", "raza": "Shih Tzu"},
    {"nombre": "Leo", "raza": "Poodle"},
    {"nombre": "Zoe", "raza": "Siberian Husky"}
]

# Imprimir el array de perros
for perro in perros:
  Perro(perro["nombre"], perro["raza"])

print("cantidad de instantias:", Perro.cont)
print("tipos de mastocas:", Perro.tipo_de_mastoca)

p1 = Perro("Mora", "American Pitbull")
print("cantidad de instantias: ", p1.cont)
print("tipo de mastoca: ", p1.tipo_de_mastoca)
print("ID:", p1.mostrar_id())

Perro.tipo_de_mastoca = "Gato"
print("tipos de mastocas:", Perro.tipo_de_mastoca)
print("tipo de mastoca: ", p1.tipo_de_mastoca)


"""
Atributos de Clase:

- Los atributos de clase son compartidos por todas las instancias de una clase.
- Se definen dentro de la clase pero fuera de cualquier método.
- Pueden ser accedidos utilizando el nombre de la clase o una instancia de la clase.
- Si se modifica el valor del atributo de clase, el cambio se reflejará en todas las instancias y en la propia clase.

Atributos de Instancia:

- Los atributos de instancia son específicos de cada instancia de una clase.
- Se definen dentro del método __init__ (o en otros métodos) utilizando self.
- Cada instancia puede tener diferentes valores para estos atributos.
"""
