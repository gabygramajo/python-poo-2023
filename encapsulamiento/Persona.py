
# Clase sin encapsulamiento
class Persona:
  # Atributo privado
  nombre_completo = "Nicolás González"

  def __init__(self, apodo) -> None:
    self.apodo = apodo
  
  def mostar_info(self):
    return self.__nombre_completo

# Clase con encapsulamiento
class Estudiante:
  # Atributo PRIVADO de clase
  __legajo = "BRT1235C"

  def __init__(self, nombre_completo, edad, dni) -> None:
    # Atributos PRIVADOS de instancia
    self.__nombre_completo = nombre_completo
    self.__edad = edad
    self.__dni = dni

  # Métodos Privados que sirven como puente para poder acceder a los atributos privados
  def __obtener_nombre_completo(self):
    return self.__nombre_completo
  
  def __obtener_edad(self):
    return self.__edad
  
  def __obtener_dni(self):
    return self.__dni
  
  # Método Público
  def mostrar_info(self):
    return f"{self.__obtener_nombre_completo()} - {self.__obtener_edad()} años"


p1 = Persona("El máquina")

# Ambos atributos son perfectamente accesibles desde el exterior. Son públicos
print(p1.apodo)
print(p1.nombre_completo)

# solo puedo acceder a los atributos o métodos que estén públicos
e1 = Estudiante("Luis Gutiérez", 15, 11775522)
print(e1.mostrar_info())