class Pelicula:

  # Constructor
  def __init__(self, titulo, duracion, lanzamiento) -> None:
    self.titulo = titulo
    self.duracion = duracion
    self.lanzamiento = lanzamiento

  # Sobreescribiendo el método str
  def __str__(self) -> str:
    return f"{self.titulo} {self.lanzamiento}"

class Catalogo:
  peliculas = []

  def __init__(self, peliculas = []) -> None:
    self.peliculas = peliculas
  
  def agregar(self, pelicula):
    self.peliculas.append(pelicula)
  
  def mostarCatalogo(self):
    for p in self.peliculas:
      print(p)

p1 = Pelicula("El padrino", 175, 1972)
p2 = Pelicula("El padrino II", 200, 1974)
c = Catalogo([p1, p2])
c.mostarCatalogo()

c.agregar(Pelicula("El capitán américa", 124, 2011))
c.agregar(Pelicula("El hombre araña 2", 127, 2004))
c.mostarCatalogo()

