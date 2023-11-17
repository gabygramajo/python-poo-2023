class Pelicula:

  # Constructor
  def __init__(self, titulo, duracion, lanzamiento) -> None:
    self.titulo = titulo
    self.duracion = duracion
    self.lanzamiento = lanzamiento
    print("se creó la película", self.titulo)

  # Destructor: borra la instancia de la clase en memoria al finalizar el programa
  def __del__(self) -> str:
    print("se está borrando la película", self.titulo)

  # Sobreescribiendo el método str
  def __str__(self) -> str:
    return f"La película {self.titulo} fué lanzada en {self.lanzamiento} con una duración de {self.duracion} minutos"

  # Sobreescribiendo el método len
  def __len__(self) -> int:
    return self.duracion

# Los métodos especiales __init__ y __del__ marcan el principio y el fin de la vida de un objeto


p1 = Pelicula("El padrino", 175, 1972)

print(str(p1))
print(len(p1))