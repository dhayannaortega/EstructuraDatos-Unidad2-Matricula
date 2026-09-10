class SolicitudMatricula:
  def __init__(self,documento,nombre,programa,valor):
      self.documento = documento
      self.nombre = nombre
      self.programa = programa
      self.valor = valor

class ColaProcesamientoMatricula:
  def __init__(self,capacidad):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.tamaño = 0

  def esta_vacia(self):
    if self.tamaño ==0:
        return True
    else:
        return False

  def esta_llena(self):
    if self.tamano == self.capacidad:
        
